#assign values

# a = 10
# b = 10
# c = 10

#multiple variable assignment 
a = b = c = 10

print(a, b, c)

# one line but different variable assignment 

Lilitha, Dhara, Quinlan = "vanilla", "lime", "chocolate"

print(Lilitha, Dhara, Quinlan)

#unpacking 
movies = ["Titans", "Juno", "Lucy"]

caleb, gemma, yolanda = movies
print(gemma)

#too many values to unpack error
# t1, t2, t3 = [100, 200, 300, 400]
# print(t1, t2, t3)

#solve error
t1, t2, t3, _ = [100, 200, 300, 400] #skip last value with _
print(t1, t2, t3)

#skip 
t1, t2, _, _ = [100, 200, 300, 400] #skip last value with _
print(t1, t2)

#place all in t3 -  unpacking operator
t1, t2, *t3 = [100, 200, 300, 400, 500] 
print(t1, t2, t3) #t3 is a list

#tuple
t1, t2, *t3 = (100, 200, 300, 400, 500)
print(t1, t2, t3) #t3 is a list

#skip to the end | multiple skip
t1, t2, *_, t3 = (100, 200, 300, 400, 500, 30)
print(t1, t2, t3) #t3 is a list