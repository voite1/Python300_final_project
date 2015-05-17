

import unittest
import sys

class TestAll(unittest.TestCase):
    
    def setUp (self):
        import sparser.urlsparser
        import sparser.pagesparser
        import sparser.sutil

    def runTest(self):
        test_value = 'sparser.urlsparser' in sys.modules
        self.assertTrue(test_value)

        test_value = 'sparser.sutil' in sys.modules
        self.assertTrue(test_value)

        test_value = 'sparser.pagesparser' in sys.modules
        self.assertTrue(test_value)


def suite():
    suite = unittest.TestSuite()
    suite.addTest (TestAll())
    return suite


def runtests():
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
    return True 


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
    

