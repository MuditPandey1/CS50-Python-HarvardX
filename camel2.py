def main():
    user_inp=str(input("camelCase: ")).strip()
    output=""
    snake_case(user_inp, output)
    ans=snake_case(user_inp,output).lower()
    print(ans)
def snake_case(user_inp, output):
    for c in user_inp:
        if c.islower():
            output+=c
        elif c.isupper():
            output+="_"+c
    return output
main()