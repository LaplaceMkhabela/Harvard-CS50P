import emoji

def main():
    text = input('Input: ')
    output = emoji.emojize(text,language='alias')
    print(output)

if __name__ == '__main__':
    main()