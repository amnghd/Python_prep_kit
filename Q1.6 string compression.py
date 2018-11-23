# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 21:22:14 2018

@author: Amin
"""

# time complexity is O(N-1)=O(N), and space complexity is O(N/2)=O(N)
import unittest


def compressor(string):
    n = len(string)
    counter = 1 # initializing the counter with one since we start the loop from the second index
    recent_char = string[0]  # recent character is initialized by first chararcter
    compressed = list() # initializing a list to 
    
    i = 1
    while(i < n):
        if string[i] == recent_char:
            counter += 1
        if string[i]!= recent_char or i == n-1: # new character or end of string
            compressed.append((recent_char+str(counter)))
            recent_char = string[i] # updating the recent character
            counter = 1
        if 2*len(compressed) > n: # if length of new string has passed original one
            #largest array can be of size n/2 (each entry contains one letter and one number)
            return string
        i += 1
    
    return "".join(compressed)


# test sets from following
#https://github.com/careercup/CtCI-6th-Edition-Python/tree/e6bc732588601d0a98e5b1bc44d83644b910978d
    
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = compressor(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()