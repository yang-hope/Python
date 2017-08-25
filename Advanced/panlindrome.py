# -*- coding: utf-8 -*-

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数

#居然没有想到翻转这一招，上网搜了才恍然大悟，唉。。。

#复杂版
def is_palindrome(n):
	str1=str(n)
	str2=str(n)[::-1]
	
	if len(str(n))==1:
		False
	else:
		return str1==str2

#简洁版 
def is_palindrome(n):
	if len(str(n))==1:
		False
	else:
		return int((str(n)[::-1]))==n

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
