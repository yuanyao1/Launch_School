import copy

my_list1 = [{"first": 'value1'}, {"second": "value2"}, 3, 4, 5]
my_list2 = copy.copy(my_list1)
my_list2[3] = 'dog'
print(my_list1)