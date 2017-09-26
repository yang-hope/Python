# -*- coding:utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')

def run_twice(Animal):
	Animal.run()
	Animal.run()

a=Animal()
b=Dog()
c=Cat()
d=Tortoise()

print('a is Animal?', isinstance(a, Animal))
print('b is Animal?', isinstance(b, Animal))
print('b is Dog?', isinstance(b, Dog))
print('c is Cat?', isinstance(c, Cat))
print('a is Cat?', isinstance(a, Cat))

run_twice(a)
run_twice(c)
run_twice(d)
