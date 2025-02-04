ADOPTION = {
    'Spain': 1582,
    'Portugal': 1582,
    'Prussia': 1610,
    'Great Britain': 1752,
    'Japan': 1873,
    'Saudi Arabia': 2016,
}

COUNTRIES = ADOPTION.keys()

def prompt(msg):
    print(f'>== {msg}')

def is_leap_year(num):
    if num < adoption_year and num % 4 == 0:
        return True
    elif num % 400 == 0:
        return True
    elif num % 4 == 0 and num % 100 != 0:
        return True
    
    return False

def select_country(countries):
    prompt('Please select one of the below countries:')
    for country in countries:
        prompt(country)
    
    user_country = input()
    while user_country not in countries:
        prompt('Invalid selection. Try again:')
        user_country = input()
    
    return user_country

adoption_year = ADOPTION[select_country(COUNTRIES)]
print(adoption_year)


print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)