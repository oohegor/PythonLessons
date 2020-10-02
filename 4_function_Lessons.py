
# ---------- Function ---------- #


def sayHello():
    print('Привет, Мир!')   # блок, принадлежащий функции
# Конец функции


sayHello()  # вызов функции
sayHello()  # ещё один вызов функции


# parameters and area of visibility
def func_outer(y):
    # we could set 'x' param name, but its shadow variable
    # func_outer(x): !!!
    # You can access global variable inside your function,
    # BUT for now, which is which? the parameter or the global variable? Confused, huh?

    global x    # need declare before use 'x = 20'
    print('y is param func_outer and y = ', y)
    print('y = {0}, func_outer see x = {1}' .format(y, x))     # you can see global x everywhere in program
    x = 20      # if 'global x' didnt set then we set new local variable

    def func_inner():
        nonlocal y
        y = 5
        print('func_inner see x = ', x)

    func_inner()
    print('Локальное y сменилось на из-за func_inner \'nonlocal\' ', y)


x = 50
print('its global x =', x)
func_outer(x)
print('Global y сменилось на ', x)


# optional parameters
def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)


# dynamic parameters and 'return'
def total(initial=5, *numbers, **keywords):     # if total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]      # or keywords.values()
    return count        # return value
# if function doesnt have return, it has -> return None


def someFunction():
    '''In someFunction(is empty function)
    
    'pass' - denotes as an empty block.'''        # this is documentation string
    pass


print(total(10, 1, 2, 3, vegetables=50, fruits=100))        # then total(10, 1, 2, 3, extra_number=12)
print(someFunction())       # return None
print(someFunction.__doc__)
