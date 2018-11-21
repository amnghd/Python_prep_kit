# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:31:56 2018

@author: Amin
"""
import timeit
# replace spcaes with %20 
# sample input "Mr Garet Bale   "
# sample output "Mr%20Garet%20Bale"


def URLifier(string, n):
    
    return string.strip().replace(" ","%20")

assert URLifier("Mr Garet Bale    ",13) == "Mr%20Garet%20Bale"