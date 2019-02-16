#!/usr/bin/python3.6

logic = """
# Exercise 27: Memorising Logic

and
or
not
!= -- not equal
== -- equal
>= -- greater-than-equal
<= -- less-than-equal
True
False


# The Truth Tables

NOT
not False -- True
not True -- False


OR
True or True -- True
False or False -- False
True or False -- True
False or True -- True


AND
True and True -- True
False and False -- False
True and False -- False
False and True -- False


NOT OR
not(True or True) -- False
not(False or False) -- True
not(True or False) -- False
not(False or True) -- False


NOT AND
not(True and True) -- False
not(False and False) -- True
not(True and False) -- True
not(False and True) -- True


!=
1 != 0 -- True
1 != 1 -- False
0 != 1 -- True
0 != 0 -- False


1 == 0 -- False
1 == 1 -- True
0 == 1 -- False
0 == 0 -- True
"""

print(logic)
