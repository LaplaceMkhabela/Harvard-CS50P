def get_fuel():
    x,y = input('Fraction: ').strip().split('/')

    try:
        return int(x),int(y)

    except ValueError:
        raise ValueError

def calculate_fuel(x,y):
    fuel_percentage = (x/y) * 100

    if (x > y) or (x < 0) or (y < 0):
        raise ValueError

    elif fuel_percentage <= 1:
        return 'E'

    elif fuel_percentage >= 99:
        return 'F'

    else:
        if fuel_percentage - int(fuel_percentage) >= .5:
            return f'{int(fuel_percentage) + 1}%' #round up

        else:
            return f'{int(fuel_percentage)}%' #round down


def main():
    while True:
        try:
            x,y = get_fuel()
            fuel = calculate_fuel(x,y)
            break

        except (ValueError,ZeroDivisionError):
            pass

    print(fuel)

if __name__ == '__main__':
    main()
