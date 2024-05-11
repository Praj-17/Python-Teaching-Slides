#Factorial is multiplication of all numbers starting from 1 to that number

# 5! is given by 5*4*3*2*1

#Range function

#The range function gets all the numbers starting from 1 to the given number


#range(1, 6) - 1,2,3,4,5
n = 10
factorial = 1
for num in range(1, n+1):
    factorial = factorial *num
print(factorial)    
