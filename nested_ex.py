classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]
}

# Task 1
# Find average of each class

def get_class_average(class_data):
  class_name = class_data[0]
  class_grades = [student["grades"] for student in class_data[1]]
  class_average = sum(grade for student_grades in class_grades for grade in student_grades) / sum(len(student["grades"]) for student in class_data[1])
  return f"{class_name}: {class_average}"

for class_name, students in classes.items():
  class_data = (class_name, students)
  print(get_class_average(class_data))


# Task 2 - each students average

def get_student_average(class_name, student_data):
    student_name = student_data["name"]
    student_grades = student_data["grades"]

    student_average = sum(student_grades) / len(student_grades)
    return f"{class_name}: {student_name}: {student_average}"

for class_name, students in classes.items():
    for student_data in students:
        print(get_student_average(class_name, student_data))

  