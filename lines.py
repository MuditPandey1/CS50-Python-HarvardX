import sys

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")

if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")

if ".py" not in str(sys.argv[1:]):
    sys.exit("Not a Python file")

def main():
    
    try:
        file=open(sys.argv[1],"r")
        lines=file.readlines()
        count=0
        for line in lines:
            if count_lines(line)==False:
                count+=1
        print(count)

    except FileExistsError:
        sys.argv("File does not exist")

def count_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__=="__main__":
    main()
