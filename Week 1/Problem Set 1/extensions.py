def extensions(file_name):
    images = ['gif','jpg','jpeg','png']

    extension = ''

    dots = file_name.count('.')

    for char in file_name.strip().lower():
        if dots == 0:
            extension += char

        if char == '.':
            dots -= 1


    if extension in images:
        if extension == 'jpg':
            return 'image/jpeg'
        else:
            return f'image/{extension}'

    elif extension == 'pdf' or extension == 'zip':
        return f'application/{extension}'

    elif extension == 'txt':
        return f'text/plain'

    else:
        return 'application/octet-stream'

def main():
    file_name = input('File Name: ')
    print(extensions(file_name))

if __name__ == '__main__':
    main()
