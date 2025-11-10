# 🟢 Easy
# 1. Write a loop that prints numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# 🟡 Medium
# 2. Ask the user for their favorite color and age.
# Display both on separate lines using a loop.
color = input("Enter your favorite color: ")
age = input("Enter your age: ")

details = [("Favorite Color", color), ("Age", age)]

for label, value in details:
    print(f"{label}: {value}")

# 🔴 Hard
# 3. Use a nested loop to print this pattern:
# 1
# 12
# 123
# 1234
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()