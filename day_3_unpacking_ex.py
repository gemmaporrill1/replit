#coordinates

import math

coordinates = [(5,4), (1,1), (6,10), (9,10)] #list of tuples | (x,y) coords
origin = (0,0)
o1, o2 = origin

# distances = [] #create a new list

# for x in coordinates:
#   x1, y1 = x
#   distance = math.sqrt((x1 - o1)**2 + (y1 - o2)**2)
#   distances.append(distance) #put distance into list
# print(distances) 

#task 2 
#use unpacking

# distances = [] #create a new list

# for coord in coordinates:
#   x, y = coord
#   distance = math.sqrt((x - o1)**2 + (y - o2)**2)
#   distances.append(distance) #put distance into list
# print(distances) 

# distances = [] #create a new list

# for x,y in coordinates:
#   distances.append(math.sqrt((x - o1)**2 + (y - o2)**2)) #put distance into list
# print(distances) 

#task 3 - using unpacking and list comprehension

distances = [math.sqrt((x - o1)**2 + (y - o2)**2) for x,y in coordinates]
print(distances)
