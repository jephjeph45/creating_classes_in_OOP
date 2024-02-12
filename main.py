# TODO 1 Creating class
# use class key word and give it the name
# Use PascalCase to Name classes by Capitalizing the first letter of every word

# TODO 2 adding attributes to the object. comes after the period of the object created
# attribute is a variable associted with an object

# TODO 3 Creating a constructor
# Is part of the blueprint that enables use to specify of that should happen when our object is being constructed. Is called initializing an object
# Initializing sets variables to the startingvalue by using __init__.
# __init__ is used to initialize the attributes of the class
# attributes ate the things the class has

# TODO 4 Creating methods
# methods gives what the object does
# a function attached to a class is called a method
class User:

# defines trhe attributes of the class
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # Creates a default value, Must not be provided as a parameter when initializing a parameter
        self.following = 0

# define new methods of the class
    def follow (self, user):
        user.followers += 1
        self.following += 1


# Using the clas blueprint you create the first object as shown below
# To initialize an object from a class you add ()
andrew = User("001", "angela")
ian = User('002', 'Sela')
print(andrew.followers)

andrew.follow(ian)

print(andrew.following)
# user_1.id = "001"
# user_1.username = "Angela"
#
# print(user_1.username)