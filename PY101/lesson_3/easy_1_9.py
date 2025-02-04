advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

advice_list = advice.split()
index = advice_list.index("house")
print(" ".join(advice_list[:index]))