#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

x = float(input("enter a number"))
xp = x/6
xd = x/8
xP = int(xp)
xD = int(xd)
XP = xp - xP
XD = xd - xD
if XP == 0 and XD == 0:
    print(f"{x} is not frue")
elif XD == 0:
    print(f"{x} is not frue")
elif XP == 0:
    print(f"{x} is frue")
else:
    print(f"{x} is not frue")