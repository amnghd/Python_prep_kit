# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:49:30 2018

@author: Amin
"""
from itertools import permutations
# is it a permutation of palindrom?

def is_palindro(s):
    return s == s[::-1]

def is_perm_palindro(s):
    s = s.lower().replace(" ","")
    for perm in permutations(s):
        if is_palindro(perm):
            return True
    return False
        
# worst time complexity O(n!)
# space complexoty O(1)
    
def efficient_palindro(s):
    letter_dict = {} #initialize a hash table
    ctr = 0 # initialize a flag
    for c in s: #O(n)
        c = c.lower() # lowercasing the letter
        if c in letter_dict.keys():
            letter_dict[c] += 1
        else:
            letter_dict[c] = 1
    for v in letter_dict.values(): #O(b)
        if v < 2:
            ctr += 1
        if ctr>1:
            return False
    return True

#time complexity O(n)
# space complexity O(n)
print(efficient_palindro("tacocat"))