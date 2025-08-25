import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(__file__ + "/../.."))

from bakeit import PasteryUploader


class BasicTest(unittest.TestCase):
    def test_upload(self):
        pu = PasteryUploader("apikey")
        with self.assertRaises(RuntimeError):
            pu.upload("hello")
