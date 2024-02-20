#Lists
#Mutable

marks = [98, 75, 40, 80, 90, 45, 80, 60]
# print(type(marks))
# marks.pop(2) # 2nd index removed pop changes original array
# print(marks)

# #marks[start_idx:end_idx]

# print(marks[:-3]) #removing the last three values from the list slice doesn't change the original array
# print(marks)

#remove 40 from the list
marks.remove(40)
print(marks)