# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:17:54 2018

@author: Amin
"""
# we make one assumption : algorithms needs to be case sensitive
def counter(string): # this develop a frequency table of the characters
    ''' More general for is available: from ollections import Counter'''
    letter_dict = {}
    for char in string:
        if char in letter_dict.keys():
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

def result_checker(remain_dict, flag):
    n = len(remain_dict)
    ctr_one = 0 # number of ones in my the remainder hash table values
    ctr_m_one = 0 # number of minus ones in the remainder hash table values
    
    for val in remain_dict.values():
        if val == 1:
            ctr_one += 1
        if val == -1:
            ctr_m_one += 1
    
    ctr_zero = n - ctr_one - ctr_m_one
    if (flag==1) and ((ctr_one==1) and (ctr_m_one==0)):
        return True
    elif ctr_zero == n-1 and flag==0:
        return True
    elif (ctr_zero == n-2) and ((ctr_one==1)and (ctr_m_one==1)) and flag==0:
        return True
    
    return False


def One_Away(s1,s2):
    if len(s1) - len(s2) > 1:
        return False
    letter_table = counter(s1)
    flag = 0
    
    for element in s2:
        if element in letter_table.keys():
            letter_table[element] -= 1
        else:
            flag += 1
            if flag >1:
                return False
    return result_checker(letter_table, flag)


print(One_Away('abcdef','abcdeg'))

# this is space complexity of O(256) and time complexity of O(SL) (SL:larger string)

