def main():
    time=input("time: ").strip()
    catchVariable=convert(time) #function calling
    if 7.0<=catchVariable<=8.0:
        print("breakfast time")
    if 12.0<=catchVariable<=13.0:
        print("lunch time")
    if 18.0<=catchVariable<=19.0: #using variable like a mathematical functions
        print("dinner time")
def convert(time):
    if ":" in time:
        hour,minutes=time.split(":")
        minutes=float(minutes) #conversion done always right to left
        mini=minutes/60
        hou=int(hour)
        res=hou+mini
        return res #returning the value
if __name__ == "__main__":
    main()
