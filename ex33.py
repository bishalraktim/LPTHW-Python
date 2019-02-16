#!/usr/bin/python3.6

# Exercise 33: While Loops

i = 0
numbers = []

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)

	i = i + 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")

print(" ")
print("The set of numbers is: ", repr(numbers))
print(f"Or the set of numbers is: {numbers}")
print(" ")

print("The numbers: ")

for num in numbers:
	print(num)



# Let's try something outside-of-the-box

print("Let's perform the above task using function.\n")



def test(num1, num2):
	print(f"At the top num1 is {num1}")
	num = num2 + 1
	print(f"At the bottom number is {num}\n")
	return num1 < num2

test1 = test(1, 9)
test2 = test(2, 19)
test3 = test(3, 29)
test4 = test(4, 39)

print(f"The result of tests is {test1}, {test2}, {test3} and {test4}\n")


print("Let's perform the task again using for loop.")

sequence = []
print(f"The sequence should be: {sequence}")

for check in range(1, 7):
	print(f"Let's add {check} to the list defined at the top of the program.")
	sequence.append(check)
	print(">>>> sequence >>>>:", repr(sequence))

print("Now let's print them out.")
for check in sequence:
	print(f" Sequence was: {check}")
