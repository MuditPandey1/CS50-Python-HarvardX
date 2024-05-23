pepsi=50
while pepsi!=0:
    n=int(input("Insert Coin: "))
    if n in [25,10,5]:
        pepsi-=n
        if pepsi>0:
            print("Amount Due: ", pepsi)
        elif pepsi<=0:
            change_owed=abs(pepsi)
            print("Change Owed: ", change_owed)
            break
    else:
        print("Amount Due: ", pepsi)
        continue
