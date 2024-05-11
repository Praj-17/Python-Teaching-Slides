string = "I like apples and do you like them too?"

#define all the vowels 

vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]

#method 1

count  = 0
for char in string:
    if char in vowels:
        count = count +1
print(count)


#Why you should look for inbuilt functionalitoes

#faster - It saves time
# The inbuilt function would be far more optmized and far  more tested, than you can write or test yourself.

