name = input("Type your name here: ")
age = input("Type your age here: ")

print(f"Your name is {name} and your age is {age}")


#Whenenver you take an input, the input is bedefault a string

print(type(age))
print(type(name))

#How to convert it to other data types

print(f"You age after 10 years will {int(age) +10}")