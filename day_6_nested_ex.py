from pprint import pprint

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

# def get_class_average(class_list):
#   class_name, students = class_list
#   class_grades = []
#   total_grades = 0
#   total_students = 0

#   for student in students:
#       student_grades = student["grades"]
#       for grade in student_grades:
#           class_grades.append(grade)
#       total_grades += sum(student_grades)
#       total_students += len(student_grades)

#   class_average = total_grades / total_students
#   return f"{class_average: .2f}"


# class_new_list = {}

# for class_name, students in classes.items():
#   class_list = (class_name, students)
#   class_new_list[class_name] = get_class_average(class_list)

# pprint(class_new_list)

# Task 2 - each students average

# def get_student_average(class_name, student_list):
#     student_name = student_list["name"]
#     student_grades = student_list["grades"]

#     student_average = sum(student_grades) / len(student_grades)
#     return f"{class_name}: {student_name}: {student_average: .2f}"


# for class_name, students in classes.items():
#     for student_list in students:
#         print(get_student_average(class_name, student_list))

# student_d = {}

# for class_name, students in classes.items():
#     class_list = {class_name: {}}
#     for student in students:
#         student_name = student["name"]
#         student_grades = student["grades"]
#         student_average = sum(student_grades) / len(student_grades)
#         class_list[class_name][student_name] = student_average
#         student_d.append(class_list)

# print(student_d)


# student_dict = {}

# for class_name, students in classes.items():
#     class_list = {}
#     for student in students:
#         student_name = student["name"]
#         student_grades = student["grades"]
#         student_average = sum(student_grades) / len(student_grades)
#         class_list[student_name] = round(student_average, 2)
#     student_dict[class_name] = class_list

# pprint(student_dict)

#task 3: task 1 + list comprehension

def get_class_average(class_list):
    class_name, students = class_list
    class_grades = [grade for student in students for grade in student["grades"]]
    total_grades = sum(class_grades)
    total_students = sum(len(student["grades"]) for student in students)
    class_average = total_grades / total_students
    return f"{class_average: .2f}"

class_new_list = {class_name: get_class_average((class_name, students)) for class_name, students in classes.items()}

pprint(class_new_list)



#task 4: task 2 + list comprehension

student_dict = {class_name: {student["name"]: round(sum(student["grades"]) / len(student["grades"]), 2) for student in students} for class_name, students in classes.items()}

pprint(student_dict)

# nested for loop ex
# for i in range(10):
#   for j in range(5):
#     print((i, j))