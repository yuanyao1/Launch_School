def multisum(num):
    multiples = [number for number in range(1, num + 1) if number % 3 == 0
                 or number % 5 == 0]
    total = sum(multiples)

    return total



# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)