# Setup Code
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]
# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.

students = sorted(students, key=lambda student: student["grade"], reverse=True)

for rank, student in enumerate(students, start=1):
    student["rank"] = rank

print(students)
