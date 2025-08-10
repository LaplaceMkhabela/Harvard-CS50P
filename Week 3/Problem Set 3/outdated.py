months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def convert(date):
    if int(date['m']) > 12 or int(date['d']) > 31:
            raise ValueError

    if len(date['d']) == 1:
        date['d'] = f'0{date['d']}'

    if len(date['m']) == 1:
        date['m'] = f'0{date['m']}'

    return f'{date['y']}-{date['m']}-{date['d']}'

def get_date():
    try:
        date = input('Date: ').strip()

        if date.find('/') != -1:
            month,day,year = date.split('/')

        elif date.find(',') != -1:
            month,day,year = date.replace(',','').split(' ')
            month = f'{months.index(month.title()) + 1}'

        else:
            raise ValueError

        return {'d':day,'m':month,'y':year}

    except TypeError:
        raise TypeError


def main():
    while True:
        try:
            date = get_date()
            new_date = convert(date)
            break

        except (ValueError,TypeError):
            pass

    print(new_date)

if __name__ == '__main__':
    main()
