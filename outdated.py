months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    
    n=input("Date: ").capitalize()
    
    try:
        if "/" in n:
            month, date, year=map(int, n.split("/"))
            if 0<date<32 and 0< month<13:
                month="{0:02d}".format(month)
                date="{0:02d}".format(date)
                print (str(year)+"-"+str(month)+ "-"+str(date))
                break
            

        elif "," in n:
            n=n.replace(",", "")
            month, date, year=n.split(" ")
            month=months.index(month)+1
            date=int(date)
            if 0<date<32 and 0< month<13:
                month="{0:02d}".format(month)
                date="{0:02d}".format(date)
                print (str(year)+"-"+str(month)+ "-"+str(date))
                break
            
            
    except ValueError:
        continue