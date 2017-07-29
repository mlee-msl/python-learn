#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
prime generator
'''

def odds():
	'generate odd series which begins with 3'
	n = 3
	while True:
		yield n
		n += 2

def primes():
	'generator: a series of primes'
	yield 2 # 2 of the first prime
	g = odds()
	while True:
		n = next(g)
		yield n # return the first num of current series 
		g = filter(lambda x : x % n != 0, g)

def main(limit=10):
	for i in primes():
		if i < limit:
			yield i
		else:
			break

if __name__ == '__main__':
	limit = int(input('Please type max value:'))
	main(limit)
