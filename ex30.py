#!/usr/bin/python3.6

# Exercise 30: Else and If

people = 30
cars = 40
trucks = 15

if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

if trucks > cars:
	print("That's too many trucks.")
elif trucks < cars:
	print("Maybe we could take the trucks.")
else:
	print("We still can't decide.")

if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")


# Let's try something out-of-the-box

result = trucks != cars or cars == people
if result == False:
	print("We have to think carefully now!")
else:
	print("It's up to you") 

check = 5 != 7 and not (7 == 7)

if check == True:
	print(f"The expression is: {check}")
else:
	print(f"The expression is: {check}")

print (" ")
print("We're trying something unique here!\nLet's get started!\n")

students = input("Enter the number of students: ")
teachers = input("Enter the number of teachers: ")
rooms = input("Enter the number of rooms: ")

if teachers == rooms and not (rooms != teachers):
	print("We cannot consider this at the moment!")
elif students == rooms:
	print("This should be the right decision!")
else:
	print("This is redundant!")
