#What is a palindrome

# it is a word or a string that reads the same in in reverse


#Examples of Palindrome
#MOM, MADAM , RADAR

string = "madamvsvavavfaqr "

charcter_split = list(string)
print(charcter_split)

index = 0
for char in reversed(charcter_split):
    if char == string[index]:
        print("it matches")
        index =index + 1

    else:
        print("It does not match")


if index == len(string):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
