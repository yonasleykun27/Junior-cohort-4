# Question:
# Create three variables: one integer, one float, and one string.
# Print each variable and its data type using type().

# Easy
num = 10          # integer
price = 12.5      # float
name = "John"     # string

print(num, type(num))
print(price, type(price))
print(name, type(name))

# 🟡 Medium

# Question:
# Ask the user for their favorite color and their age.
# Example Output:
# Your favorite color is [color]
# Your age is [age] years old!

# Medium
color = input("Enter your favorite color: ")
age = input("Enter your age: ")

print("Your favorite color is", color)
print("Your age is", age, "years old!")


# 🔴 Hard

# Question:

# Create five variables of different data types: integer, float, string, list, and dictionary.

# Print each variable, its type, and for sequence/mapping types, also print the length.

# Hard
num = 25                             # integer
pi = 3.1416                          # float
message = "Hello, Python!"           # string
fruits = ["apple", "banana", "cherry"]  # list
person = {"name": "John", "age": 20} # dictionary

print(num, type(num))
print(pi, type(pi))
print(message, type(message), "Length:", len(message))
print(fruits, type(fruits), "Length:", len(fruits))
print(person, type(person), "Length:", len(person))









# 🟢 Easy Level

# Question:
# Write a Python program that asks the user to enter two numbers.
# Then print their sum, difference, and whether the first number is greater than the second.


# Enter first number: 8  
# Enter second number: 5  
# Sum = 13  
# Difference = 3  
# Is first greater than second? True

# Easy Level
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Is first greater than second?", num1 > num2)

# 🟡 Medium Level

# Question:
# Create a dictionary of countries and their capitals.
# Add one new country to it.
# Then update one existing capital.

# {'Ethiopia': 'Addis Ababa', 'Kenya': 'Nairobi', 'Sudan': 'Khartoum', 'Eritrea': 'Asmara'}

# Medium Level
countries = {
    "Ethiopia": "Addis Ababa",
    "Kenya": "Nairobi",
    "Sudan": "Khartoum"
}

# Add one new country
countries["Eritrea"] = "Asmara"

# Update one existing capital
countries["Sudan"] = "Khartoum City"

print(countries)
# 🔴 Hard Level

# Question:
# Write a Python program that:

# Creates a dictionary of students and their scores (at least 3 students).

# Asks the user to input a new student name and score, and add it to the dictionary.

# Asks the user to input the name of an existing student and update their score.

# Calculates and prints:

# The student with the highest score

# The student with the lowest score

# The average score of all students

# Hard Level
students = {
    "John": 85,
    "Sara": 90,
    "Melek": 78
}

# Add a new student
new_name = input("Enter new student name: ")
new_score = float(input("Enter new student score: "))
students[new_name] = new_score

# Update existing student's score
update_name = input("Enter the name of a student to update their score: ")
if update_name in students:
    students[update_name] = float(input("Enter new score for " + update_name + ": "))
else:
    print("Student not found!")

# Find highest and lowest
highest_student = max(students, key=students.get)
lowest_student = min(students, key=students.get)
average_score = sum(students.values()) / len(students)

print("\n--- Results ---")
print("All Students:", students)
print("Highest Score:", highest_student, "=", students[highest_student])
print("Lowest Score:", lowest_student, "=", students[lowest_student])
print("Average Score:", average_score)








# 🟢 Easy Level

# Question:
# Create a set of your favorite fruits and print it.
# Add a new fruit to the set and print the updated set.

# Easy Level
fruits = {"apple", "banana", "mango"}
print("My favorite fruits:", fruits)

# Add a new fruit
fruits.add("orange")
print("Updated fruits:", fruits)


# 🟡 Medium Level

# Question:
# Ask the user for their age.
# If age ≥ 18, print "You can vote"; otherwise, print "You are too young to vote".



# Medium Level
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You are too young to vote")


# 🔴 Hard Level — Conditional Statements

# Question:
# Ask the user to enter a score (0–100).
# Print the grade based on the score:
# A → 90–100
# B → 80–89
# C → 70–79
# D → 60–69
# F → below 60
# If the score is invalid (<0 or >100), print "Invalid score".


# Hard Level
score = float(input("Enter your score (0–100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
