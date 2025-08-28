# Understanding Data Types and Variables

name = input("Enter your name: ") 
age = input("Enter your age: ")
height = input("Enter your height in meters: ")

print("\nBefore conversion:")
print(f"Value of name: {name}")
print(f"Value of age: {age}")
print(f"Value of height: {height}")

age = int(age)
height = float(height)

print("\nAfter conversion:")
print(f"Value of name: {name}")
print(f"Value of age: {age}")
print(f"Value of height: {height}")
