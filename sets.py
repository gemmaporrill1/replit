# string, lists, tuples, dictionary, sets -> data types
# sets - like lists it is mutable but only unique values
# no order - no guarantee

tech_gadgets = { 'smartphone', 'laptop', 'watch', 'tablet'}
print(tech_gadgets, type(tech_gadgets))

#add one item
tech_gadgets.add('e-reader')
print(tech_gadgets)


#add multiple items -. not from a dictionary tuple and lists work
more_gadgets = ["drone", 'selfie stick']
tech_gadgets.update(more_gadgets)
print(tech_gadgets)

#delete
# .remove -> error if it isn't in the set
# .discard is safer, no error when deleting if not in set
tech_gadgets.discard('drone')
tech_gadgets.discard('gimble')
print(tech_gadgets)

#empty set -> use set constructor
x = set()


#why we use sets
outdoor_activities = {'hiking', 'cycling', 'swimming'}
indoor_activities = { 'gaming', 'reading', 'cycling'}

#find common values
# displays a set -> 'cycling' * 1
print(indoor_activities.intersection(outdoor_activities)) 
print(indoor_activities.union(outdoor_activities)) #all items

#print the different items from first set perspective
print(outdoor_activities.difference(indoor_activities))
print(indoor_activities.difference(outdoor_activities))

print(indoor_activities.symmetric_difference(outdoor_activities)) #opposite to intersection


#list to set
colours = [ 'red', 'blue', 'red', 'green', 'pink', 'blue']
print(colours)
# red, blue, green, pink

#easy
colour_set = set(colours)
print(colour_set)

#hard
unique = set()
for colour in colours:
  unique.add(colour)
print(unique)

# set to list
print(list(set(colours)))

#set comprehension
x = [5, 6, 8, 9]
{num*2 for num in x }

x = [5, 6, 8, 9, 9, 3, 6] #only prints unique values
{num*2 for num in x }
