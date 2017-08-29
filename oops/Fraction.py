# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 00:05:03 2017

@author: narveer-rathore
"""
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        common = gcd(num, den)
        return Fraction(num//common, den//common)
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

fraction = Fraction(3, 5)
print(fraction)