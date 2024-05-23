from pyfiglet import Figlet
import sys
import random

figlet=Figlet()
figlet.getFonts()

if len(sys.argv)==1:
        get_txt=input("Input: ")
        font=random.choice(figlet.getFonts())
        print(figlet.renderText(get_txt))

elif len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[1]=='--font'):

    try:
        figlet.setFont(font=sys.argv[2])
        get_txt=input("Input: ")
        print(figlet.renderText(get_txt))

    except:
        print("Invalid usage")
        sys.exit(1)

else:
    sys.exit("Invalid usage")
    
    #Get to work with the libraries
    