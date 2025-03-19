# # Lists of students and their scores
# students = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# # Using zip() to iterate over both lists together
# for student, score in zip(students, scores):
#     print(f"{student} scored {score}.")


# fruits = ["Apple", "Banana", "Cherry"]

# # Using enumerate to get index and value
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}. {fruit}")


grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Using .items() to loop through dictionary key-value pairs
for student, grade in grades.items():
    print(f"{student} received a grade of {grade}.")


