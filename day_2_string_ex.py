#find secret code and report

# message = "    🚨🔍📱🔑secret_code✌️" 
# code = 'SECRET_CODE✌️'

# key_index = message.find("🔑")

# output = message[key_index+1::].upper() #removing first index 

# if(output == code):
#   print("you are a hacker")
# else:
#   print("try again")

#task 2 
# if can't find index = -1 output


# message = "    🚨🔍📱secret_code✌️" 
# code = 'SECRET_CODE✌️'

# key_index = message.find("🔑")

# output = key_index #removing first index 

# if(output == -1):
#   print("no secret key is present")
# else:
#   print("try again")

#task 3 - remove junk
message = "    🚨🔍📱🔑****secret_code✌️((((" 
code = 'SECRET_CODE✌️'

find_key = message.find("🔑")

output = message[find_key+1::].strip("*").strip("(").upper()

if(output == code):
  print("you are a hacker")
else:
  print("try again")

#dot chaining - continue if it is a string 


