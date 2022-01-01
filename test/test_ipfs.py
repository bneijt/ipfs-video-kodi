# -*- coding: utf-8 -*-
import unittest
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
