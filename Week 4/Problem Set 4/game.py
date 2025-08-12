from random import randint

def get_guess(randon_number):
    while True:
        try:
            guess = input('Guess: ')
            guess = int(guess)

            if guess == randon_number:
                print('Just right!')
                break
            elif guess >= 0 and guess < randon_number:
                print('Too small!')
            elif guess > randon_number:
                print('Too large!')

        except (TypeError,ValueError):
            pass


def get_level():
    while True:
        n = input('Level: ')

        try:
            n = int(n)

            if n < 0:
                raise ValueError
            else:
                return randint(1,n)

        except (TypeError,ValueError):
            pass

def main():
    mystery_number = get_level()
    get_guess(mystery_number)

if __name__ == '__main__':
    main()
