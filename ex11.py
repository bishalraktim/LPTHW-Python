#!/usr/bin/python3.6

# Exercise 11: Asking Questions

# print("How old are you?") # This line will tell print to end line with a new line character. 

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(' ') # print(" ") or print(' ') will print an empty line. 
print(f"so, you're {age} old, {height} tall and {weight} heavy.")
