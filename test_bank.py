def main():
    greeting=input("Greetings gentleman: ").lower()
    val=value(greeting)
    print ("$", val)


def value(greeting):
    substring=greeting[0:1]
    if "hello" in greeting:
        return 0
    elif substring=="h":
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()
