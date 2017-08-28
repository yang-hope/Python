# -*- coding:utf-8 -*-

#python延迟绑定

#why returns [6,6,6,6] rather than [0,2,4,6]?

def multipliers():
	return [lambda x: i*x for i in range(4)]

print([m(2) for m in multipliers()])

# output:[6,6,6,6]

#fix
def multipliers():
	#添加默认参数a
	return [lambda x, a=i: a*x for i in range(4)]

print([m(2) for m in multipliers()])

#output:[0,2,4,6]

#因为匿名函数中的i并不是立即引用后面循环中的i值的，而是在运行嵌套函数的时候，才会查找i的值，这个特性也就是延迟绑定

#因为Python解释器，遇到lambda（类似于def）,只是定义了一个匿名函数对象，并保存在内存中，只有等到调用这个匿名函数的时候，才会运行内部的表达式，而for i in range(4) 是另外一个表达式，需等待这个表达式运行结束后，才会开始运行lambda 函数，
