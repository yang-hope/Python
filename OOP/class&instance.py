#-*- coding:utf-8 -*-

class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson', 90)

print(bart.name)

bart.print_score()

print(bart.get_grade())

#类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

#方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据。
