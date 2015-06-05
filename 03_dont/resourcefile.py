'''
Bogus library
'''

from robot.libraries.BuiltIn import BuiltIn

def py_get_variable_value():
    '''
    Lorem Ipsum
    '''
    stuff = BuiltIn().get_variable_value("${XOXO}")
    print stuff
    return stuff
