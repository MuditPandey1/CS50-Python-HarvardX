# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:06:46 2024

@author: MUDIT PANDEY
"""

#program promts user for arithmetic expressions which has spaces

math=input("Expression: ").strip()

#split the expression in x y and z
x=""
z=""

#for x
for i in math:
    match i:
        case "+"| "-" | "/" | "*":
            break
    x+=i

for r in math[::-1]:
    match r:
        case "+"| "-" | "/" | "*":
            break
    z+=r

p=float(x)
q=float(z[::-1])
#calculates the expressions
#outputs the floating result of the expresseon, rounded to 1 decimal place
if "+" in math:
    print (round(p+q,1))
elif "-" in math:
    print(round(p-q,1))
elif "*" in math:
    print(round(p*q,1))
elif "/" in math:
    if z!=0:
        print(round(p/q,1))
else:
    print("Seriously bruh?... You kidding me?")