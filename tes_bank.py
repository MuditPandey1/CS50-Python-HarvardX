from test_bank import value

def main():
    test_hello()
    test_h()
    test_no_case()

def test_hello():
    assert value("hello")==0
    assert value("hello, spyder")==0

def test_h():
    assert value("hey")==20
    assert value("how you doing?")==20

def test_no_case():
    assert value("What's up?")==100

if __name__=="__main__":
    main()