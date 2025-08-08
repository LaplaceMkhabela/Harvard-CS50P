def coke():
    paid = 0
    due = 50
    denominations = [5,10,25]

    while paid < 50:
        print(f'Amount Due: {due - paid}')
        coin = int(input('Insert Coin: '))

        if coin in denominations:
            paid += coin

    print(f'Changed Owed: {paid - due}')
    

if __name__ == '__main__':
    coke()
