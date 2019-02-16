#!/usr/bin/python3.6

# Exercise 32: Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print(f"This is count {number}")

# the same as above
for fruit in fruits:
	print(f"A fruit of types: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
	print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6): # range (1, 5) = (1, 2, 3, 4)
	print(f"Adding {i} to the list.")
	# append is a function that lists understand
	elements.append(i)

print(" ")
print(">>>>>>> elements =", repr(elements))

# now we can print them out too
for i in elements:
	print(f"Element was: {i}") 

print(" ")

# Let's try something outside-of-the-box
print("Here's a different scenario")

for test in range(1, 5):
	print(f"The output will be: {test}")

print(" ")
	
for check in range(0, 4):
	fruits.append(check)
	print(f"Again, the another output will be: {fruits}")
