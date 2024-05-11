year = 2025

#check if the year is perfectly divisible

mod_value = year%4

if mod_value == 0:
    print(f"The year {year} is a leap year")
else:
    print("It is not a leap year")