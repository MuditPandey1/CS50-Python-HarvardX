from twttr import shorten

def main():
    case_letter()
    number()
    punc()

def case_letter():
    assert shorten("Twitter")=="Twttr"
    assert shorten("TWITTER")=="TWTTR"
    assert shorten("twitter")=="twttr"
    assert shorten("Water")=="wafjg"

def number():
    assert shorten("87966")=="87966"

def punc():
    assert shorten("?.!")=="?.!"

if __name__ == "__main__":
    main()

