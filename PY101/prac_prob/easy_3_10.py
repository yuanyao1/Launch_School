def century(year):
    cen = year // 100 if year % 100 == 0 else ((year // 100) + 1)
    cen = str(cen)

    if cen.endswith(('11', '12', '13')):
        return cen + 'th'
    elif cen.endswith('1'):
        return cen + 'st'
    elif cen.endswith('2'):
        return cen + 'nd'
    elif cen.endswith('3'):
        return cen + 'rd'
    
    return cen + 'th'

# print(century(100))     # 1st
# print(century(2000))    # == "20th"  
# print(century(2001))    # == "21st"  
# print(century(1965))    # == "20th"  
# print(century(256))     # == "3rd"    
# print(century(5))       # == "1st"      
# print(century(10103))   # == "102nd"
# print(century(1052))    # == "11th"  
# print(century(1127))    # == "12th"  
# print(century(11201))   # == "113th"

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True