import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def test1(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False
    
def test2(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return 
    
def test3(s):
    suffix = ''
    for char in s:
        if char.isdigit():
            suffix = s[s.find(char):]
    
    if suffix == '':
        return True
    elif suffix[0] != '0' and suffix.isdigit():
        return True
    else:
        return False

def test4(s):
    for char in s:
        if char in string.punctuation:
            return False
        
    return True


def is_valid(s):
    return test1(s) and test2(s) and test3(s) and test4(s)

main()