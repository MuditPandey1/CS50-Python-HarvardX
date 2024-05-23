import sys
from os.path import splitext
from PIL import Image , ImageOps

file1=splitext(sys.argv[1])
file2=splitext(sys.argv[2])
images=[]

def main():
    
    check_cmd()
    
    try:
        imgfile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    shirtfile=Image.open("shirt.png")
    size=imgfile.size
    
    doodle=ImageOps.fit(imgfile, size)
    doodle.paste(shirtfile,shirtfile)
    doodle.save(sys.argv[2])
    
    
def check_cmd():
    
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if check_extension(file1[1])==False:
        sys.exit("Invalid input")
    if check_extension(file2[1])==False:
        sys.exit("Invalid output")
    if file1[1]!=file2[1]:
        sys.exit("Input and output have different extensions")

def check_extension(file):
    if file in [".jpg",".jpeg",".png"]:
        return True
    return False


      
if __name__=="__main__":
    main()