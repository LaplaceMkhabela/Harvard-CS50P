grocery_list = dict()

def add_item():
    items = []
    items = input().strip().upper().split('and')

    for item in items:
        if item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1

        else:
            grocery_list[item] = 1

def print_list():

    for item in sorted(grocery_list):
        print(grocery_list[item],item)

def main():
    while True:
        try:
            add_item()

        except KeyError:
            pass

        except EOFError:
            break

    print_list()

if __name__ == '__main__':
        main()
