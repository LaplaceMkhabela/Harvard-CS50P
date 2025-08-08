def camel(camel_text):
    snake_case = ''
    for char in camel_text:
        if char.isupper():
            snake_case += f'_{char.lower()}'
        else:
            snake_case += char
    
    return snake_case


def main():
    input_text = input("camelCase: ")
    print("snake_case: ", camel(input_text))

if __name__ == '__main__':
    main()
