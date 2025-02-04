def twice(num):
    num_str = str(num)
    first_half = num_str[: len(num_str) // 2]
    second_half = num_str[(len(num_str) // 2):]
    num = num if first_half == second_half else num * 2
    
    return num

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True