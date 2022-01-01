import random

import requests


def via(gateway):
    return IPFS(gateway)


def lower_keys(dictList):
    return [{k.lower(): v for k, v in entry.items()} for entry in dictList]


class IPFS:
    def __init__(self, gateway):
        assert len(gateway) > 0
        self._gateway = gateway
        self._cache = {}

    def get_links(self, path, params):
        url = self._gateway + "/api/v0/dag/get"
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        rjson = r.json()
        return lower_keys(
            filter(
                lambda link: len(link["Name"]) > 0
                and "/" in (link.get("Cid") or link["Hash"]),
                rjson.get("links") or rjson["Links"],
            )
        )

    def list(self, hash):
        """Get the directory content of the given hash"""
        assert type(hash) == str
        if hash in self._cache:
            if len(self._cache) > 50:
                # Drop 10 keys
                for k in random.sample(self._cache.keys(), 10):
                    del self._cache[k]
            return self._cache[hash]

        entries = self.get_links("/api/v0/dag/get", params={"arg": hash})
        self._cache[hash] = entries
        return entries

    def link(self, hash):
        return self._gateway + "/ipfs/" + hash
