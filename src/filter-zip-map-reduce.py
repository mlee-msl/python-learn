#!/usr/bin/python
# -*- coding:utf-8 -*-

"
This module test four functions about filter & zip & map & reduce
"

if __name__ == '__main__':
	print(__doc__)
	#############################################################
	#					filter
	#############################################################
	l1 = list(filter(lambda x : x % 2, range(50)))
	print('filter: %s' % l1)

	#############################################################
	#					zip
	#############################################################
	l2 = list(zip(range(1, 50, 3), range(1, 100, 2)))
	print('zip: %s' % l2)

	#############################################################
	#					map
	#############################################################
	l3 = list(map(lambda x, y, z : x + 2* y + 3 * z, range(10), range(10, 30, 2), range(2, 12))) # 序列长度要求一样，依次对应传给x,y,z
	print('map: %s' % l3)

	#############################################################
	#					reduce
	#############################################################
	from functools import reduce
	l4 = reduce(lambda x, y : x + 2* y, range(100))
	print('reduce: %s' % l4)

	l5 = reduce(lambda x, y : 10 * x + y, range(1,10))
	print('reduce: %s' % l5)

	l6 = int(reduce(lambda x, y : str(x) + str(y), range(1,10)))
	print('reduce: %d' % l6)

