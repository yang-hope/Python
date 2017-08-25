# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#按名字排序
def by_name(t):
	return str.lower(t[0])

L1 = sorted(L, key=by_name)
print(L1)

# 按成绩从高到低排序
def by_score(t):
	return t[1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2)
