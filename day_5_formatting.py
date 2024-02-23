from math import pi
from datetime import datetime 

salary = 420_000_000 #DX
print(salary)

#number fortmatting
print(f"My salary is R{salary:,}")
print(f"My salary is R{salary:_}")

#float formatiing
print(f"The PI value is: {pi:.2f}") # floating points

#format text

name = "Gemma"
person = "Siya"
print(f"My name is {name:>10}")
print(f"My name is {name:<10}")
print(f"My name is {name:^10}") #centre

print(f"My name is {person:*>10}")
print(f"My name is {person:#<10}")
print(f"My name is {person:$^10}")

caleb = 0.925
print(f'The test results are out and Caleb got {caleb:.2%}')

#dates
#current time

now = datetime.now()
print(f'The current date is: {now:%d-%m-%Y}')
print(f'The current date is: {now:%d/%m/%Y}')