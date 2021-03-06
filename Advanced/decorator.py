# -*- coding:utf-8 -*-

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2017-8-29')

#相当于省略了now = log(now)

now()

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本:

def logger(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('execute')
def now():
    print('2017-8-29')

#相当于省略了now = log('execute')(now)

now()

#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

def log(func):
	def wrapper(*args, **kw):
		print('begin call %s():' % func.__name__)
		func(*args, **kw)
		print('end call %s():' % func.__name__)
	return wrapper

@log
def now():
	print('2017-9-1')

now()

##再思考一下能否写出一个@log的decorator，使它既支持：@log 又支持@log('execute')

import functools

def log1(text):

	if isinstance(text, str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('%s %s():' % (text, func.__name__))
				return func(*args, **kw)
			return wrapper
		return decorator

	else:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('call %s():' % func.__name__)
				return func(*args, **kw)
			return wrapper
		return decorator

@log1('execute')
def now():
	print('2017-9-1')

now()

#这里一直报错，说缺少一个位置参数，后来添加了一个None就运行成功了，可是原理不明，再学几课再回来研究研究。
@log1(None)
def now():
	print('2017-9-1')

now()
