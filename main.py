#Functions:
"""Create a sum () so it can take 2 arguments to do sum"""
"""def sum(a,b):
    print(a+b)
a = int(input("enter your number: "))
b = int(input("enter your number: "))
sum(a,b)"""

#write a python function to sum all the numbers in a list
#sample list: [8,2,3,0,7]
#expected: 20
"""def sum(numbers):
    total = 0
    for x in numbers:
        total = total + x
    print(total)
numbers = [8,2,3,0,7]
sum(numbers)"""
#write a function to multiply all the elements in a collection
"""def sum(numbers):
    total = 1
    for x in numbers:
        total = total * x
        print(total)
numbers = [8,2,3,0,7]
sum(numbers)"""
#******************************************** practice this code *******************************************************
#write a python function to print even numbers from the list
#sample list:- [1,2,3,4,5,6,7,8,9]
#expected:- [2,4,6,8]

#write a function that converts a decimal numbers in to binary number
"""def dectobin(num):
    if num>1:
        dectobin(num//2)
    print(num % 2, end="")
dectobin(11)"""
#return():-
"""def dectobin(num):
    if num>1:
        dectobin(num//2)
    return(num % 2)#---> it returns your output
print(dectobin(11))"""

"""sum = 10
def f1(x):
    return x + sum
print(f1(5))"""
"""return:- a special key word that u can use inside a function
or methods to send the function results back to the caller."""
#type("hello")
#len("hello")
"""def f1(x):
    print(x)
f1(10)"""
"""def f2(x):
    return x
print(f2(10))"""
#what is the purpose of return?
"""A return statement is used to end the execution of the function call 
and “returns” the result (value of the expression following the return keyword) to the caller.
The statements after the return statements are not executed.
If the return statement is without any expression, then the special value None is returned."""
"""when you return the value you can decide what you gonna do with value."""
"""x = len(input("enter the string"))
print(x**2)"""

"""def f1(x):
    print(x) #--->10
print(f1(10))  #--->None
#why we are getting none?"""
"""when i use print(x) and given the argument f1(10) the 10 will gets to the f1(x) place and first prints the 10 """
"""def f1(x):
    return x
print(f1(10))"""
"""sum = 10
def fun_sum(x):
    return x + sum
print(fun_sum(100))"""

"""sum = 10
def fun_sum(x):
    a = x + sum
    return a
print(fun_sum(100))"""

#write a program to print sum of range of numbers.
#sample input:- 7
#expected output:- 28

"""num = int(input("enter your number: "))
sum = 0
for i in range(0,num+1):
    sum = sum+i
    print(sum)"""
"""num = int(input("enter your number: "))
sum = sum(range(1,num+1))
print(sum)"""
#***********************************************************************************************************************
#list comprehension:-
"""it offers you a smaller line of code that you can create a new list from the existing list"""
"""list_fruits = ["Apple","banana","pineapple","mango","kiwi"]
#print the fruits with letter "a" in it and store it in new list.
new_list = []
for i in list_fruits:
    if "A" in i:
        new_list.append(i)
print(new_list)"""

"""list_fruits = ["Apple","banana","pineapple","mango","kiwi"]
#new_list = [items(i) for items(i) in "collection name"]
new_list = [x for x in list_fruits if "e" in x]
print(new_list)"""

#print the new list with out banana from the existing list_fruits
"""list_fruits = ["Apple","banana","pineapple","mango","kiwi"]
new_list = [x for x in list_fruits if x!= "banana"]
print(new_list)"""
#create list of numbers from 0 to 20?
"""numbers = []
for x in range(21):
    numbers.append(i)
print(numbers)"""

"""numbers = [x for x in range(21)]
print(numbers)

#from the above list if i want to even numbers in new list then create new list withneven numbers
numbers = [x for x in range(21) if x%2 == 0]
print(numbers)

#create the new list with odd numbers
numbers = [x for x in range(21) if x%2 != 0]
print(numbers)
#Note:- So LC(lisi comprehencen) can offer shortest syntax and also it is time efficient.

#create a new list of numbers in range of 20 the output must be in multiple of 2.
numbers = [x*2 for x in range(21)]
print(numbers)"""

#lambda, filter, map

#lambda():-
#what is lambda?
#lambda is an "anonymous function"
#"anonymous function" means this function doesn't have name.
"""def f1 (x):
    return(x)
print(f1(10))"""
#syntax for lambda():- "lambda arguements:expression"
#so lambda is an anonymous function it can have many arguments and single expression.
#what is an expression?
#expression is some kind of statement/calculation/step using that value to give single
#lambda is an anonymous function how can you call it
#we generally use this function where it has some name.
#means we can create a variable to call this function.
"""x = lambda a: a+10
#when you are calling the lambda function use the variable name
print(x(5))"""
"""x = lambda a,b,c : a+b+c+
print(x(5,6,7))"""
#when we can use lambda function?
#create a function that can give square of every number?
"""def square(x):
    return x**2
def cube(x):
    return x**3
def four(x):
    return x**4
def sqrt(x):
    return x**0.5
print(square(4))
print(cube(4))
print(four(4))
print(sqrt(4))"""

"""def power(n):
    return lambda a: a**n
square = power(2)
cube = power(3)
print(square(6))
print(cube(3))"""
#similarly try the lambda function for the multiplication.


#Global varaible and local varaible.
#hat is global and local variables?
#global variable is a variable that can create outside the function
#you can access the
"""x = "amazing"
print(x)
def f():
    return x
print(f())"""
#what is local variavble?
#creating a function inside the function is known as local variable.
#local vRIABLE IS THE Temporary variable , it only losts inside the function
"""def f():
    x = "fantastic"
    return x
print(f())"""
"""Note:- even the variable names are same the local variables never effect the global variables."""

#map():-
#what map dose?
#it uses a function on iterables/.
#what is iterables?
#iterables are nothing but list,tuple,set,array,
#map will take an function and run it over the iterables.
"""functions are the 1st class objects. 
which means 1 function can act as argument for another function"""
#syntax :- map= (function,iterables)
"""a = ['apples', 'banana','cherries', 'pineapple']
length = []
for i in a:
    length.append(len(i))
print(length)
#do same though LC
l = [len(i) for i in a]
print(l)"""
"""a = ['apples', 'banana', 'cherries', 'pineapple']
#if you want to display the output by using the map function we need to decide in wich iterables the output has tober
length = tuple(map(len,a))
print(length)"""
"""a = ['apples', 'banana', 'cherries', 'pineapple']
def f1(x):
    return "hello" + x
#print(f1(" apples"))
#apply the function for each item in the collection.
l = list(map(f1,a))
print(l)"""
#when we have to use the map function?
#when we are having multiple user input collection then we can use the map function
"""user = input()
print(user)
print(type(user))
#i want to seperate this value

user = input().split()
print(user)
print(type(user))"""
#how to convert above thing in integer"""
"""number = []
for x in number:
    number.append(int(x))
print(number)
print(type(number))"""
"""31-07-2024"""
#takea set of numbers being seperated with the spaces
"""user = input()
print(user)
print(type(user))"""
#if i want to seperate this number
"""user = input().split()
print(user)
print(type(user))"""
#how to convert this string of elements in list to integer
"""user = input().split()
print(user)
print(type(user))
number = []
for x in user:
    number.append(int(x))
print(number)
print(type(number))"""
#user = input().split()
"""number = tuple(map(int,input().split()))
print(number)"""
#Note:- before executing the map() we need to decide in what type of collection, do we need that
#how can we print the following 10 20 30 40 50 in double that to in tuple?
#lambda:- you can have many arguments but single expression
"""double = tuple(map(lambda x : x * 2, map(int,input().split())))
print(double)
#map(int,input().split())---> map storing entire thing/data if we want it in a readable object 
we need to add tuple,list,set."""
#*****************************************************************************************************************************************
"""filter()---> collection_name(filter(function,iterable))
filter gives the output of the collection if the condition is true"""
"""age = [18,48,21,16,24,15,56,12,14,20,18]
def adult(x):
    if x >= 18:
        return x
f1 = list(filter(adult,age))
print(f1)
f1 = list(filter(lambda a:a >= 18,age))
print(f1)"""
#how can i give expressions when i am using the conditional statement.
#shell we logical operaters in lambda?----> yes we can use
"""age = [18,48,21,16,24,15,56,12,14,20,18]
f1 = list(filter(lambda a:a >= 18 and a<=30 ,age))
print(f1)"""
"""f1 = list(filter(lambda a:18<=a<=30 ,age))
print(f1)
#so filter basically filters ypur original collection that returns true or false, 
any value that comes out to be true original value can be stored as a collection(list, tuple, set) of items
#List comprehencen, lambda, map, filter, along with sending one function as argument to another function"""
"""age = [18,48,21,16,24,15,56,12,14,20,18]
def adult(x):
    if x >= 18:
        return x
f1 = list(filter(adult,age))
print(f1)
f1 = list(map(lambda a:a >= 18,age))
print(f1)"""

#Regular expressions:- is a building pakage which is known as "re"
#A RegEx, or Regular expressiopns is a sequence of characters that founds a search pattern.
#import re
#txt = "hello world!"
#search weather world is present or not
#x = re.search("world!$",txt)
#print(x)
#Regular expression functions
#findall()---> returns a list containing all objects
#search()---> returns match object
#split()---> returns a list
#sub ---> replace one or many maches with the string


























