# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:53:52 2018

@author: Amin
"""
# test cases :
# s1= aabbcc, s2= abbcac ==> true
# s1= a, s2 =a ==> true
# s1=aa, s2=ab ==>false
# s1= abd, s2=abc ==> false

def is_permutation(s1,s2):
    return sorted(s1) == sorted(s2)

# time complexity = O(nlogn)
# space complexity O(1)
    
assert is_permutation("aabbcc","abbcac")== True
assert is_permutation("a","a")== True
assert is_permutation("aa","ab")== False
assert is_permutation("abd","abc")== False