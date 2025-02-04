import pdb

def multiply(num_a, num_b):
    return num_a * num_b

def square(num):
    return multiply(num, num)

def power_n(num, power):

    if power == 0:
        return 1
    elif power == 1:
        return num
    
    # product = num
    # for _ in range(power - 1):
    #     product = multiply(num, product)
    # return product

# make list out of the number and power
# put first 2 digits into the multiply function
# change first digit to the multiple function result
# remove last digit
# run multiply function until only 2 digits remaining

    numbers = [num for i in range(power)]
    while len(numbers) > 1:
        result = multiply(numbers[0], numbers[1])
        numbers[0] = result
        numbers.pop(-1)

    return result

print(power_n(2,0))
print(power_n(2,1))
print(power_n(2,5))

# print(multiply(5, 3) == 15)  # True
# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True