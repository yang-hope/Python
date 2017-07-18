# -*- coding:utf-8 -*-

a = float(input('height:'))
b = float(input('weight:'))
bmi = b/(a**2)

if bmi<18.5:
	print('your BMI is %.1f' % bmi, '过轻')
elif 18.5 <= bmi < 25:
	print('your BMI is %.1f' % bmi, '正常')
elif 25 <= bmi < 28:
	print('your BMI is %.1f' % bmi, '过重')
elif 28 <= bmi < 32:
	print('your BMI is %.1f' % bmi, '肥胖')
else:
    print('严重肥胖')
