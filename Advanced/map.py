# -*- coding:utf-8 -*-

def normalize(name):
	return str(name).title()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
