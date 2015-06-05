'''
Unit tests for ExampleLibary.py
'''

#if __name__ == '__main__' and __package__ is None:
#    from os import sys, path
#    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import unittest
import ExampleLibrary as e


class MyTests(unittest.TestCase):
    '''
    Basic unittest approach
    '''
    def test_multiply_by_two(self):
        '''
        Basic 
        '''
        self.assertTrue(e.multiply_by_two(6) == 12.0)

    @classmethod
    def test_greet_me(cls):
        '''
        Unit test
        '''
        e.greet_me(122)




if __name__ == '__main__':
    unittest.main()
