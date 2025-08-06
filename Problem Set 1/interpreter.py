def interpreter():
    x,y,z = input('Expression: ').split(' ')
    x = int(x)
    z = int(z)
    
    match(y):
        case '+':
            result = x+z
        case '-':
            result = x-z
        case '*':
            result = x*z
        case '/':
            result = x/z

    return round(float(result),1)


if __name__ == '__main__':
    output = interpreter()
    print(output)