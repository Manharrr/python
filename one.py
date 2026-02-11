# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")


# a = Animal()
# d = Dog()
# c = Cat()

# def show(obj):
#     obj.sound()

# show(Dog())
# show(Cat())


# class Student:
#     def __init__(self):
#         self._age = 22

# s = Student()
# print(s._age)


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary   # private variable

#     def show_salary(self):
#         print("Salary:", self.__salary)

# emp = Employee("Manhar", 30000)
# print(emp._Employee__salary)


# # print(emp.__salary)   

# # emp.show_salary()       


# def get_number():
#     return 10

# x = get_number()
# print(x)


# a=[1,2,3]
# b=[1,2,3]

# print(a is not b)
# print(a is b)

# print(a==b)

# mark= 1000

# if mark >=90:
#     print("aaa")
# elif mark >=75:
#     print("bbbb")
# elif mark >=50:
#     print("ank kazhuiv ella")
# else:
#     print("weekback")

choice="tea"

match choice:
    case "coffee":
        print("coffeeee sekleceteddd")


# arr=[1,2,3,4,5,6,]

# for i in arr:
#     pass

# i=0
# while  i <30:
#     print(i)
#     pass
#     i+=1
   

# for i in range(10,0,-1):
    # pass
    # if i ==5:
    #     continue
    # print(i)

# lst=[23,44,3,2,55,4,5,6,77,8,88,99,101,2,33,32,45,65]

# lst.insert(3,"manharrrr")
# # lst.pop(1)
# # lst.remove("manharrrr")
# # lst.clear()
# del lst[1]
# print(lst)


# for i in lst:
#     print(i)


new=[]
# for i in range(1,6):
#     new.append(i*i)
#     print(new)

# new=[i*i for i in range(1,6)]
# print(new)

# lst=[23,44,3,2,55,33,32,45,65]
# lst.insert(0,99)

# print(lst)



# n = 5

# for i in range(1, n+1):
#     print(" " * (n - i) + "* " * i)

# s = {10, 20, 30,40,1,23,34,2}

# # s.update([44,43,56,78])
# s.clear()
# print(s)

# s.pop()

# s.add((333,11))
# s.clear()

# print(s)



# text= "hello world"

# new=""

# for i in text:
#     if i == " ":
#         break

# stud={
#     "name":"manhar",
#     "age":21,
#     "place":"mmmmmm",
# }
# stud["age"]=100
# stud["qualififi"]="bca"
# stud.pop("name")

# stud.update({"stalam":"tiriruuuu"}) #///
# # print(stud["name"])
# print(stud.get("age")) 

# del stud["place"]
# stud.popitem()
# print(stud)   

# for val in stud.values():
#     print(val)

# new=[]
# new=[i *i for i in  range(0,5)]
# print(new)



# new={x:x*x for x in range(1,6) if x%2==0}
# print(new)

# new={x: x for x in range(1,10)}

# print(new)

# txt="hello world"

# for i in txt.split():
#     if i=="hello":
#         print(i)
# def man(name,age):
#     print(name,age)

# man(name="manharrr",age=333)



try:
    a=int(input("enter a nummm"))
    result=100/a
except ZeroDivisionError:
    print("error unddd")
except ValueError:
    print("only by nummm divide patollu")
else:
    print(result)

finally:
    print("thank youu")
    
