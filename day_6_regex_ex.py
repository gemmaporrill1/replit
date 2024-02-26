import re

# names array
names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans"]
# output = 

for name in names:
  name_shuffle = [re.sub(r'(\w+)\s*(\w+)', r'\2, \1', name)]
  print(name_shuffle)

# Assignment
post = "Loving the #sunny weather in #California. #travel #fun"

# Output
# ['#sunny', '#California', '#travel', '#fun']

hash_tag = re.findall(r'(#\w+)', post)
print(hash_tag)