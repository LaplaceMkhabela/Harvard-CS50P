import inflect

def get_names():
    names = []
    while True:
        try:
            name = input('Name: ')
            names.append(name)

        except EOFError:
            break
    return names


def main():
    names = get_names()

    p = inflect.engine()

    print('\nAdieu, adieu, to ' + p.join(names))

if __name__ == '__main__':
    main()