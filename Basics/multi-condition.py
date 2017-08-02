# -*- coding:utf-8 -*-

k = input('input the index of shape:')
if k == '1':
	print ('circle')
elif k == '2':
	print ('oval')
elif k == '3':
	sd1 = int(input('the first side:'))
	sd2 = int(input('the second sdie:'))
	if sd1 == sd2:
		print ('the square\'s area is: %d' % (sd1*sd2))
	else:
		print ('the rectangle\'s area is: %d' % (sd1*sd2))
elif k == '4':
	print ('triangle')
else:
	print ('you input the invalid number.')
