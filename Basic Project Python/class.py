class name:
    def __init__(self, age, job):
        self.da = age
        self.age = age
        self.job = job
obj = name(12, "marketing")
print(obj.da)
print(obj.age)
print(obj.job)
exit()
#7.1 Describe the relationship between an object and its defining class. 

#ans:  a class defines the common structure and behavior of objects, while an object is a specific instance-
 # of that class with its own state and identity.

#7.2 How do you define a class? 
#ans: A class defines the properties and behaviors for objects.
class name():
    pass


# 7.3 how to make object

#ans
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started!")

# Instantiate an object
my_car = Car("Toyota", "Camry")

# Access object attributes
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry

# Invoke object methods
my_car.start_engine()  # Output: Engine started!


#7.4 What is the name of the initializer method?
#answer: The initializer method in Python is called __init__(). 
# It is a special method within a class that is automatically called when an object is created (instantiated).


#7.5 The first parameter in the initializer method is named self by convention. What is the role of self?
#answer: In Python, the self parameter in the initializer method (and other instance methods) of a class refers to the instance of the object itself.
# It is a convention to name the first parameter of instance methods as self, although you can technically use any valid variable name.

# for exampe 
class Person:
    def __init__(self, name, age):
        self.name = name  # Assigning the name argument to the object's name attribute
        self.age = age    # Assigning the age argument to the object's age attribute

    def greet(self):
        print("Hello, my name is", self.name,)  # Accessing the object's name attribute using self

person = Person("John", 25)
person.greet()  # Output: Hello, my name is John

#7.6 What is the syntax for constructing an object? What does Python do when constructing an object?

#The syntax for constructing an object in Python involves calling the class name followed by parentheses.
# for example 
# object_name = ClassName(arg1, arg2, ...)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 25)

#7.7 What are the differences between an initializer and a method?
#ans: the initializer is a special method used for object initialization, automatically called during object creation.
# Methods, define the behavior and functionality of the object and need to be explicitly invoked to perform their actions.

#7.8 What is the object member access operator for? 
#ans: The object member access operator, represented by a dot (.), is used to access the attributes and methods of an object in Python.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

person = Person("John")
print(person.name)  # Accessing the 'name' attribute of the 'person' object
person.greet()      # Invoking the 'greet()' method of the 'person' object


#7.9 What problem arises in running the following program? How do you fix it? - -init- -
#incorrect usage of underscores in the __init__() method of the A class.
# correcr underscore is 
class A:
    def __init__(self, i):
        self.i = i

def main():
    a = A()
    
    print(a.i)

main()  # Call the main function

#What is wrong with the following programs?
#ans: a is correct

