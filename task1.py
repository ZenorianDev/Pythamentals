# Understanding Data Types and Variables

name = input("Enter your name: ")  # String
age = int(input("Enter your age: "))  # Integer
height = float(input("Enter your height in meters: "))  # Float

print("Before conversion:")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))


age = int(age)
height = float(height)


print("\nAfter conversion:")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))