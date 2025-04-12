# apple = 'one'

# data = {
#     apple: 50,
#     "banana": 10,
#     "cherry": 'red',
#     }

# print(data)
# print(f'variable id = {id(data[apple])} with value {data[apple]}')
# print(f'variable id = {id(data['one'])} with value {data['one']}')

# print(min(data.values()))  # Output: 'apple' (min key by lexicographic order)
# print(max())  # Output: 'cherry' (max key by lexicographic order)

# set1 = {'dog', 1, [5, 4],}
# print(set1)

# def func1():
#     pass

# list1 = [1, 2]
# set1 = {'dog', 1, (5, 4),}
# print(set1.add('cat'))
# print(set1)
# print(set1.discard('dog'))
# print(set1)

# set2 = {'dog', 1, (2, [3, 4]),}
# print(set2)

# tup1 = (1, [2, 3])
# tup2 = (1, (2, 3))

# dict2 = {
#     'atlanta': 'hawks',
#     'boston': 'celtics',
# }

# frozenset1 = frozenset(set1)

# dict1 = {
#     'name': 'john',
#     True: 'smith',
#     range(2): 'turtle',
#     frozenset1: 'iceberg',
#     func1: 'lettuce',
#     None: 'nothing',
#     tup2: 'D',        # works since tuple contains hashable objects
#     # dict2: 'teams', # TypeError: unhashable type: dict
#     # list1: 'A',     # TypeError: unhashable type: list
#     # set1: 'B',      # TypeError: unhashable type: set
#     # tup1: 'C',      # TypeError: unhashable type: list in tuple
# }

# print(dict1)


# set1 = {'dog', 1, (5, 4),}
# frozen1 = frozenset(set1)           # frozenset({'dog', 1, (5, 4)})
# frozen2 = frozenset(['a', 'b'])     # frozenset({'b', 'a'})
# print(frozen1)
# print(frozen2)

# frozen3 = frozenset(['hawk', 'eagle', 50])  # frozenset({'eagle', 'hawk', 50})
# print(frozen3)

# frozen4 = frozenset(['hawk', 'eagle', 50, [100, 200]]) # TypeError: unhashable type: 'list'
# print(frozen4)

# frozen5 = frozenset(['a', 'b'], 'fish')

# list(['a', 'b'])
# tuple({'a', 'b'})
# # set('a', 'b')
# set4 = {'a', 'b'}
# set1 = {'dog', 1, (5, [1, 2]),}
# print(set1)
# dict()
# del data[apple]

# print(data)

# dict1 = {
#     'apple': 'Produce',
#     'carrot': 'Produce',
#     'pear': 'Produce',
#     'broccoli': 'Produce',
# }

# for blah in dict1:
#     print(blah)

# dict1['apple'] = 'Fruit'
# dict1['carrot'] = 'Vegetable'
# dict1['pear'] = 'Fruit'
# dict1['broccoli'] = 'Vegetable'

# print(dict1)


# list_of_pairs = [('hawk', 1), ('eagle', None), ('bat', True)]
# tuple_of_pairs = (('hawk', 1), ('eagle', None), ('bat', True))
# set_of_pairs = {('hawk', 1), ('eagle', None), ('bat', True)}
# print(dict(list_of_pairs))
# print(dict(tuple_of_pairs))
# print(dict(set_of_pairs))

# keys = ['hawk', 'dove']
# values = ['predator', 'prey']
# zipped_pairs = zip(keys, values)
# print(dict(zipped_pairs))

# set5 = set(frozenset(['honda', 'ford']))
# print(repr(set5))

# print(list(range(1, 6, -1)))


# dict1 = {
#     'apple': 'Produce',
#     'carrot': 'Produce',
#     'pear': 'Produce',
#     'broccoli': 'Produce',
# }
# set_a = {'fish', True, 2.5}
# for idx, element in enumerate(dict1.values()):
#     print(f'index: {idx}, element: {element}')


# list_a = [1, ['a', 'b'], 'dog', ['a', 'b']]
# print(list_a.count(['a', 'b']))     # 2
# print(list_a.index(['a', 'b']))   # 1

# dict1 = {
#     'apple': 'Produce',
#     'carrot': 'Produce',
#     'pear': 'Produce',
#     'broccoli': 'Produce',
# }

# print(dict1.setdefault('fish', 'mackerel'))
# print(dict1)
# print(dict1.popitem())
# print(dict1)

# teams = {
#     'Atlanta': 'Hawks',
#     'Boston': 'Celtics',
# }

# teams_other = {
#     'Atlanta': 'Falcons',
#     'Dallas': 'Mavericks',
# }

# merged_teams = teams | teams_other
# print(merged_teams)
# {'Atlanta': 'Falcons', 'Boston': 'Celtics', 'Dallas': 'Mavericks'}

# teams |= teams_other # same as teams.update(teams_other)
# print(teams)
# {'Atlanta': 'Falcons', 'Boston': 'Celtics', 'Dallas': 'Mavericks'}

# tup_a = (range(7), (2, 3), 1, 'dog', (2, 3), range(7), range(7), dict1, dict1)
# print(tup_a.count((2, 3)))   # 2
# print(tup_a.count(range(7))) # 3
# print(tup_a.index((2, 3)))   # 1
# print(tup_a.index(range(7))) # 0
# print(tup_a.count(dict1))
# print(tup_a.index(dict1))

# print(range(7).start)

# word = 'seven'
# print(id(word))
# print(id(word.replace('a', 'z')))

# string = "This is the first line.\nThis is still the first line.\nThis is the second line."
# cleaned_string = string.replace("\n", " ", 1)
# print(cleaned_string)

# sentence = """the quick brown
# fox jumped
#     over the log"""

# print(sentence)

# set1 = {'dog', 'cat'}
# frozen = frozenset(set1)
# lst = [1, 2]
# lst.extend(frozen)
# print(lst)
# print("*".join(set1))

# 'This is the first line. This is still the first line.\nThis is the second line.'

# set_a = {'fish', True, 2.5}
# del set_a['fish']
# print(set_a)

# a, b = [3, 5]
# a, b = range(2)
# a, b = {'dog', 'cat'}
# print(a)
# print(b)

# cities = {'Austin', 'Jackson', 'Denver', 'Houston'}
# cities_2 = {'Jackson', 'Houston', 'London'}
# cities_3 = {'Austin', 'Jackson', 'Denver', 'Houston', 'Jackson', 'London'}

# cities = {'Austin', 'Jackson', 'Denver', 'Houston'}
# cities_2 = {'Jackson', 'Houston', 'London'}
# cities_3 = {'Austin', 'London', 'Moscow'}

# print(cities.issubset(cities_2,cities_3))
# print(cities.update(cities_2, cities_3))
# print(cities.difference(cities_2,cities_3))
# print(cities.union(cities_2,cities_3))
# print(cities.intersection_update(cities_2))
# print(cities)

# tup1 = ('a', 'b')
# set1 = {'sky', 50}
# list1 = ['ground', 3.0]

# result_tup = (*tup1, *set1, *list1)    # ('a', 'b', 50, 'sky', 'ground', 3.0)
# result_set = {*tup1, *set1, *list1}    # {3.0, 'ground', 50, 'sky', 'a', 'b'}
# result_list = [*tup1, *set1, *list1]   # ['a', 'b', 50, 'sky', 'ground', 3.0]
# print(result_tup)
# print(result_set)
# print(result_list)


# print(cities.union(cities_2)) # {'Jackson', 'Denver', 'Houston', 'Austin'}
# print(cities) # no mutation

# print(cities | cities_2)  # {'Jackson', 'Denver', 'Houston', 'Austin'}
# print(cities) # no mutation

# print(cities.intersection(cities_2)) # {'Denver'}
# print(cities) # no mutation

# print(cities & cities_2) # {'Denver'}

# print(cities.difference(cities_2))  # {'Jackson', 'Austin'}
# print(cities - cities_2)            # {'Jackson', 'Austin'}
# print(cities_2 - cities)            # {'Houston'}

# print(cities.isdisjoint(cities_2))
# print(cities.discard('Jackson'))
# print(cities)

# def profile(**blah):
#     for key, value in blah.items():
#         print(f"{key}: {value}")

# profile(name="Srdjan",
#         age=38,
#         profession="software engineer")

# Output:
# name: Srdjan
# age: 38
# profession: software engineer

set1 = {'atlanta', 'boston'}
set2 = {'falcons', 'red sox'}
zip1 = zip(set1, set2)
print(dict(zip1))