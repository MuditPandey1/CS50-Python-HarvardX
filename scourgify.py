import csv
import sys

students=[]

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if ".csv" not in str(sys.argv[1:]):
    sys.exit("Not a CSV file")
    

try:
    with open(sys.argv[1],"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            name_split=row["name"].split(",")
            students.append({"first":name_split[1].lstrip(), "last":name_split[0],"house":row["house"]})
            
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2],"w") as file:
    writer=csv.DictWriter(file,fieldnames=["first","last","house"])
    writer.writerow({"first":"first", "last":"last", "house":"house"})
    for row in students:
        writer.writerow({"first":row['first'], "last":row['last'] ,"house":row['house']})
        
    