import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    if re.search(r"^[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]+$",ip):
        numbers=ip.split(".")
        for iter in numbers:
            if int(iter) <0 or int(iter)>255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()