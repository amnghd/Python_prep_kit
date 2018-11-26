# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:43:30 2018

@author: Amin
"""
import unittest
 
def zero_matrix(array):
    row_list = list() # initializing a list for rows to keep the columns to be deleted
    column_list = list()
    
    R = len(array) # number of rows
    C = len(array[0]) # number of columns
    
    for r in range(R):
        for c in range(C):
            if array[r][c] == 0:
                row_list.append(r)
                column_list.append(c)
    
    # nullifying
    for row in row_list:
        for c in range(C):
            array[row][c] = 0
            
    for col in column_list:
        for r in range(R):
            array[r][col] = 0
            
    return array

#time complexity O(N*M)                
#space complexity O(max(N,M))
# tests are acessible from here:
# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/8_Zero%20Matrix/ZeroMatrix.py
    
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()