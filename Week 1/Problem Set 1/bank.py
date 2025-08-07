def bank():
    greeting = input('Greeting: ')
    prefix = greeting[:1]
    
    if greeting.lower() == 'hello':
        print('$0')
    elif prefix.lower() == 'h':
        print('$20')
    else:
        print('$100')


if __name__ == '__main__':
    bank()