#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
prime generator
'''

def naturalNumbers():
	'generate natural numbers series which begins with 2'
	n = 2
	while True:
		yield n
		n += 1

def process(n):
	return lambda x : x % n != 0

def primes():
	'generator: a series of primes'
	g = naturalNumbers() # initialize series
	while True:
		n = next(g) # get the first num of current series
		yield n # return the first num of current series 
		# adjust current series as new series by the Sieve of Eratosthenes
#		g = filter(lambda x : x % n > 0, g) # method 1
		g = filter(process(n), g) # method 2
