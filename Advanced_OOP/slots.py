# -*- coding:utf-8 -*-

class Student(object):
	__slots__ = ('name', 'age') #允许绑定的属性名称

class GraduateStudent(Student):
	pass

s = Student()
s.name = 'Nora'
s.age = 26
print('s.name =', s.name)
print('s.age =', s.age)

s.score = 99
print('s.score =', s.score)

g = GraduateStudent()
g.score = 99
print('g.score=', g.score)
