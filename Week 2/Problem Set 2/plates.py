import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def test1(s):
    #test if the first two characters are alphabets
    if len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha():
            return True
    else:
        return False
    
def test2(s):
    #test if the length of the string is between 2 and 6
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False
    
def test3(s):
    #test if numbers don't start with 0 or no alphabets follow ater digits
    suffix = ''
    for char in s:
        if char.isdigit():
            suffix = s[s.find(char):]
            break
    
    if suffix == '':
        return True
    elif suffix[0] != '0' and suffix.isdigit():
        return True
    else:
        return False

def test4(s):
    #test if string contains no punctuation
    for char in s:
        if char in string.punctuation:
            return False
        
    return True


def is_valid(s):
    return test1(s) and test2(s) and test3(s) and test4(s)

main()