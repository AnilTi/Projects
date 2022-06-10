'''
In Python 3 predefined inbuilt decorators:-

1. @property decorator
2. @classmethod decorator
3. @staticmethod decorator

In Python 3 types of Methods & 2 types of Variables
in inside of class:-

1. Instance Method
2. Class Method
3. Static Method

a. Instance Variable:-
   A variable that is defined inside a method and
   belongs only to the current instance of a class.

b. Class Variable:-
   A variable that is shared by all instances of a class.
   Class variables are defined within a class but outside
   any of the class's methods.

Method− A special kind of function that is defined in a class
        definition.

'''

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def msg(self):
        print(self.name+" "+self.age)


print("Object 1:")
s1=Student("aman","23")
print(s1.name)
print(s1.age)
s1.msg()
print("****************")
print("Object 2:")
s2=Student("deepak","28")
print(s2.name)
print(s2.age)
s2.msg()
print("****************")

# In above class name & age both are instance variable,
# because these are defined inside of __init__() method.
# For each object, instance variable are different.

# here msg() method is called instance method,because
# we have passing self parameter, self is nothing, its
# represent object itself.Instance method is a most common
# type of method in python classes. They are called instance
# method because they can access unique data of their instance.

#**************************************************************#

class Student:
    clg_name="Delhi University"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def msg(self):
        print(self.name+" "+self.age)


print("Object 1:")
s1=Student("aman","23")
print(s1.name)
print(s1.age)
print(s1.clg_name)
#print(Student.clg_name)
s1.msg()
print("****************")
print("Object 2:")
s2=Student("deepak","28")
print(s2.name)
print(s2.age)
print(s2.clg_name)
#print(Student.clg_name)
s2.msg()
print("****************")

# here clg_name is a class variable. all the objects
# of that class can used that variable. Its always
# defined outside of methods & inside of class.

# ************************************************************#

# Diff. b/w Instance Method & Class Method :-

# In instance method we can pass object as a parameter self,
# but in class method we can pass cls parameter, cls means
# class itself & also used @classmethod decorator.


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def msg(self):
        print(self.name+" got "+self.marks,"%")

s1=Student("aman","93")
s2=Student("deepak","65")


# In this class supoose we want to count how many objects are
# created for this u can create class method.

class Student:
    count=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.count=Student.count+1
    def msg(self):
        print(self.name+" got "+self.marks,"%")
    @classmethod
    def obj_count(cls):
        return cls.count



s1=Student("aman","93")
s2=Student("deepak","65")
print(Student.obj_count()) #call using class name
print(s1.obj_count()) # call using object name
print(s2.obj_count()) # call using object name

# here obj_count() is a class method. It is accesible both class 
# name as well as objects name.
# *********************************************************************#


# static method :- In instance method & class method we have must
# pass 1 parameter self & cls, but in case of static method we have
# no pass any parameter , its work just like normal function, but
# it belongs to the class member. It is defined using @staticmethod
# decorator. How to check age of students using static method:-

class Student:
    count=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.count=Student.count+1
    def msg(self):
        print(self.name+" got "+self.marks,"%")
    @classmethod
    def obj_count(cls):
        return cls.count
    @staticmethod
    def get_age(age):
        if(age<17):
            print("belongs to school !!")
        else:
            print("don't belongs to school !!")



s1=Student("aman","93")
s2=Student("deepak","65")
print(Student.obj_count())
print(s1.obj_count())
Student.get_age(16)
s1.get_age(20)


# Diff. b/w class method & static method:-

# 1. class method takes cls as first parameter, while static
#    method need no specific parameters.

# 2. static methods knows nothing about the class state, while
#    class methods can access and modify class state.

# 3. @classmethod decorators are used to create class method,
#    @staticmethod decorators are used to create static methods.

#***************************************************************#


# @property decorator - By using it, we can use the class
# function as an attribute.


class Student:  
    def __init__(self,name,grade):  
         self.name = name  
         self.grade = grade  
    @property  
    def display(self):  
         return self.name + " got grade " + self.grade  
  
stu=Student("Raj","B")  
print("Name:", stu.name)  
print("Grade:", stu.grade)  
print(stu.display)



