def deep():
    answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything?')
    if (answer == '42') or (answer == 'forty two') or (answer == 'forty-two'):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    deep()