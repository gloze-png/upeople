def invert_student_courses(student_dict):
    """
    Function to invert a dictionary where students are keys and lists of courses are values.
    The inverted dictionary will have courses as keys and lists of students as values.
    """
    inverted_dict = {}

    # Iterate through the original dictionary
    for student, courses in student_dict.items():
        for course in courses:
            # If the course is not yet in the inverted dictionary, initialize it with an empty list
            inverted_dict.setdefault(course, []).append(student)

    return inverted_dict


# Sample input dictionary
students_courses = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Print the original dictionary
print("Original Dictionary:")
for student, courses in students_courses.items():
    print(f"{student}: {courses}")

# Invert the dictionary
inverted_courses = invert_student_courses(students_courses)

# Print the inverted dictionary
print("\nInverted Dictionary:")
for course, students in inverted_courses.items():
    print(f"{course}: {students}")
