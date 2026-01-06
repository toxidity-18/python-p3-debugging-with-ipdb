#!/usr/bin/env python3

from ipdb_debugging import plus_two # this is used to find the function named plus_two inside the other file ipdb_debugging.py

class TestIpdbDebugging: #container which keep all the related test together .
    '''ipdb_debugging.py'''
    
    def test_adds_two(self): # the mission or rather the test that pytest will run automatically .
        '''adds_two() adds 2 to input arg and returns sum.'''
        assert(plus_two(3) == 5) # assert is like a boolean either return true or false .

