#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time

class Timer:
	def __init__(self):
		self.prompt = "Please start..."
		self.unit = ["年", "月", "日", "时", "分", "秒"]
		self.__start = 0
		self.__end = 0

	def start(self):
		print("Starting...")
		self.__start = time.localtime()
		self.prompt = "Please end"

	def end(self):
		if not self.__start:
			print("Please start firstly...")
		else:
			print("End")
			self.__end = time.localtime()
			self.__calc()
	
	def __calc(self):
		self.cost = []
		self.prompt = "Total cost: "
		for i in range(6):
			self.cost.append(self.__end[i] - self.__start[i])
		self.__convert()
		for i in range(6):
			if self.cost[i]:
				self.prompt += str(self.cost[i])+self.unit[i]

	def __convert(self):
		d = {1: 12, 2: 30, 3: 24, 4: 60, 5: 60}
		for i in reversed(range(1, len(self.cost))):
			if self.cost[i] < 0:
				self.cost[i] += d[i]
				self.cost[i-1] -= 1
			
		
	def __repr__(self):
		return self.prompt

if __name__ == "__main__":
	pass	
