import sparser.urlsparser
import sparser.pagesparser
import sparser.sutil

import unittest
import sys

class TestAll(unittest.TestCase):

    def test_load_urlsparser(self):
        test_value = 'sparser.urlsparser'in sys.modules
        self.assertTrue(test_value)

    def test_load_pagesparser(self):
        test_value = 'sparser.pagesparser'in sys.modules
        self.assertTrue(test_value)

    def test_load_sutil(self):
        test_value = 'sparser.sutil'in sys.modules
        self.assertTrue(test_value)

if __name__ == "__main__":
    unittest.main()

