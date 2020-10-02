
# ---------- Comments ---------- #
# with slash -- "#"


# ---------- Numbers ---------- #
# int , float, complex
# 2, 123123123123123123123123, 3
# 52.3E-4 = 52.3 * pow(10,-4)
# (-5+4j) and (2.3 - 4.6j)

# ---------- Strings ---------- #
# "asd"
# 'asd'
#
# '''
# asd asd
# asd
# '''
# if ->  'What\'s'  'your name?'  = 'What's your name?'  (automatic concatenation)

# The method format
age = 21
name = 'Egor'

print('{0} has {1} age old.' .format(name, age))
print('{} == work too' .format(age))
# float (.) with an accuracy of 3 signs
print('{0:.3}'.format(1/3))
# fill underline (_) from center (^) with width 11
print('{0:_^11}'.format('hello egor'))
# by keywords
print('{name} has written {book}'.format(name='Swaroop', book='A Byte of Python'))
# {}
print("My name is {0} :-{{yeeees}}".format('Egor'))


# ---------- Variables ---------- #
# i, __my_name, name_23, a1b2_c3 and etc.           - is good
# 2things, my-name, >a1b2_c3, "this is into quotes" - isn't good

# all are objects -> "string", 3, and etc.

# i = 5
# print(i)  <==> i = 5; print(i)  ( we can, but why?:) )
print\
    ('\'\\\' - is power, but her s nim')  # <==> print('')

# indents for blocks
# i = 5
#  print('Значение составляет ', i) # Ошибка! Пробел в начале строки
# print('Я повторяю, значение составляет ', i)
