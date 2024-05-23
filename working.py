import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    
    match=re.search(r"([0-9][0-2]*):*([0-5][0-9])* ([A-P]M) to ([0-9][0-2]*)*:*([0-5][0-9]*)* ([A-P]M)",s) 
    if match:
        list=match.groups() 
        if int(list[0])>12 or int(list[3])>12:
           raise ValueError
        time1=match_pattern(list[0],list[1],list[2])
        time2=match_pattern(list[3],list[4],list[5])
        return time1 +" to "+ time2
    else:
        raise ValueError
    
def match_pattern(hour, minute, time):
    if time=="PM":
        if int(hour)==12:
            new_hour=12
        else:
            new_hour=12+int(hour)
    else:
        if int(hour)==12:
            new_hour=0
        else:
            new_hour=int(hour)
            
    if minute==None:
        new_minute="00"
        new_time=f"{new_hour:02}" +":"+ new_minute
    else:
        new_time=f"{new_hour:02}"+":" + minute
        
    return new_time
        
        

if __name__ == "__main__":
    main()