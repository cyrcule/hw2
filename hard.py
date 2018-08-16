# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
 
name_person1 = input('введите имя персонажа 1: ')
 
person1_dict = {'name': name_person1, 'health': 90, 'damage': 50}
 
name_person2 = input('введите имя персонажа 2: ')
 
person2_dict = {'name': name_person2, 'health': 100, 'damage': 30}
 
print(person1_dict)
print(person2_dict)
 
def attack(person1_dict, person2_dict):
    pers1 = dict(**person1_dict)
    pers2 = dict(**person2_dict)
    new_h = pers2.get('health') - pers1.get('damage')
    pers2.update({'health':new_h})
    return pers2
 
person2_dict = attack(person1_dict, person2_dict)
 
print(person1_dict)
print(person2_dict)
 
# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
 
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
 
import random, os
 
def open_file (name):
  SEP = ' - '
  with open(os.path.join('game', name + '.txt'), 'r', encoding='UTF-8') as f:
    charact = []
    for line in f:
        l_strip_split = line.strip('\n').split(SEP)
        charact.append(l_strip_split)
    return dict(charact)
 
name_person1 = input('введите имя персонажа 1: ')
 
person1_dict = open_file(name_person1)
 
name_person2 = input('введите имя персонажа 2: ')
 
person2_dict = open_file(name_person2)
 
print('изначальные характеристики перса 1: ', person1_dict)
print('изначальные характеристики перса 2: ', person2_dict)
 
def attack(person1_dict, person2_dict):
    pers1 = dict(**person1_dict)
    pers2 = dict(**person2_dict)
    new_h = float(pers2.get('health')) - float(pers1.get('damage')) / float(pers2.get('armor'))
    pers2.update({'health':new_h})
    return pers2
 
while True:
  r = random.randint(1,2)
  if r == 1:
    person2_dict = attack(person1_dict, person2_dict)
    if person2_dict.get('health') <= 0:
      print('Победил {}. Осталось здоровья {}.'.format(person1_dict.get('name'), person1_dict.get('health')))
      break
  else:
    person1_dict = attack(person2_dict, person1_dict)
    if person1_dict.get('health') <= 0:
      print('Победил {}. Осталось здоровья {}.'.format(person2_dict.get('name'), person2_dict.get('health')))
      break
