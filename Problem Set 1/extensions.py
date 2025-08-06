def extensions():
    images = ['gif','jpg','jpeg','png']

    file_name = input('File Name: ')
    extension = file_name[file_name.find('.')+1:]
    
    if extension in images:
        return f'image/{extension}'
    elif extension == 'pdf' or extension == 'zip':
        return f'application/{extension}'
    elif extension == 'txt':
        return f'text/plain'
    



if __name__ == '__main__':
    output = extensions()
    print(output)