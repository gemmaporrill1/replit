import re

# Assignment
post = "Loving the #sunny weather in #California. #travel #fun"

# Output
# ['#sunny', '#California', '#travel', '#fun']

hash_tag = re.findall(r'(#\w+)', post)
print(hash_tag)