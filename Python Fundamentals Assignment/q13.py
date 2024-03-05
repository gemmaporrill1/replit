# Setup Code
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40},
]
# Expected Task: Aggregate points for each house and print the total.

aggregated_points = {}

for house in house_points:
    house_name = house["house"]
    points = house["points"]

    if house_name in aggregated_points:
        aggregated_points[house_name] += points
    else:
        aggregated_points[house_name] = points

for house, total_points in aggregated_points.items():
    print(f"{house}: {total_points} points")
