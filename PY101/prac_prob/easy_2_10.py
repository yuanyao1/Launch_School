import datetime

def prompt(message):
    print(f"==> {message}")

prompt("What is your age?")
age = int(input())

prompt("At what age would you like to retire?")
retirement_age = int(input())

work_years = retirement_age - age
year = datetime.date.today().year

print(f"It's {year}. You will retire in {year + work_years}")
print(f"You have only {work_years} years of work to go!")