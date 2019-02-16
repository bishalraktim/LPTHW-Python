#!/usr/bin/python3.6

# Exercise 28: Boolean Practice

run = "python" == "PYthon"
print(f"The output of 'python == PYthon' is: {run}\n")

Test = 1 == 1 or 2 != 5
print(f"The output of Test is: {Test}\n")

testing = "test" == "test"
print(f"The output of 'test == test' is: {testing}\n")

find = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
print(f"The output of find is: {find}\n")

check = 3 != 4 and not ("testing" != "test" or "Python" == "Python")
print(f"The output of check is: {check}")
