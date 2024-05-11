string = "Hello this is the assignment number 8"


#two methods to do this

output = string.title()
print(output)

#method 2

words = string.split(' ')
output = ""
for word in words:
    word.capitalize()
    output = output + " " + word 
print(output)