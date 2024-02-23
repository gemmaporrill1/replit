outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

#task 1
#which ones from the dictionary are outdoor activity gadgets?
# output = {"smartwatch", "drone"}

# outdoor_gadgets = []

# for activity, gadget in activity_gadgets.items():
#   if gadget in outdoor_activities:
#     outdoor_gadgets.append(activity)

# print(outdoor_gadgets)

#answer
# outdoor_gadgets = set()
# for gadget, activity in activity_gadgets.items():
#   if activity in outdoor_activities:
#     outdoor_gadgets.add(gadget)

# print(outdoor_gadgets)

# #task 2 
# #which ones are indoor gadgets

# indoor_gadgets = set()
# for activity, gadget in activity_gadgets.items():
#   if gadget in indoor_activities:
#     indoor_gadgets.add(activity)

# print(indoor_gadgets)

#task 3 | DRY 
#which ones are outdoor and indoor gadgets

#attempt
# def gadget_set(activity_gadgets):
#   for activity, gadget in activity_gadgets.items():
#     if gadget in outdoor_activities:
#       gadget_set.add(activity)
#       print(f"Outdoor gadget: {activity}")
#     else:
#       gadget_set.add(activity)
#       print(f"Indoor gadget: {activity}")
#   return gadget_set

# answer

# def getGadgetSet(activity_gadgets, activities):
#   gadgets = set()
#   for gadget, activity in activity_gadgets.items():
#     if activity in activities:
#       gadgets.add(gadget)

#   return gadgets


# print(getGadgetSet(activity_gadgets, indoor_activities))
# print(getGadgetSet(activity_gadgets, outdoor_activities))

#set comprehension for above
def getGadgetSet(activity_gadgets, activities):
  return {gadget for gadget, activity in activity_gadgets.items() if activity in activities}

print(getGadgetSet(activity_gadgets, indoor_activities))
print(getGadgetSet(activity_gadgets, outdoor_activities))