import random

while True:
    try:
        n=int(input("Level: "))
        if n>=0:
            gen_guess=random.randint(1,n)
            while True:
                try:
                    ask_guess=int(input("Guess: "))
                    if ask_guess<gen_guess:
                        print("Too small!")
                    elif ask_guess>gen_guess:
                        print("Too large!")
                    else:
                        print("Just right!")
                        break
                except ValueError:
                    continue
        break
    except ValueError:
        continue