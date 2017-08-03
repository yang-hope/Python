# -*- coding:utf-8 -*-

from random import randint

x = randint(0,300)
go = 'y'
while (go == 'y'):
	print ('please input a number between 0~300:')
	digit = int(input())
	if digit == x:
		print ('Bingo!')
		break
	elif digit > x:
		print ('Too big, please try again.')
	else:
		print ('Too small, please try again.')
	print ('if you do not want to continue, input n, or input y')
	go = input()
else:
	print ('Goodbye!')
