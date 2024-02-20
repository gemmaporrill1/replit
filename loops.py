# while loop

# num_rows = int(input("how many rows? "))

# row = 1
# while row <= num_rows:
#   print('😊' * row)
#   row += 1

# for loop
# num_rows = int(input("how many rows? "))
# for row in range(1, num_rows+1):
#   print('😊' * row)

# similar to slice syntax
# range(3) | range(end)
# randge(1,3) | range(start, end)

#task

player_stats = [10, 30, 60] # create a copy

# powered_up = player_stats.copy()

# for i in range(len(player_stats)):
#   powered_up[i] *= 2 

# print(player_stats, powered_up)
  

#power: [20, 60, 120]

#list comprehension
#double all the stat for each stat present in player stats
# powered_up_stats = [stat * 2 for stat in player_stats]

# print(powered_up_stats, player_stats)

#task 

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]

# character_count = [len(i) for i in avengers]
# print(character_count)

for i in avengers:
  if len(i) > 10:
    print(i)
  