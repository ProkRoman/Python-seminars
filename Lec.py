# Типы данных справедливы int, float, boolean, str
# list и др.
# Python – язык с динамической типизацией
# value = 2809
# name = 'Sergey'

# a = 123
# b = 1.23

# # print(type(a))
# # print(type(b))

# s ='hello'

# print(s)
# print(a, '-', b, '-', s)
# print('{2} - {1} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = [1, '2', 3, True]
# print(list)



# Ввод и вывод данных
# print() – отвечает за вывод данных input() – отвечает за ввод данных


# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a,b,))
# print(f'{a} {b}')


# print('Введите а')
# a = int(input()) # float
# print('Введите b')
# b = int(input()) # float
# print(a, ' + ', b, ' = ', a+b)
# # print('{} {}'.format(a,b,))
# print(f'{a} {b}')


# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной программы
# Если помните математику – проблем не будет
# +,-,*,/,%,//,**
# Приоритет операций **,⊕,⊖,*,/,//,%,+,-
# ( ) Скобки меняют приоритет
# Арифметические операции
#  exp1 = 2**3 - 10 % 5 + 2*3
#  exp2 = 2**3 - 10 / 5 + 2*3
#  print(exp1)  # 14.0 или 14
#  print(exp2)  # 12.0 или 12

# a = 1.3345
# b = 3
# c = round(a * b, 3)
# print(c)
  
# a =3
# a += 5

# print(a)

# a = 1 < 4 and 5 < 8
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# func = 1
# T = 4
# X = 2

# print(func<T>(X))

f = [1,2,3,4]
# print(f)
# print(2 in f)

is_odd = f[0] % 2 == 0
print(is_odd)