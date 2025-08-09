nutrition = {
    'apple':130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 50,
    'grapes': 90,
    'honeydew': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'strawberries': 50,
    'sweet': 100,
    'tangerine': 50,
    'watermelon': 80
}

def main():
    item = input('Item: ').strip().lower()

    if item in nutrition:
        print('Calories: ',nutrition[item])
    else:
        print()

if __name__ == '__main__':
    main()