#Lists
#Mutable

# marks = [98, 75, 40, 80, 90, 45, 80, 60]
# print(type(marks))
# marks.pop(2) # 2nd index removed pop changes original array
# print(marks)

#slice - no mutation
# [::-1] last index and reverse
# #marks[start_idx:end_idx]

# print(marks[:-3]) #removing the last three values from the list slice doesn't change the original array
# print(marks)

#remove 40 from the list
# marks.remove(40) #mutation as original array is changed
# print(marks)

# eng = 100
# marks.append(eng) #append adds the value to the end of the list, mutation
# print(marks)

# sci = 76
# marks.insert(0, sci)
# print(marks)

pricelist1 = [1000, 1500, 400]
# pricelist2 = [2000, 500]

# print(pricelist1 + pricelist2) # add lists together no mutation | New copy
# print(pricelist1, pricelist2) #no mutation 

# print([5, 6] * 2) # [5, 6, 5, 6]

# # copy = pricelist1.copy() #copying the list

# # Copy
# copy = pricelist1

# print(copy.append(600))
# print(pricelist1.append(700)) # point to the same place in memeory
# print(pricelist2.append(800))

# print(copy, pricelist1, pricelist2)

# storing the memory address of the first item
# address => 456 + 0 
# 456 + 1 
# stores in continuous location 

#slice -> copy

pricelistcopy = pricelist1[:]

print(pricelist1.append(700)) # point to the same place in memeory
print(pricelistcopy.append(800))

print(pricelist1, pricelistcopy)

print(id(pricelist1), id(pricelistcopy)) # check different addresses

# which item is removed
pricelist1.remove(1000)

#joining 

subjects = ["maths", "science", "english" ] 

print(', '.join(subjects))

#sorting  -> mutable
subjects.sort()
print(subjects)

#reverse order
subjects.sort(reverse=True)
print(subjects)



