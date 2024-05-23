import re
from numb3r import validate

def main():
    test_format()
    test_range()
    
def test_format():
    assert validate(r"1.2.3")==False
    assert validate(r"1.258.369.98.50")==False
    assert validate(r"1.2.3.4")==True
    assert validate(r"255.255.255.255")==True
    assert validate(r"1")==False
    assert validate(r"4.5")==False

def test_range():
    assert validate(r"255.255.255.255")==True
    assert validate(r"512.512.512.512")==False
    assert validate(r"1.2.235.36")==True   
    assert validate(r"255.1.23.1000")==False
    
if __name__ == '__main__':
    main()
    
    