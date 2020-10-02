
# ---------- Command Flow ---------- #

# if
number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Поздравляю, вы угадали,')    # New block starts here
    print('(хотя и не выиграли никакого приза!)')   # New block finished here
elif guess < number:
    print('Нет, загаданное число немного больше этого.')    # + one block
    # you can do everything into this block
else:
    print('Нет, загаданное число немного меньше этого.')
    # guess > number

print('Завершено')  # program's main block

# while
number = 23
running = True

while running:
    guess = int(input('Введите целое число (или сразу 23): '))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False  # stop while
    elif guess < number:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:   # remember "while" has "else"
    print('Цикл while закончен.')

print('Завершение while.')    # program's main block

# for
for i in range(1, 6, 2):   # range(1,5) from 1 to 5 [1,2,3,4]   # range(1,5,2) step 2 [1,3]
    print(i)
else:
    print('Цикл for закончен')

# if you want get array use list(range(1,5))

# break
while True:
    s = input('Input some :')
    if s == 'exit':
        break
    print('String size :', len(s))
print('End "break"')

# continue
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины')
    # Разные другие действия здесь..
