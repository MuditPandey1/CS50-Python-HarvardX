from working import convert
import pytest

def main():
    test_hour()
    test_minutes()
    test_raising_errors()

def test_hour():
    
    assert convert("10:30 PM to 8:50 AM")=="22:30 to 08:50"
    assert convert("10 PM to 8 AM")=="22:00 to 08:00"
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00"
    assert convert('9 AM to 5 PM')=="09:00 to 17:00"
    
def test_minutes():
    
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60")
        
def test_raising_errors():
    with pytest.raises(ValueError):
        convert("14 PM to 17 PM")
    
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

if __name__ == '__main__':
    main()
    