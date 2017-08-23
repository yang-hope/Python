# -*- coding:utf-8 -*-
#关于map

def normalize(name):
	return str(name).title()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#关于reduce
from functools import reduce

def prod(L):
	def multi(x,y):
		return x*y

	return reduce(multi, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#关于map&reduce
