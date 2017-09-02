#!/usr/bin/python3
#-*- coding: utf-8 -*-

def bubbleSort(arr):
	for i in range(len(arr)):
		for ii in reversed(range(i+1, len(arr))):
			if arr[ii] < arr[ii-1]:
				arr[ii], arr[ii-1] = arr[ii-1], arr[ii]
	return arr

if __name__ == "__main__":
	arr = input("Type a list> ").split()
	for (index, value) in enumerate(arr):
		try:
			arr[index] = int(value)
		except Exception as err:
			print(err)
			exit(0)
		finally:
			pass
	print(bubbleSort(arr))
