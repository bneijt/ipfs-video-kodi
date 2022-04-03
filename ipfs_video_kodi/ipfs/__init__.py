import random
import requests

MAX_CACHE_SIZE = 100


def via(gateway):
    return IPFS(gateway)


def lower_keys(dictList):
    return [{k.lower(): v for k, v in entry.items()} for entry in dictList]


class IPFS:
    def __init__(self, gateway):
        assert len(gateway) > 0
        self._gateway = gateway
        self._cache = {}

    def get_links(self, cid):
        params = {"arg": cid}
        url = self._gateway + "/api/v0/dag/get"
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        rjson = r.json()
        link_list = lower_keys(
            filter(
                lambda link: len(link["Name"]) > 0
                and "/" in (link.get("Cid") or link["Hash"]),
                rjson.get("links") or rjson["Links"],
            )
        )

        # Backwards compatibility
        for i in link_list:
            if "cid" in i:
                i["hash"] = i["cid"]
        return link_list

    def resolve_ipns(self, cid):
        params = {"arg": cid}
        url = self._gateway + "/api/v0/name/resolve"
        print(params)
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        rjson = r.json()
        path = rjson.get("Path") or rjson.get("path")
        assert path.startswith("/ipfs/"), "Should resolve to ipfs path"
        return path[len("/ipfs/") :]

    def list(self, path):
        """Get the directory content of the given path (ipns/hash or plain cid)"""
        assert type(path) == str, "Argument path must be a string"
        cid = self.resolve_ipns(path[len("/ipns/") :]) if path.startswith("/ipns/") else path

        if cid in self._cache:
            if len(self._cache) > MAX_CACHE_SIZE:
                # Drop 10 keys
                for k in random.sample(self._cache.keys(), 10):
                    del self._cache[k]
            return self._cache[cid]

        entries = self.get_links(cid)
        self._cache[cid] = entries
        return entries

    def link(self, hash):
        return self._gateway + "/ipfs/" + hash
