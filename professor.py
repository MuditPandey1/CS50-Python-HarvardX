import random as r


def main():
    
    level=get_level() 
    score=user_score(level)
    print(f"Score: {score}")
    

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    
    if level==1:
        x=r.randint(0,9)
        y=r.randint(0,9)    
    elif level==2:
        x=r.randint(10,99)
        y=r.randint(10,99)
    else:
        x=r.randint(100,999)
        y=r.randint(100,999)
        
    return x,y        
        
def user_solution(x,y):
    trial=1
    while trial<=3:
        try:
            user_ans=int(input(f"{x} + {y} = "))
            if user_ans==(x+y):
                return True
            else:
                print("EEE")
                trial+=1
        except:
            print("EEE")
            trial+=1
    print(f"{x} + {y} = {x+y}")
    return False
        
def user_score(level):
    round=1
    score=0
    while round<=10:
        x,y=generate_integer(level)
        user_response=user_solution(x,y)
        if user_response==True:
            score+=1
        round+=1
    return score
        


if __name__ == "__main__":
    main()