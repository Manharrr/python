# print("Hello Manhar, Python is working!")
# print("how are uuuuuuuuu") 
# count = 1

# while count <= 10:
#     print(count)
#     count += 1

"""num=[1,2,3,4,5,6,7,8,9]
#num[0]=99
#num.insert(1,22)
num.pop(0)
print(num)"""

#num=(1,2,3,4,5)
#print(num[1:2])
#num[0]=9
#print(num[-2])


"""print(len(num)) 
print(max(num))   
print(min(num))""" 

"""for i in range(5):
    print("hello")"""

"""nums = [10, 20, 30]
total=0

for i in nums:
    total += i
print(total)

i=1
while i<=5:
    print(i)
    i +=1
"""
"""nums = [1,3,4,5,5,6,]

out=[n*2 for n in nums]



print(out)


s = {10, 20, 30,40,50,60,70}

x = s.pop()
print(x)
print(s)


"""
"""import copy

stud={"name":"manhar","age":22,"place":"mlp"}

text=copy.deepcopy(stud)
print(text)"""


#print(stud.get("city"))
#print(stud["city"])
"""print(stud.items())"""
"""stud["name"]="nabeel"
stud["country"]="abccc"
stud.update({"name":"peeru"})
stud.update({"course": "Backend Python"})
del stud["course"]
#del stud["country"]
stud.popitem()
#stud.clear()
print(stud)"""

"""for key in stud:
    print(key)

for val in stud.values():
    print(val)"""

"""for key,value in stud.items():
    print(key,value)

even = {x: x*x for x in range(1, 10)}

print(even)

names = ["a", "b", "cccc"]
lengths = {name: len(name) for name in names}
print(lengths)

data = {"a": 1, "b": 2}
swapped = {v: k for k, v in data.items()}
print(swapped)"""

"""
a = "Hello"
b = "World"

print(a + " "+ b)

print("h1 " *3)

name = "Manhar"
age = 22

print(f"My name is {name} and age is {age}")

"""
"""
text = "python Programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
"""


"""def myfunc(*args):
    print(args[3])

myfunc(1, 2, 3, 4)"""

"""def stud(**kwargs):
    print(kwargs)
    
    
stud(name="manhar",age=21,place="xmsmxsmc",phn=21423455665466)  """

"""def show(n):
    if n == 0:        # base case
        return
    print(n)
    show(n-1)        # recursive call

show(5)"""

"""add=lambda a,b :a+b
print(add(5,6))"""

"""import math

print(math.sqrt(25))     # square root
print(math.pow(2, 3))    # power


print(math.pi)
print(math.e)

"""

"""import datetime

today = datetime.date.today()
now = datetime.datetime.now()

print(today)
print(now)
"""
"""import re

text = "My number is 9876543210"
x = re.search("[0-9]{10}", text)
print(x.group())"""
"""
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Division error")
except ValueError:
    print("Wrong input")
else:
    print("Calculation successful")"""

"""
try:
    a = int(input("Enter a number: "))
    result = 100 / a
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter only numbers")
else:
    print("Result:", result)
finally:
    print("Thank you for using the program")
"""

"""
count = 1

def update():
    global count
    count = 5
    
update()
print(count)
"""

# def my_decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello")

# greet()

# class Person:          # Class
#     def __init__(self):
#         print("Hello!")

# p1 = Person()          # Object
# p2 =Person() 

# class Demo:
#     school = "XYZ"      # static variable

#     def __init__(self, name):
#         self.name = name   # instance variable

#     def show(self):
#         age = 20          # local variable
#         print(self.name, age, Demo.school)

#         # create object
# d1 = Demo("Manhar")

# # call method



# class Parent:
#     def show(self):
#         print("I am Parent")

# class Child(Parent):
#     def display(self):
#         print("I am Child")

# obj = Child()
# obj.show()
# obj.display()


# nam2="manhar"
# print(nam2)




# i=0
# while i<=20:
#     print(i)
#     i+=3


# nums = [1, 2, 3]
# it = iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# nums = [1, 2, 3, 4]

# def add_10(x):
#     return x + 10

# result = map(add_10, nums)
# print(list(result))


# from functools import reduce

# num=[2,3,4,5,6,100]

# ttl=reduce(lambda a,b : a*b , num)
# print(ttl)

# for i in num:
#     print(i)


keys = ["a", "b", "c"]
values = [1, 2, 3]

d = dict(zip(keys, values))
print(d)

