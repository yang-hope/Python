# -*- coding:utf-8 -*-

def triangles():
	b = [1]
	while True:
		yield b
		b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
		# b = [sum(i) for i in zip([0]+b, b+[0])]
n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break
