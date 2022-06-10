# Class method are basically used for to change
# the values of class variable.

class Employee():
    no_of_leaves=8

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def output(self):
        return f"The Name is {self.name} , Salary is {self.salary} and Role is {self.role}"
    

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

obj1=Employee("Aman",9000,"Executive")
obj2=Employee("Deepak",45000,"Manager")

print(obj1.output())
print(obj2.output())

print(obj1.no_of_leaves)

Employee.no_of_leaves=12
print(obj1.no_of_leaves)

# if u want to change the values of class variable
# using instance object,then its create a new instance
# variable.
obj1.no_of_leaves=15 
print(obj1.no_of_leaves)

print(obj2.no_of_leaves)
print(Employee.no_of_leaves)

obj1.change_leaves(18)
print(obj1.no_of_leaves)
print(Employee.no_of_leaves)



