def factors(number):
    divisor = number
    result = []

    if number <= 0:
        return "Please give a positive number"
    
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

num_a = 10
num_b = 0

print(factors(num_a))

print(factors(num_b))