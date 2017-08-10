# -*- coding:utf-8 -*-

from collections import Iterable

print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? [1,2,3]:', isinstance([1,2,3], Iterable))
print('Iterable? 123:', isinstance(123, Iterable))

print('for key in d:')
d = {'a':1, 'b':2, "c":3}
for key in d:
	print (key)

print('for ch in \'ABC\':')
for ch in 'ABC':
	print(ch)

print('for i, value in enumerate([\'A\', \'B\', \'C\']):')
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

print('for x, y in [(1,1), (2,4), (3,9)]:')
for x, y in [(1,1), (2,4), (3,9)]:
	print (x,y)
