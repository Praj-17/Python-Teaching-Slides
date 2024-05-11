# While loop is very similar to for loop

#But it does not iterate an iterate, but it runs unit  a particular condition is met
# a = 0
# while a<=10:
#     print(a)


#NEVER EVER WRITE A WHILE LOOP WITHOUT A BREAK STATMENT OR AN ENDING CONDTION
a = 10
while a<10:
    if a == 5:
        break
    else:
        print(a)
else:
    print('a is no longer less than 10')


n = 50

for i in range(n):
    for i in range(0,i+1):
        print("*", end = "")
    print("")

