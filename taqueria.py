menu= {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
Amount=0
while True:
    try:
        order=input("Item: ").title()
        
        if order in menu:
            Amount+=menu[order]
            Amt=("{:.2f}".format(Amount))
            price=("Total: "+"$"+str(Amt)).strip()
            print(price)        
        elif order=='Control-D':
            break
        
    except EOFError:
        break
    except KeyError:
        pass
    else:
        continue
