camelCase=input("Input: ")
for c in camelCase:
    if c.islower():
        print(c, end="")
    elif c.isupper():
        print("_"+ c.lower(),end="")
        continue