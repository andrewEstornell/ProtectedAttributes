# importing libaraies allows you to use functions from that libarary
import random as rand


# variables are dynamic (not static, so we dont need to specifty type)
random_integer = rand.randint(0, 10)
print("random integer", random_integer)

#we can also change them to be anything
# here we change random_integer from a integer to an array
random_integer = [1, 2, 3, 4]
print('random_integer is now', random_integer)

#now we change it back
random_integer = rand.randint(0, 10)


# Conditional expressions
if random_integer > 5:
    print("random_integer > 5")
elif random_integer > 3:
    print("random_integer > 3 and random_integer <= 5")
elif random_integer == 3:
    print("random_integer == 3")
else:
    print("random_integer < 3")

# forloops (ever forloop in python is techicnally a "for each loop")
# range(n) gives you unders 0, 1, 2, ..., n - 1
n = 10
for i in range(n):
    print(i)

# nested loops
for i in range(n):
    for j in range(i):
        print((i, j), end=' ') #end=' ' means the line ends with  a space rather than '\n' for a new line
    print('') # makes new line


#lists
# all 3 of these lists are the same thing
l1 = [1, 2,3]
l2 = [i for i in range(3)]
l3 = []
for i in range(3):
    l3.appen(i)
print("l1", l1)
print("l2", l2)
print("l3", l3)

# defining functions
# z is an optinal argument, if no value of z is given to the function, it defualts to z=10
def my_function(x, y, z=10):
    print(str(x) + '+' + str(y) + '+' + str(z) + '=' + str(x + y + z))

#calling function without optional argument 
my_function(1, 2)

#calling function wih optinal argument
my_function(1, 2, z=30)

