# -*- coding: utf-8 -*-
import unittest
import src.ipfs as ipfs

test_gateway = ipfs.via("http://51.15.122.1")


class TestIpfsMethods(unittest.TestCase):

    def test_list_file_should_be_empty(self):
        a = test_gateway.list("QmTNdv6MBhCjcGY5tpabi7aCeLZL65tmDzW37J9ZrFbZfL")
        self.assertEqual(a, [])

    def test_list_directory_should_work(self):
        a = test_gateway.list("QmVZV84e6nSwfA8LppiS4KXKiAhpbqqGYzofHtecQjd9js")
        self.assertEqual(len(a), 1)
        self.assertEqual(a[0]['Name'], "pexel")



if __name__ == '__main__':
    unittest.main()
