#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
You will need to use a logical statement that checks to see if any of the names
matches the input name.  Don't be surprised if there are many and/or connectors.

(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile")
VIPNames = ("Blanka")
VIPNames = ("Christine")
VIPNames = ("Carol")
VIPNames = ("Richard")
VIPNames = ("Daniel")
VIPNames = ("Chun-Li")

x = input("Enter your name=>")

if x == VIPNames:
    print(f"Hi {x}, You are VIP!")
elif x != VIPNames:
    print(f"why are you here {x}, you werent invited")