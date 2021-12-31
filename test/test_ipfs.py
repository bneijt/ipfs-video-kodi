# -*- coding: utf-8 -*-
import unittest
import ipfs_video_kodi.ipfs as ipfs

test_gateway = ipfs.via("http://127.0.0.1:5001")


def test_list_directory_should_work():
    a = test_gateway.list("Qme4QjkyZQuFtN2SDhELfXVshMyAEec53jaFQ8kR4maLeV")
    assert len(a) == 1
    assert (
        a[0]["Name"]
        == "Alan Kay at OOPSLA 1997 - The computer revolution hasnt happened yet.webm"
    )
