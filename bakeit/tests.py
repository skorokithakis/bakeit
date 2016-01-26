import os
import sys
import unittest
import pep8

sys.path.insert(0, os.path.abspath(__file__ + "/../.."))

from bakeit import PasteryUploader


class BasicTest(unittest.TestCase):
    def test_upload(self):
        pu = PasteryUploader("apikey")
        with self.assertRaises(RuntimeError):
            pu.upload("hello")

    def test_pep8(self):
        pep8style = pep8.StyleGuide([['statistics', True],
                                     ['show-sources', True],
                                     ['repeat', True],
                                     ['ignore', "E501"],
                                     ['paths', [os.path.dirname(
                                         os.path.abspath(__file__))]]],
                                    parse_argv=False)
        report = pep8style.check_files()
        assert report.total_errors == 0
