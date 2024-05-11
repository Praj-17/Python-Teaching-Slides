fruits = ['apples', 'mangoes', 'bananas']

print(fruits) # ['apples', 'mangoes', 'bananas']
print(fruits[1]) #1 Output only Mangoes

# for fruit in fruits: # apples
#                      # manoges
#                      #bananas
#     # print(fruit)

#using string
string = "Hello this is python class 5"
# for char in string:
#     print(char)

#using If-else in loops

# #using Break
# for char in string:
#     if char == "y":
#         break
#     else:
#         print(char)

count = 0
for char in string:
    if char == "i":
        count = count +1
    else:
        continue
print(count)

#Break = When you would want a loop to stop at some given condition

#Continue  = When you would want a loop to skip doing something

# When you would write continue, The codeblock after the continue wont be executed

count = 0
for char in string: #chat is iterator and string is iterable
    if char == "i":
        count = count +1
    continue
    print(char) #Anything your write after continue wont be executed
print(count)


# Range Function

#The range function is used to create a range of numbers

first_50_numbers = list(range(51)) # the range function always excludes the upper limit of the range
print(first_50_numbers)

from_51_to_100 = list(range(51, 101)) # the default lower limit is 0
print(from_51_to_100)

#Reverse the same numbers


#create a range
# to convert it to a list
#to reverse that list
# TO convert the reversed list to a list again
reversed_numbers = list(reversed(from_51_to_100))

#method 2
#create a range
# to convert it to a list
#Build for loop that iterates and appends to it a new list

reversed_numbers = []
for i in reversed(from_51_to_100):
    reversed_numbers.append(i)
print(reversed_numbers)
    
for i in range(1, 10): #i is the iterator 
    print("THis is the number", i)
else:
    print("The foor loop is finished")

#Iterating over multiple iterables with multiple iterators

#iterables are those which are iterated - LIST, SET, Tuple, String, ramge
#Iterators are those variables which represent one element of that iteration

for i in range(1,10):
    for j in range(11,20):
        print(i, j)

#Pass statement - Pass is used as a placeholder! 

a = 11
if a == 10:
    print(a)
else:
    pass # The passs stament is used to avoid, The syntax error it says do not do anything and just move ahead