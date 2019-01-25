
import requests
import random

def via(gateway):
    return IPFS(gateway)

class IPFS:
    def __init__(self, gateway):
        assert len(gateway) > 0
        self._gateway = gateway
        self._cache = {}

    def get(self, path, params):
        r = requests.get(self._gateway + '/api/v0/dag/get', params=params, timeout=20)
        r.raise_for_status()
        return r

    def list(self, hash):
        """Get the directory content of the given hash"""
        assert type(hash) == str
        if hash in self._cache:
            if len(self._cache) > 50:
                #Drop 10 keys
                for k in random.sample(self._cache.keys(), 10):
                    del self._cache[k]
            return self._cache[hash]

        r = self.get('/api/v0/dag/get', params={"arg": hash})
        r.raise_for_status()

        entries = list(filter(lambda link: len(link['Name']) > 0 and '/' in link['Cid'], r.json()["links"]))
        self._cache[hash] = entries
        return entries

    def link(self, hash):
        return self._gateway + "/ipfs/" + hash
