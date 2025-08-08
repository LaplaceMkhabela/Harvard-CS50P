def remove_vowels(text):
    output = ''
    vowels = ['a','e','i','o','u']

    for char in text:
        if char.lower() not in vowels:
            output += char

    return output


def main():
    input_text = input('Input: ')
    print('Output: ',remove_vowels(input_text))

if __name__ == '__main__':
    main()