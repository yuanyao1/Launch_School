# Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise

def odd(num):
    return abs(num) % 2 == 1


print(odd(0))
print(odd(1))
print(odd(2))
print(odd(-111))
print(odd(-212))