# S = 'spam'
# d = {}
# for (offset, item) in enumerate(S):
#     print(item, 'at offset', offset)
#     d[offset] = item
#
# s = 'qwekirjio'
# s
# srtd = sorted(s)
# srtd = ''.join(srtd)
# srtd
# 'e' in srtd
#
# l = []
# for i in range(5):
#     l.append(i)
# l
#
# l1 = [i for i in range(5) if i % 2]
# l1
#
# d1 = {i: i + 1 for i in range(10)}
# d1
#
# gen = [i for i in range(0, 101, 10)]
# gen
# min(gen)
# max(gen)
# len(gen)
#
# gen2 = gen[:]
# gen2
#
# L1 = [1, 2, 3, 4]
# L2 = [5, 6, 7, 8]
# new_L = zip(L1, L2)
# list(new_L)
# dict(zip(L1, L2))
#
# for x, y in zip(L1, L2):
#     print(x, '+', y, '=', x + y)
#
# L = [True, None]
# any(L)
# all(L)
#
# i = range(10)
#
#
# def gen_list(arg1: int, arg2: int) -> list:
#     gen = [i for i in range(arg1, arg2, 10)]
#     return gen
#
#
# gen_list(0, 100)
#
#
# def num(a, b, *args, **kwargs):
#     print(a, b, args, kwargs)
#
#
# num(1, 2)
# num(1, 2, 3, 4, 5, val=1)
#
# lambda x, y: x + y + 1
# noname_funk = lambda x: x + 1
# noname_funk(2)
#
# na = lambda x, y: x + y + 1
# na(2, 2)
#
# new_list = [(1, 3), (2, 2), (3, 1)]
# print(sorted(new_list, key=lambda i: i[0]))
#
# from functools import lru_cache
#
#
# @lru_cache
# def cash(i):
#     print(f'-{i}-')
#
#
# cash(1)
# cash(2)
# cash(1)
#
#
# def t_cash(i):
#     print(f'-{i}-')
#
#
# t_cash(1)
#
# """
# Создвние списка
# """
# lst = [1, 'sdf', (1, 2)]
# lst_gen = list(i for i in range(10))
#
# """Создание словаря + генератор"""
#
# dic = {0: 'Tol', 1: 'Anna', 2: 'Bogdan', 3: 'Artem'}
# dic[1]
# dic_gen = {i: i + 1 for i in range(0, 3)}
# dic_gen
#
# """Создание множества"""
# new_set = {1, 2, 3, 2}
#
# lst[0]
#
# list_for_if = [i for i in range(0, 0, 10)]
# if len(list_for_if) > 10:
#     print(f'Длина списка {len(list_for_if)}')
# elif 2 < len(list_for_if) <= 5:
#     print(f'Длина списка меньше либо равно 5.')
# elif len(list_for_if) <= 2:
#     print(f'Длина списка меньше либо равно 2.')
# else:
#     print(f"Странность. Длина списка = {len(list_for_if)}")
#
# s = 10
# a = True
# while a == True:
#     s -= 1
#     print(f's = {s}')
#     if s == 0:
#         a = False
#
# L = [i for i in range(0, 3)]
# print(L)
# for i in L:
#     print(i)
#
# print(lambda i: range(0, 5))
# print(list(range(0, 5)))
#
# str = 'tst'
# result = 'e' in str
# if result:
#     print('PASS')
# else:
#     print('NOT PASS')
#
# print(1, 2, 3)
#
# print(1, 2, 3, sep='-', end='\n')
#
# print()
#
# user_name = input('Enter your name:')
# print(f'Your name is {user_name}')
#
# with open('1.txt', 'a') as file_name:
#     file_name.writelines('Start write \n')
# with open('1.txt', 'r') as file_name:
#     file_name.read()
#     print(file_name)
#
# f = open('1.txt')
# f.read()
# f.readlines()
# print(f)
# f.close()
#
# for line in open('1.txt'):
#     print(line.strip())
#
# d = [1, 2, 3]
# print(21, *d)
#
# список = [1, 2, 3, 4]
# print(список)
#
# test = lambda x, y: x + y + 1
# test(2, 2)
#
# test_list = [(1, 3), (2, 2), (3, 1)]
# print(sorted(test_list, key=lambda i: i[0]))
#
#
# class Human:
#
#     def __init__(self, age, sex, name):
#         self.age = age + 1
#         self.sex = sex
#         self.name = name
#
#     def hum_info(self):
#         print(f'Human name - {self.name}, age - {self.age}, sex - {self.sex}')
#
# h1 = Human(age = 36, sex='male', name='Tol')
# h1.hum_info()
#
# class Sporsman(Human):
#
#     def __init__(self, age, sex, name, sport ):
#         self.sport = sport
#         super().__init__(age, sex, name)
#         print(super())
#
#     def hum_info(self):
#         #super().hum_info()
#         print(f'Human name - {self.name}, age - {self.age}, sex - {self.sex}, sport - {self.sport}')
#
# s1 = Sporsman(age = 36, sex='male', name='Tol', sport='Box')
# s1.hum_info()
# h1.hum_info()
#
#
#
# assert 3>2, 'Test norm'
#
#
# def test_integers(a,b):
#     assert a>b, 'Error a < b'
#
# def test_suit():
#     try:
#         test_integers(3,2)
#         test_integers(4,3)
#     except AssertionError as g:
#         print(f'Tests failed {g}')
#     else:
#         print('Tests passed.')
#
# test_suit()
#
#
# """Идиоматика Питона"""
# #поиск подстроки в строке
# name = 'Anatoliy Kravchenko'
# if 'AnatoliyQ' in name:
#     print('This name has an Hammand in it!')
# else:
#     print('Found errros')
#
# 1 in [1,2,3]
#
# ##########################
# chars = ['Hello', 'Word']
# ' '.join(chars)
# ############################
# names = ['Tol', 'Art', 'Anna', 'Bogdan']
# for i, name in enumerate(names):
#     print(i, name)
# ###########################
# with open('2.txt', 'w') as f:
#     names = ['Tol', 'Art', 'Anna', 'Bogdan']
#     dic = {}
#     x = 0
#     for i, name in enumerate(names):
#         print(i, name)
#         dic[i] = name
#         f.writelines(dic[x])
#         x += 1
#     print(dic)
#
# ##############обращение к словарю
# d = {'a':1, 'b':2}
# d.get('a')
# d.get('c')
# d['c']
# d.setdefault('f', 4)    #если нет ключа то добавляет
#
#
# #################sort
# l = [1,3,5,7,3,2]
# l.sort()
# new_l = sorted(l)
# print(l)
# print(new_l)
#
# l = [(1,3), (2,2), (3,1)]
# l.sort(key=lambda x: x[1])
# l.reverse()
#
#
# """Пользывательские типы данных"""
# import collections
# #collections.nametuple
#
# Point = collections.namedtuple('Point', ['x', 'y'])
# p1 = Point(1, 2)
# p2 = Point(x=3, y=5)
# z = p1.x + p2.x
# z
#
# ############counter
#
# c = collections.Counter('asdasdasd')   ###Counter({'a': 3, 's': 3, 'd': 3})
#
#
# ###########defaultdict
# from collections import defaultdict
# sentense = 'Hello! My name is Anatolii. I am from Ukraine. Now i live in' \
#            'Poland. I am 36 years old. I very need this work.'
# words = sentense.split(' ')   ###разбивка по словам
# d = defaultdict(int)
# for word in words:
#     d[word] += 1
# print(d)
#
#
# def trace(func):
#     def inner(*args, **kwargs):
#         print(func.__name__, args, kwargs)
#         return func(*args, **kwargs)
#     return inner
#
# @trace
# def foo(x):
#     return x
#
#
# foo(1)
#

import pytest


def func_for_test(x, y):
    return x + y


def test_func_pos():
    assert func_for_test(1, 1) == 2


def test_func_neg():
    assert func_for_test(1, 1) != 3


def test_suit():
    test_func_pos()
    test_func_neg()


@pytest.mark.parametrize(
    'x,y', [(1, 1), (2, 1), (3, 1)]
)
def test_add(x, y):
    assert x + y < 4


@pytest.mark.skip(reason='Outdate')
def test_skipp():
    assert 1 == 1




def decor_test_func(func):
    def inner():
        print("Test func wrapper start")
        func()
        print("Test func wrapper stop")
    return inner

@decor_test_func
def print_hello():
    return print('Hello Word')

decor_test_func(print_hello())


import requests


@pytest.fixture
def fact_url():
    return 'https://google.com'


@pytest.mark.smoke
def test_smoke(fact_url):
    reply = requests.get(fact_url)
    # assert reply.status_code == requests.codes.ok
    assert reply.status_code == 200


def fun_wrapper(func):
    def inner():
        print('Start')
        func()
        print('Stop')
    return inner

@fun_wrapper
def print_text():
    print('Printing text')

print_text()


def cycle(cycle = 5):
    x = 10
    while cycle > 0:
        print(x)
        x -=1
        if x == 0:
            x = 10
            cycle -= 1

cycle()

new_str = 'qwerty'
ch_str = new_str[::-1]
print(ch_str)

ch_str_new = ''.join(reversed(new_str))
print(ch_str_new)


lst = [1,2,3,4,4,(1,2,3), 'wer', 5]
lst_str = str(lst)
type(lst_str)
type(lst)
lst_tuple = tuple(lst)
type(lst_tuple)
lst_set = set(lst)
type(lst_set)
lst_dic = dict(lst)

i = iter(lst)
b = dict(zip(i, i))

l1 = [1,2,3]
l2 = [3,2,1]
new_dic = dict(zip(l1,l2))
print(new_dic)


stroka = ['Hello', 'word', '!']

#new_stroka = ' '.join(stoka)

def wrapper(func):
    def inner(stroka):
        print('Start join.')
        func(stroka)
        print('Stop join.')
    return inner

@wrapper
def func_join(stroka):
    full_str = ' '.join(stroka)
    return print(full_str)

func_join(stroka)







def param_transfer(fn):
    def wrapper(arg):
        print('Run func: ' + str(fn.__name__) + '(), with param: ' + str(arg))
        fn(arg)
    return wrapper

@param_transfer
def print_sum(num):
    num = num + 100
    print(num)

print_sum(4)



for i in range(0,5):
    print(i)

gen = (i for i in range(0, 6))
for i in gen:
    print(i)

def simple_gen(val):
    while val > 0:
        val -= 1
        yield val   #--------pause in work generator
gen_iters = simple_gen(5)
print(next(gen_iters))

while True:
    print('Endless cycle')

for i in range(11):
    #print(i)
    if i == 12:
        print(f'Cycle is break. i = {i}')
        break
    print(i)
else:
    print('Work else')



"""Create gegerator"""

def gen(val):
    while val > 0:
        val -= 1
        yield val

gen_iters = gen(5)

print(next(gen_iters))

g = (i for i in range(0, 11))
for i in g:
    print(i)


for i in range(0, 5):
    print(i)








