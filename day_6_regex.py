import re

# Regex -> Regular expression

# Pattern match in a string 

# they have 16 digits
# start with 4

# 1. search
# 2. findAll
# 3. sub

quote = 'To be or not to be'

# r -> raw
# search 

findBe = re.search(r'be$', quote) # if not present, it returns None
# if present, it returns a match object 're match'

output = "Present" if findBe else "Not present"

print(findBe)
print(output)

# findall

find_be = re.findall(r'be', quote) 
print(find_be)

# more complex
quote1 = "funny funy funnny fuzzy"
find_fun = re.findall(r'fun{2,}y', quote1) # give regex inside 
# will give you all the matches
print(find_fun)

# why we use r(raw)

text = "This \\ that \\ those"

matches = re.findall('\\\\', text) #two matches
# raw string dn't need to escaping (no slash needed)
matches_r = re.findall(r'\\', text) 

print(matches)
print(matches_r)

# sub example

tweet = "Spoiler: This movie is great, but the spoiler was unexpected. Avoid sharing spoilers!"

censor_tweet = re.sub(r'spoiler', "*" * 7, tweet, flags = re.IGNORECASE)
print(censor_tweet)

# capture groups

website_list = "google.com, yahoo.com, facebook.com, twitter.com"

result = re.sub(r'(\w+)\.com', 'blacklist.com', website_list)
result1 = re.sub(r'(\w+)(\.com)', r'\1.net', website_list)
print(result1)

# r'\2 \1.net' | moves strings around 
