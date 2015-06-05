import resourcefile
import os.path
import unittest

def what_are_the_functions():
    output = dir(resourcefile)
    print output
    return output

def is_the_library_called_marketplaceclient():
    print __name__
    print resourcefile.__name__
    return resourcefile.__name__

class TestresourcefileName(unittest.TestCase):
    def test_name(self):
        self.assertEqual(resourcefile.__name__, 'resourcefile')
        
    def test_name2(self):
        self.assertEqual(resourcefile.__name__, 'resourcefile')
    
    def test_py_get_variable_value(self):
        resourcefile.py_get_variable_value()
    


def run_python_unit_test():
    dir(__name__)
    suite = unittest.TestSuite()
    suite.addTest(TestresourcefileName('test_name'))
    suite.addTest(TestresourcefileName('test_name2'))
    suite.addTest(TestresourcefileName('test_py_get_variable_value'))
    result = unittest.TestResult()
    suite.run(result)
    print result
    
if __name__ == '__main__':
    unittest.main()
