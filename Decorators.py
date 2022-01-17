"""Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class"""
def shout(txt):
    return txt.upper()

print("---------------------------------Example 1:Treating the functions as objects.--------------------------------------------")

print(shout('Hello'))

yell = shout #we have assign function as a variable

print(yell('Hello'))

#Example 2: Passing the function as an argument 
print("---------------------------------Example 2: Passing the function as an argument.--------------------------------------------")
def whisper(txt):
    return txt.lower()

def greet(func):
    greeting = func("Hi, I am created by function passed by argmt.")
    print(greeting)

greet(shout)
greet(whisper)

#Example 3: Returning functions from another function.
print("---------------------------------Example 3:Returning functions from another function.--------------------------------------------")

def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)
print(add_15(10))

print("---------------------------------Decorators.--------------------------------------------")

def hello_decorator(func):
    #inner 1 is wrapper func in which argmt is called
    #inner func can access the other local func 
    def inner1():
        print("This before function execution")

        #calling actual func inside wrapper func 
        func()
        print("This is after execution")

    return inner1

def func_2b_used():
    print("This is inside the function!!")

#passing func_2n_used inside decorator to control its behaviour
func_2b_used = hello_decorator(func_2b_used)

func_2b_used()

print("--------------------------------- find out the execution time of a function using a decorator.--------------------------------------------")

import time,math

#decorator to cal duration taken by any func
def cal_time(func):
    #added argmt insider inner1, if func takes any argmt can b added
    def inside(*args,**kwargs):
        #sorting time after execution
        begin = time.time()

        func(*args,**kwargs)

        #sorting time after func execution
        end = time.time()
        print("Total time taken in: ",func.__name__,end - begin)
    return inside

#this can b added to any func present, in this case calcualte factorial

@cal_time
def factorial(num):
    #sleep time 2 sec cz it takes very less time so that u can c acutal diff
    time.sleep(2)
    print(math.factorial(num))

factorial(10)

#function returns something or an argument is passed to the function

def hello_deco(func):
    def inner1(*args,**kwargs):
        print("after execution")
        returned_val = func(*args,**kwargs)
        print("after execution")

        return returned_val

    return inner1
@cal_time
@hello_deco
def sum_of_two(a,b):
    print("inside func")
    return a+b
a,b = 1,2
print("Sum = ",sum_of_two(a,b))


print("---------------------------------Chaining Decorators.--------------------------------------------")


def decor1(func):
    def inner():
        x = func()
        return x*x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2*x
    return inner

@decor1
@decor
def num():
    return 10
print(num())


