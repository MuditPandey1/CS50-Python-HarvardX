grocery={}
while True:
    try:
        item=input().upper()
        if item=="" or item=='CONTROL-D':
            raise EOFError
        if item in grocery:
            grocery[item]+=1
        else:
            grocery[item]=1
    except EOFError:
            for iteration in sorted(grocery):
                print(grocery[iteration],iteration)
            break