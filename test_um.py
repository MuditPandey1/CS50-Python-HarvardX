from um import count
import pytest

def main():
    test_count_with_spaces()
    test_count_with_similar_letters()
    test_count_with_words()

def test_count_with_spaces():
    assert count("This is, um, CS50")==1
    assert count("Hello, Um, World")==1
    assert count("Um?")==1

def test_count_with_words():
    assert count("Yummy")==0
    assert count("album")==0
    assert count("um, umm")==1
def test_count_with_similar_letters():
    assert count("Thanks for the, um, album...")==1
    assert count("um? mum?")==1

if __name__ == '__main__':
    main()
    