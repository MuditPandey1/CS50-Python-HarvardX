import inflect

p = inflect.engine()

lst=[]

while True:
    n=input("Name: ")
    try:
        if n!="":
            lst.append(n)
        else:
            mylist=p.join(lst)
            print("Adieu, adieu, to", mylist)
            break
        
    except EOFError:
        break
