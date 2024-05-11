

a = 10

#Equals to 
if a == 10:
    print("a is equal to  10")
else:
    print("It is not ")
#Not equal to 
a = 12

if a != 10:
    print("a is not equal to  10")
else:
    print("It is not ")

#Greater than
a = 10
if a >10:
    print("a is greter than   10")
else:
    print("It is not ")
#Greater than or equal to 
a = 10
if a >=10:
    print("a is greter than   10")
else:
    print("It is not ")
#less
a = 10
if a <10:
    print("a is greter than   10")
else:
    print("It is not ")
#less
a = 10
if a <=10:
    print("a is greter than   10")
else:
    print("It is not ")




#Elif

b = 45

if b == 10:
    print("b is 10")
elif b <= 15:
    print("b is 15")
elif b >50:
    print("b is greater than 50")
elif b < 40:
    print("b is less than 40")
else:
    print("b does not satisfy any of the above condition")



#Clubbing Ifs and elifs together

if a ==10 and b >20:
    print("a is 10 and b is greater than 20")
else:
    print("not satisfied")

if a ==10 and b >20 and b>30 and a <=30  : # you can add multiple conditions here
    print("a is 10 and b is greater than 20")
else:
    print("not satisfied")

if a == 10 or b >100 or b <10:
    print("The condition is satisfied")
else:
    print("no condition satiesfied")



#NEsted Ifs

if a>=10:
    if a<5:
        print("a is less than 5 and also a is less than 10")
    
    elif a ==5:
        print("a is 5")
    else:
        print('a is not less than 5 but less than 10')
else:
    print("a is greater than or equal to 10")