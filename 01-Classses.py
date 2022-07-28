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