# -*-coding: utf-8 -*-

# type()

print('type(123)=', type(123))
print('type(\'123\')=', type('123'))
print('type(None)=', type(None))
print('type(abs)=', type(abs))

import types

print('type(\'abc\')==str?', type('abc')==str)

#attrs

class MyObject(object):

	def __init__(self):
		self.x = 12

	def power(self):
		return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\')=', hasattr(obj, 'x')) #有属性'x'吗？
print('hasattr(obj, \'y\')=', hasattr(obj, 'y')) #有属性'y'吗？
setattr(obj, 'y', 20) #设置一个属性'y'
print('hasattr(obj, \'y\')=', hasattr(obj, 'y')) #有属性'y'吗？
print('getattr(obj, \'y\')=', getattr(obj, 'y')) #获取属性'y'
print('obj.y=', obj.y) #获取属性'y'

print('getattr(obj, \'z\')=', getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

f=getattr(obj, 'power') #获取属性'power'
print(f)
print(f())