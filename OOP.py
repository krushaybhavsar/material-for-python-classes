# Object Oriented Programming in Python

# def hello():
#     print("hello")

# print(type(hello)) # from Function class

# x = 1
# y = "hello"
# print(x + y) # objects of string and int can't be added together

# string = "hello" # if it was equal to 1, you get error because int object has not method upper
# print(string.upper()) # calling a method of a specific object

# class Dog:  # creation of a class

#     def __init__(self, name, age): # Constructor --> instantiates variables right when the object is created
#         self.name = name # instantiated an attribute of the class dog called name
#         self.age = age

#     def add_one(self, x): # can have any kind of method (returns and with parameter)
#         return x + 1

#     def bark(self): # defining method in the class, all methods in a class have to have the parameter self
#         print("bark") 
    
#     def get_name(self):
#         return self.name
    
#     def set_age(self, age):
#         self.age = age

# d = Dog("Tim", 20) # creation of an object of class Dog (parameters are the parameter of the contructor)
# print(type(d)) # prints <class '__main__.Dog'> --> the main part tells us the module the object was defined in, by default it is main
# d.bark()
# print(d.add_one(6))
# d2 = Dog("Bill", 12) # assigns name bill to dog object (notice have both objects hve different names)
# print(d2.name)
# print(d2.get_name())
# d2.set_age(50)
# print(d2.age)

# WHY OOP?
# it is good if you want to create multiple instances of something with the same attributes

######### EXAMPLE CODE WITH MULTIPLE CLASSES ########################################################################################

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade

# class Course: 
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = [] # made attribute without having var in parameter
    
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value/len(self.students)

# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# # print(course.students[0].name)
# print(course.add_student(s3))
# for student in course.students:
#     print(student.name)
# print(course.get_average_grade())

######### INHERITANCE ########################################################################################
# class Pet: # generalization
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")

#     def speak(self):
#         print("I don't know what to say")

# class Cat(Pet): # means that I am inheriting the upper level class
    
#     def __init__(self, name, age, color):
#         super().__init__(name, age) # calling upper level class's constructor
#         self.color = color
    
#     def speak(self):
#         print("meow")

#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# class Dog(Pet):
#     def speak(self):
#         print("bark")

# class Fish(Pet):
#     pass

# p = Pet("Tim", 19)
# p.show()
# p.speak()

# c = Cat("Bill", 34, "blue")
# c.show()
# c.speak()

# d = Dog("Jill", 25)
# d.show()
# d.speak()

# f = Fish("Bubbles", 5)
# f.speak()

########## CLASS ATTRIBUTES AND CLASS METHODS ##############################################################################
# class attributes are attributes that are specific to the class, not to an instance or an object of that class

# class Person:
#     number_of_people = 0 # this is a class attribute and because it is not defined as an attibute of an instance of the class, it is defined for the entire class (does not use self)

#     def __init__(self, name):
#         self.name = name
#         # Person.number_of_people += 1
#         Person.add_person()

#     @classmethod # decorator
#     def get_number_of_people(cls): # instead of self, use cls
#         return cls.number_of_people

#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1

# p1 = Person("Tim")
# p2 = Person("Jill")

# print(p1.number_of_people)
# #          OR     
# print(Person.number_of_people)

# Person.number_of_people = 8
# print(p2.number_of_people)

# p3 = Person("John")
# print(Person.number_of_people)
# p4 = Person("Bob")
# print(Person.number_of_people)

# print(Person.get_number_of_people())

######## STATIC METHODS #############################################################################################
# class Math:

#     @staticmethod
#     def add5(x):
#         return x + 5

# print(Math.add5(5))

