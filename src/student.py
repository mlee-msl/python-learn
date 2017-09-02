#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
class demonstration
'''

class Student(object):
	__slots__ = ('__name', '__gender', '__age') # limit attr of the instance

	def __init__(self, name, gender, age):
		self.__name = name   # __XXX means private variable which can't access out of class which implementit by changing the name of the attribute(like _Student__name) by interpreter
		self.__gender = gender
		self.__age = age
	
	def getName(self):
		return self.__name
	
	def getGender(self):
		return self.__gender

	def getAge(self):
		return self.__age

	def setName(self, name):
		if isinstance(name, str) and len(name) >= 2:
			self.__name = name
		else:
			raise ValueError('Invalid name')
	
	def setGender(self, gender = 'male'):
		if gender != 'male':
			self.__gender = 'female'
		else:
			self.__gender = 'male'

	def setAge(self, age):
		if isinstance(age, int) and age >=0 and age <=100:
			self.__age = age
		else:
			raise ValueError('Invalid age')

	def show(self):
		print('%s:%s:%s' % (self.__name, self.__gender, self.__age))
	
	def __len__(self):
		return len(self.__name) # if you define this method, you can use 'len' method as instance

	def __repr__(self): # the same as __str__
		'print object as return'
		return 'name:%s,gender:%s,age:%s' % (self.__name, self.__gender, self.__age)
