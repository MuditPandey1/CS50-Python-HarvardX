from plates import is_valid

def main():
    
    test_start_letters()
    test_length_check()
    test_num_at_end()
    test_no_punctuation()
    
    
def test_start_letters():
    assert is_valid("A123LP")==False
    assert is_valid("!@456P")==False    
    assert is_valid("AAA666")==True
    
def test_length_check():
    assert is_valid("AA")==False
    assert is_valid("AAA123")==True 
    
def test_num_at_end():
    assert is_valid("AA12AA")==False
    assert is_valid("AWQ123")==True
    
def test_zero():
    assert is_valid("CS05")==False
    assert is_valid("CS50")==True

def test_no_punctuation():
    assert is_valid("PI3.14")==False
    assert is_valid("QWR123")==True
    
    
if __name__=="__main__":
    main()