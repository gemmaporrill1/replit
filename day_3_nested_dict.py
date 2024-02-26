person = {
  "name": "Siya Kolisi",
  "age": 32,
  "address": {
    "city": "Port Elizabeth",
    "country": "SA",
  }, 
  # "stats": {
  #             "points": 50,
  #          },
  "sport": "Rugby",
  "height": 186
}

print(person["address"]["city"])


#if no stats dictionary | error handling 
print(person.get('stats')) #none output

#attribute error "NoneType" object has no attribute 'get'

print(person.get('stats', {})) #{} output

print(person.get('stats', {}).get('points')) #none output

#Dictionary Comprehension

#what should be the key: value
# nums = {x: x for x in range(10)}
# print(nums)

# #verything in list comprehension also works in dictionary comprehension

# nums = {x: x ** 2 for x in range(10) if x % 2 == 0} | returns a dictionary
# print(nums)

#when index matters
nums = [90, 50, 80]

for num in enumerate(nums):
  print(num)

#old way of doing things
for idx in range(len(nums)):
  print(idx, nums[idx])

for idx, num in enumerate(nums): #give index and vlaue
  print(idx, num)

print(list(enumerate(nums))) #list of tuples 