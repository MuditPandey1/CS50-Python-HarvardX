n=str(input("Input: "))
output=""
for iter in n:
    match iter:
        case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U" :
            continue
    output+=iter
print(output)
            