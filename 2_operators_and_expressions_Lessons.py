
# ---------- Operators ---------- #
# + 3+5 = 9, 'a' + 'b' = 'ab'
# - -5.2 = 0-5.2, 50 -24 = 26
# 2*3 = 6, 'la' *3 = 'lalala'
# 2 ** 4 = 16 (2*2*2*2)
# 4/3 = 1.3333
# 4//3 = 1
# 8%3 = 2
# 2 << 2 = 8 (10 => 1000)
# 11 >> 1 = 5 (1011 => 101)
# 5 & 3 = 1
# 5 | 3 = 7
# 5 ^ 3 = 6
# ~5 = -6 (invert all bits)

# 3 < 5 => true
# 3 > 5 => true
# 3 >= 5 => false
# 3 <= 5 => true
# 3 == 5 => true  ('str' == 'stR' => false)
# 2 !- 3 => true
# x=true not x => false
# true and false => false
# true or false => true

# a short record
a = 2
a *= 3  # a = a * 3


# operator priority (power from down to up)
# lambda
# or
# and
# not x
# in , not in
# is , is not
# < , <= , > , >= , != , ==
# |
# ^
# &
# << , >>
# + , -
# * , / , // , %
# +x , -x
# ~x
# **
# x.attribute
# x[index]
# x[index1:index2]
# f(arguments ...)
# (expressions, ...)
# [expressions, ...]
# {key:data, ...}

# 2 + ( 3 * 4 ) better then 2+3*4

length = a
breadth = 2

area = length * breadth
print('Square =', area)
print('Perimeter =', 2 * (length + breadth))



