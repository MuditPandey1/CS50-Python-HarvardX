def main():
    fraction=input()
    percentage=convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x,y=fraction.split("/")
            x=int(x)
            y=int(y)
            ans=x/y

            if ans<=1:
                return int (ans*100)
            else:
                fraction=input()
                pass
        except (ValueError, ZeroDivisionError):
            raise



def gauge(percentage):

    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return str(percentage) + "%"



if __name__ == "__main__":
    main()
