# Create a class named Person with attributes and a method

class Person():
    def __init__(self, first_name, last_name, age):
        # attributes:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # methods:
    def full_name(self):
        return self.first_name + " " + self.last_name

    
# create objects/ Instances from the class
objPerson1 = Person("John", "Smith", 25 )
objPerson2 = Person("Kate", "Jones",20)

# access and print an objects attribute
print(objPerson1.first_name)
print(objPerson2.first_name)

# access the object method full_name()
print(objPerson1.full_name())
print(objPerson2.full_name())

# print the memory location of each object
# This location will change everytime you run the applications
# as the memory is returned to the operating system when the application 
# finishes.
# Note: They reside in different areas in memory: THEY ARE UNIQUE 
print(id(objPerson1))
print(id(objPerson2))

# add an instance attribute after the object has been created
objPerson1.middle_name = "Jimmy"
print(objPerson1.middle_name)

# error as objPerson2 does NOT have an instance attribute "middle_name"
# print(objPerson2.middle_name)

# print all object attributes:
print(objPerson1.__dict__)
print(objPerson2.__dict__)

# Print out object methods and attributes without attribute values:
print(dir(objPerson1))

# Update an instances attribute
objPerson1.first_name = "Johnny"
objPerson2.first_name = "Katrina"

print(objPerson1.full_name())
print(objPerson2.full_name())

print(dir(int))
print(dir(str))


