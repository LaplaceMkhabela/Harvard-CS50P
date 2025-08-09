def bank():
    greeting = input('Greeting: ').lower().strip()

    if greeting.find('hello') == 0:
        print('$0')
    elif greeting[0] == 'h':
        print('$20')
    else:
        print('$100')


if __name__ == '__main__':
    bank()
