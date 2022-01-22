# numbers_count = int(input())
# sum = 0
# for i in range(numbers_count): # превратится в 0, 1, 2, 3
#     # sum = 0 bad
#     number = int(input())
#     sum += number
# print(sum)

# numbers_count = int(input())
# sum = 0
# for i in range(numbers_count): # превратится в 0, 1, 2, 3
#     # sum = 0 bad
#     number = int(input())
#     if number % 3 == 0:
#         sum += number
    
# print(sum)
    
# for i in 4:
#     print(...)
# 0 + 4 0 + 6 0 + 22 0 + 35

#? break continue

# numbers_count = int(input())
# sum = 0
# for _ in range(numbers_count): # превратится в 0, 1, 2, 3
#     # sum = 0 bad
#     number = int(input())
#     if number % 3 == 0:
#         # continue #! Прерывает текущую итерацию и вызывает следующую
#         # break #! Прерывает весь цикл
#         break
#     sum += number
    
# # print(sum)

# arr = [] # array - массив, 
# #? Корректнее list - список
# List is a sequence of elements with index access

# friend1 = 'Vasya'
# friend2 = 'Petya'

# friends = ['Vasya', 'Petya', 'Masha', 'Yulia', 'Katya']

#? массив = [элемент0, элемент1, ...]
#? Индексный доступ - массив[индекс] => i-ый элемент
# print(friends[3])
# print(len(friends)) # length / size of array => 5 


# for i in range(len(friends)): # range(5) = 0, 1, 2, 3, 4
#     print(friends[i])

# for friend in friends:
#     print(friend)

# shops = [101, 263, 300]
# count_of_numbers = len(shops)

# for i in range(count_of_numbers):
#     print(shops[i])        
    
# for shop in shops:
#     print(shop)

#! в Python строки иммутабельны (неизменяемые)
# arr = []
# str_input = input()
# numbers = str_input.split(' ') # => '5 7 2'
# # arr.append()
# # print(arr)
# print(str_input)
# print(numbers)

# string.split(string)
# Получает массив из строки по разделителю
#! строка.split(разделитель) => массив из разделенных элементов (строк)

# string.join(array)
# Создает строку из массива
#! соединитель.join(массив) => строка с соединенными элементами (массив столько строк)

# sdfg = ' . '
# sdfg

# print(' -> '.join(numbers))

# array.append(element)

# List comprehension
# [elem for ...]


# num = int(input()) # => 10
# arr = []

# for i in range(num):
#     arr.append(i)
    
# print(arr)   

# print([i**2 for i in range(num)])

# def name_function(arg1, arg2, arg3, ... argN):
#     return something....


# def y(x):
#     x = 100
#     print('[y] x = %d' % x)
#     return x**2

# num = int(input())
# print(y(num))

# x = int(input()) => 60
# print(y(x)) #! передается копия, поэтому x не изменится
# print('[main] x = %d' % x)


# def add(arr, elem):
#     arr.append(elem)
#     print('[add]')
#     print(arr)

# num = int(input())
# print(y(num))

# arr = [1, 2, 3, 4]
# add(arr, 5)
# print('[main]')
# print(arr)
    
#! passing parameters by reference по ссылке (передаются сами реальные значения)
#! passing parameters by value по значению (передаются копии)

#! Простые типы передаются по значению (int, string, float...)
#! Остальные передаются по ссылке (array)

#?
#!
#TODO:
#* .....


# Функции

# def name_function(arg1, arg2, arg3, ... argN):
#     return something....

#! default arguments must be located at the end of the list of args

# def func(arg1='1', arg2='2', arg3='default'): # default arguments
# def func(arg1, arg2, arg3='default'): # default arguments
#     print('1', arg1)
#     print('2', arg2)
#     print('3', arg3)
    
# func('1234')
# func(arg1='zhopa', arg2='negra', arg3='black') # => black
# func(arg1='zhopa', arg2='negra') # => default

    
# func('zhopa', 'negra', 'black')
    
    
# func(arg1='zhopa', arg2='negra', arg3='black')
# func(arg2='zhopa', arg3='negra', arg1='black')

# def sorted(arr, reverse=False)


# numbers = [5, 2, 6, 0, 0, -9, 4, -11]
# print(numbers)
# print(sorted(numbers)) # sorting in ascending order
# # print(sorted(numbers, reverse=False)) # sorting in ascending order

# print(sorted(numbers, reverse=True)) # sorting in descendindg order

# Calculates a square of the number
# def y(x):
#     return x**2

# print(3)
# ascending order - по возрастанию
# descendindg order - по убыванию
#? do not understand what's wrong
#?list = [int(i) for i in input().split()]
#?sum = 0
#?for i in range(1, len(list)):
 #?   if list[i] > list[i - 1] and list[i] > list[i + 1]:
  #?      sum += 1
#?print(list[i])

#line = [int(i) for i in input().split()]
#print(max(line), line.index(max(line)))

#str = input()
#print(str[:-2])
#print(str[3])
#print(str[-2])
#print(str[::2])

#sentence = input()
#space = sentence.find(' ')
#first_part_sentence = sentence[0:space]
#second_part_sentence = sentence[space:]
#print(second_part_sentence + ' ' + first_part_sentence)

#string = 'Собака'


# for symbol in string:
#   print(symbol)
# array = [string[i] for i in range(len(string)) if i % 3 != 0]
# # ['c', 'о', 'б']

# print(''.join(array))

# array = [string[i] for i in range(len(string)) if i % 3 != 0]
# ['c', 'о', 'б']

#print(''.join([string[i] for i in range(len(string)) if i % 3 != 0]))

# for i in range(n: int): => n раз

# elements = [5, 2, 6, 7, 3] => 5 (n)
# for element in elements:

# while условие: # (прервется, когда условие станет ложным)
#   действие
  
  
# i = 0
# while i < 10:
#   i += 1
  
# print(i)

# N = int(input())
# pow = 0
# result = 1
# while result <= N:
#   pow += 1
#   result *= 2
# pow -= 1

#! for - счетный цикл
#! должно быть известно количество повторений

#! while - пока не ....
#! Мы не знаем, сколько повторений будет

# def get_pow(num, pow):
  # 2 ** n = 2 * 2 * 2 * 2
  # num ** pow = num * num * num * num
  # result = 1
  # for _ in range(pow):
  #   result *= num
    
  # return result       
  # for i in range(5):
  
  # for i in 0, 1, 2, 3, 4
          
      
      
      
# print(get_pow(2, 5))
# print(get_pow(3, 4))

# get_pow(2, 5) + get_pow(2, 6)

# sum = 0
# for i in range(1, 10): # => 1, 2, 3, 4, 5, 6, 7, 8, 9:
#   sum += get_pow(2, i)  
  
# print(sum)
 
# buildings = [1, 2, 3, 4]
# for build in buildings
  
          
# get_pow(2, 5) 
          
# N = int(input())
# pow = 0
# while (get_pow(2, pow) <= N):
#   pow += 1
# pow -= 1

# (a + b) * (a - b)

# def sum(a, b):
#   return a + b

# def sub(a, b):
#   return a - b

# def mul(a, b):
#   return a * b

# add(a, b) => c
# sub(a, b) => d
# mul(c, d) => result

#! Декомпозиция
# def open_door():
#   print('take key')
#   print('go to the door')
#   print('insert the key to the lock')
#   print('turn the key anti-clockwise')
#   print('push the door')


# print('....')

# print('bio finger')
# print('go to the door')
# print('insert the key to the lock')
# print('turn the key anti-clockwise')
# print('push the door')

# print('....')

# print('take key')
# print('go to the door')
# print('insert the key to the lock')
# print('turn the key anti-clockwise')
# print('push the door')

# print('take key')
# print('go to the door')
# print('insert the key to the lock')
# print('turn the key anti-clockwise')
# print('push the door')

# print('take key')
# print('go to the door')
# print('insert the key to the lock')
# print('turn the key anti-clockwise')
# print('push the door')

# print('take key')
# print('go to the door')
# print('insert the key to the lock')
# print('turn the key anti-clockwise')
# print('push the door')

# open_door()

# open_door()

# open_door()

# open_door()

#* 1. import door
# доступ: door.функция() или door.переменная
# door.open_door(key, door)

# import door

# your_door = 'DOOR1'
# key = door.take_key()
# print('taken the key')

# door.open_door(key, your_door)

#* 2. from door import *
# доступ: door.функция() или door.переменная

# from door import *
# from door import take_key, open_door
# import door as dr
# dr.open_door()

#your_door = 'DOOR1'
#key = take_key()
#print('taken the key')

#open_door(key, your_door)

#list = [int(i) for i in input().split()]
#count = 0
#for i in range(len(list)):
#  for f in range(i + 1, len(list)):
#    if list[i] == list[f]:
#      count += 1
#print(count)


#! List (array)
# array = [1, 2, 3, 4] # list []
# array[2] = 25 => [1, 2, 25, 4]

# array[-1] => 4
# array[len(array)-1] => 4

# print(array[2]) => '3'

# array = [
#   1,
#   2,
#   3,
#   4, #? ',' после последнего элемента тоже нужна
# ]

#! Tuple (кортеж)
# tuple = (1, 2, 3, 4) # - immutable #! НЕЛЬЗЯ ИЗМЕНЯТЬ
# print(tuple[2])
# tuple[2] = 25 #! ЗАПРЕЩЕНО

# def foo():
#   return 5, 4 # => (5, 4)

# a, b = foo() => (5, 4)

# a = 5
# b = 4
# a, b = (b, a)
# a, b = b, a
# print(a, b)
# tuple = (5, 4, 2)
# tuple[2] = 5

# c = a
# a = b
# b = c

#! Set (множество)
# numbers = {1, 2, 3, 4, 5, 5, 1, 6, 8}
# numbers = set()  = {}
# print(numbers)

# arr = [1, 2, 3, 4, 5, 5, 1, 6, 8]
# print(list(set(arr)))

# numbers = {8, 1, 2, 3, 4, 5, 5, 1, 6, 8}
# # print(numbers[0])
# for number in numbers:
#   print(number)

# sports = {34, 25, 11, 9}
# english = {25, 9, 48, 15}
# print(sports.intersection(english)) # Группа из спортсменов-англичан
# print(sports.union(english)) # Все спортсмены и англичане
# print(sports.difference(english)) # Все спортсмены, не являющиеся англичанами
# sports.add(30)
# print(sports)

# print(' '.join(list(set('3 5 4 6 2 7 8 6 0'.split(' ')))))

# set = set(input().split(' '))
# list_of_unique = list(set)
# unique_string = ' '.join(list_of_unique)
# print(unique_string)

#! Dict - dictionary - словарь
# dictionary = dict()
# {
#   'key': value,
#   'key2': value2,
#   'key3': value3,
#   ...
# }

#address_book = {
 # 'Avi': '054233456',
  #'Igor': '8911000000',
  #'Yaniv': '065444220',
#}

# print(address_book['Avi'])

# name = input()
# number = input()
# address_book[name] = number

# dict.items() => [
#   ('Avi', '054233456'),
#   ('Igor', '8911000000'),
# ]

# for name, number in address_book.items():
#   print('name: %s, number: %s' % (name, number))
  
# print(address_book['VASYA'])
# print(address_book.get('VASYA'))

# address_book['VASYA'] = '7876765678'
# number = address_book.get('VASYA')
# if number:
#   print(number)
# else:
#   print('Not found')

# len(arr) => длина
# .count(n) => кол-во элементов n
# .find/rfind - находит индекс первого/последнего вхождения
# .index() - 
# .replace() - замена
# .append(elem) - добавление в конец
# .pop(elem) - удаление последнего элемента и возврат его

# def sum(a, b):
#   return a + b

# print(sum(4, 6))
# print(sum)

# # a = 5
# # a = 'r'
# # a = Card(...)
# a = sum
# print(a(4, 6))

#def order_run():
#  print('Я пробежал')
  
#def order_eat():
#  print('Я покушал')
  
#def order(action):
#  print('Выполняю приказ...')
#  action() # <=> ass()
  
  
  
  
#def ass():
#  print('Я посрал')
  
#order(action=ass)




# class Musician:
#     def play():
#         pass
        
# # Musician()

# class Pianist(Musician):
#     def play():
#         pass
#         # keyboard
        
# class Violinist(Musician):
#     def play():
#         pass
#         # violin

# def foo():
#     return '123'

# def foo2():
#     return '456'

# print(foo)
# print(foo())

# func = foo
# print(func())

# func = foo2
# print(func())

# func = lambda: '789'
# print(func())

# class LastNamePlayer(Player):
#     def __init__(self, name, last_name, cards: List[Card] = None):
#         super().__init__(name, cards)
#         self.last_name = last_name


# people = [
#     {
#         'name': 'Vasya',
#         'salary': 50000,
#     },
#     {
#         'name': 'Petya',
#         'salary': 100000,
#     },
#     {
#         'name': 'Valeriy',
#         'salary': 502000,
#     },
#     {
#         'name': 'Polina',
#         'salary': 30000,
#     },
# ]

# def sort(person):
#     return name of person

# people.sort(key=lambda person: (person['name'], person['salary']))
# print(people)

# s = 'a '
# split_s = s.split(' ')
# print(split_s)
# print(len(split_s[-1]))