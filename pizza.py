import csv
import sys
from tabulate import tabulate

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
if ".csv" not in str(sys.argv[1:]):
    sys.exit("NNot a CSV file")

def main():
    lst=[]

    try:
        with open(sys.argv[1],"r") as file:
            reader=csv.reader(file)
            for row in reader:
                lst.append(row)

    except FileNotFoundError:
        sys.argv("File does not exist")

    print(tabulate(lst[1:], headers=lst[0],tablefmt="grid"))

if __name__=="__main__":
    main()
