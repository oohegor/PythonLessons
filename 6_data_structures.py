# ---------- List ---------- #
# Это мой список покупок
shopList = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать ', len(shopList), 'покупок.')

print('Покупки:', end=' ')
for item in shopList:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shopList.append('рис')
print('Теперь мой список покупок таков:', shopList)

print('Отсортирую-ка я свой список')
shopList.sort()  # directly changes. not returns
print('Отсортированный список покупок выглядит так:', shopList)

print('Первое, что мне нужно купить, это', shopList[0])
oldItem = shopList[0]
del shopList[0]
print('Я купил', oldItem)
print('Теперь мой список покупок:', shopList)

# ---------- Cortege ---------- #
zoo = ('питон', 'слон', 'пингвин')  # помните, что скобки не обязательны
print('Количество животных в зоопарке -', len(zoo))
new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo) - 1 + len(new_zoo[2]))

# ---------- Dictionary ---------- #
# 'ab' - сокращение от 'a'ddress'b'ook
ab = {
    'Swaroop'   : 'swaroop@swaroopch.com',
    'Larry'     : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer'   : 'spammer@hotmail.com'
}
print("Адрес Swaroop'а:", ab['Swaroop'])
# Удаление пары ключ-значение
del ab['Spammer']
print('\nВ адресной книге {0} контактов\n'.format(len(ab)))
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))
# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

# ---------- Sequences ---------- #
shopList = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'
# Операция индексирования
print('Элемент 0 -', shopList[0])
print('Элемент 1 -', shopList[1])
print('Элемент 2 -', shopList[2])
print('Элемент 3 -', shopList[3])
print('Элемент -1 -', shopList[-1])
print('Элемент -2 -', shopList[-2])
print('Символ 0 -', name[0])
# Вырезка из списка
# Если первое число не указано, Python начнёт вырезку с начала последовательности.
# Если пропущено второе число,Python закончит вырезку у конца последовательности.
print('Элементы с 1 по 3:', shopList[1:3])
print('Элементы с 2 до конца:', shopList[2:])
print('Элементы с 1 по -1:', shopList[1:-1])
print('Элементы от начала до конца:', shopList[:])
# Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])

# ---------- Set ---------- #
bri = set(['Бразилия', 'Россия', 'Индия'])
print('Индия' in bri)
print('Usa' in bri)
bric = bri.copy()
bric.add('Китай')
print(bric.issuperset(bri))
bri.remove('Россия')
bri & bric      # OR bri.intersection(bric)

# ---------- Reference ---------- #
print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist    # mylist - лишь ещё одно имя, указывающее на тот же объект!
del shoplist[0]  # Я сделал первую покупку, поэтому удаляю её из списка
print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один объект.
print('Копирование при помощи полной вырезки')
mylist = shoplist[:]     # создаём копию путём полной вырезки
del mylist[0]    # удаляем первый элемент
print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что теперь списки разные

# ---------- String ---------- #
name = 'Swaroop'    # Это объект строки
print('Our string: ' + name)
if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')
if 'a' in name:
    print('Да, она содержит строку "a"')
if name.find('war') != -1:
    print('Да, она содержит строку "war"')
delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))
