lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_total(numbers):
    total = sum([num for num in numbers if num % 2 != 0])
    return total

print(odd_total([1, 6, 7]))

new_lst = sorted(lst, key=odd_total)
print(new_lst)