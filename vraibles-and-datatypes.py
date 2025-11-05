#------------------- Display on screen--------------------
from tkinter import Variable


print("hello world")
print('waqas ahmed')

# single line print
print("hello world",'waqas ahmed')

# numbers print
print(26)

# math use in numbers
print(15+10)

# variable --------> jis ki value change hosaktu hai!

# Variable name = value
print('waqas ahmed')

# updating Variable
name = "muhammad umer"
print(name)

# string value of variable
my_name = 'waqas ahmed'
print(my_name)
# hum " " ky darmiyan koi chez likh kr print kren gy to wo as it is print hogi!
# print("name")

# numaric value of variable -------> ye whole number hota hai!
age = 32
print(age)

# floating value of variable ------> is men decimal number hota hai!
price = 25.99
print(price)


print("my name is :",my_name)
print("my age is :",age)
print('Book Price is :',price)

# Assigment Opreator = assigment opreator ki right side wali value left side
# waly variable men store hogi.

age = 321
# update variable value with existing variable.
age2 = age
print(age2)

# identifire variables or functions k name hoty hain. 
# axhy programmer varible k nme simple to understand, short or meannig full rakhta hai.


# type() function se hum datatype malom kr skty hain.

print(type(name))
print(type(age))
print(type(price))


# primary deta types:
# String
# Integer ----> positive value---> 1, nagitive value----> -1 and zero 0.
# Float 3.99   4.45  9.00
# Boolean ----->  True | False
# None -----> jaha par hum koi value store nahi krwana chahty.


# boolean variable
isPresent = True
isSignIn = False

# None variable
square = None

print(type(isPresent))
print(type(square))


# checking type of type function😁
print(type(type))

# keywords ky name pr identifire ka name nhi rkh skty.
# yani variable or function ka name ka name keyword  k name par nahi rakh sakty.

# python case sensitive language hai

                    # Practice 1:
# Creat Sum of two numbers

number_one= 5
number_two= 6

total = number_one + number_two
print(total)


# Type of Tokens
# Punctuators --------> wo symbols jo python ky code ko orgnize krny k lye use hoty hain.
# (),[],{},@,#,-=,+=,/=,*=,//=,= etc.

# python implicit typed lnguage hai. yani alg se deta type bataye baghair ye khud se hi pehchan leti ai ky coder ny kon si deta type use ki hai.
# jab ky c++ or java explicit typed language hai in men batana parta hai k konsa deta type use kia hai jesy int age = 25.


                # Expression Execution
# string and numeric values can opreate thogether with *
A,B=2,3
Txt = "@"
print(2*Txt*3)
# ans is ---> @@@@@@

# string nd string can opreate with + is callesd conctintion.
A,B = "2",3
Txt="@"
print((A+Txt)*B)
# ans is ---> @2@2@2

# numaric values can oprate with all arthimatic opreators.
A,B = 2,3
C = 4
print(A+B*C)
# ans is ---> 14 q k * pehly dekha jaega.

# kaahin integer or float dono k darmiyan arthmetic opretion ho to result hamesha flot ayega

