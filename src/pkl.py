#!/usr/bin/python3
#-*- coding: utf-8 -*-

import pickle

if __name__ == "__main__":
	d = {"001": "武汉", "002": "上海", "003": "南京", "004": "天津"}
	with open("/home/mlee/Desktop/tmp.txt", "wb+") as f:
		pickle.dump(d, f)
		D = pickle.load(f)
		print(D)
else:
	print("imported")

