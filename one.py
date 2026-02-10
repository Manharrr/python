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


# # print(emp.__salary)   ❌ ERROR (cannot access)

# # emp.show_salary()       # ✅ correct way


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