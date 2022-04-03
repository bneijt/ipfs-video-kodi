# -*- coding: utf-8 -*-
import pytest

import ipfs_video_kodi.ipfs as ipfs

test_gateway = ipfs.via("https://ipfs.io")


def test_list_directory_should_work():
    a = test_gateway.list("Qme4QjkyZQuFtN2SDhELfXVshMyAEec53jaFQ8kR4maLeV")
    assert len(a) == 1
    assert (
        a[0]["name"]
        == "Alan Kay at OOPSLA 1997 - The computer revolution hasnt happened yet.webm"
    )
    b = test_gateway.list("QmYHDhsgUgdKSAimguGC92MzQ8VNFHZw3yp6kAHwiXCFLm")
    assert len(b) == 3


@pytest.mark.skip(reason="uses remote systems")
def test_remote_apis():
    for gateway_url in [
        "http://127.0.0.1:8080",
        "https://ipfs.io",
        "https://dweb.link",
        "https://gateway.pinata.cloud",
    ]:
        remote_gw = ipfs.via(gateway_url)
        b = remote_gw.list("QmYHDhsgUgdKSAimguGC92MzQ8VNFHZw3yp6kAHwiXCFLm")
        assert len(b) == 3, f"Should be able to get listing from {gateway_url}"
