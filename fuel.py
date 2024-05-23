while True:
    n=input("Fraction: ")
    if "/" in n:
        x,y=n.split("/")
        if x.isdigit() and y.isdigit():
            x=int(x)
            y=int(y)
            if x<=y and y!=0:
                try:
                    p=int(round((x/y)*100,0))
                    if p<=1:
                        print("E")
                        break
                    elif p>=99:
                        print("F")
                        break
                    else:
                        print(str(p)+"%")
                        break
                except (ValueError, ZeroDivisionError):
                    continue
            else:
                raise ValueError
        else:
            continue
    else:
        continue