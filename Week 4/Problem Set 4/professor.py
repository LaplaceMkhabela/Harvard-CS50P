import random


def main():
    n = get_level()
    number_pairs = generate_integer(n)

    get_answers(number_pairs)



def get_level():
    while True:
        level = input('Level: ')

        try:
            level = int(level)

            if level not in [1,2,3]:
                raise ValueError
            else:
                return level

        except (TypeError,ValueError):
            pass


def generate_integer(level):
    game_pairs = []

    if level == 1:
        for i in range(20):
            game_pairs.append(random.randint(0,9))

    elif level == 2:
        for i in range(20):
            game_pairs.append(random.randint(10,99))

    elif level == 3:
        for i in range(20):
            game_pairs.append(random.randint(100,999))

    return game_pairs

def get_answers(numbers):
    score = 0
    number_pairs = []

    for i in range(0,20,2):
        number_pairs.append(tuple(numbers[i:i+2]))


    for pair in number_pairs:
        attempts = 0

        while True:
            if attempts < 3:
                ans = input(f'{pair[0]} + {pair[1]} = ')

                try:
                    ans = int(ans)

                    if ans == pair[0] + pair[1]:
                        score += 1
                        break
                    else:
                        raise ValueError

                except (TypeError,ValueError):
                    attempts += 1
                    print('EEE')

            elif attempts == 3:
                print(f'{pair[0]} + {pair[1]} = {pair[0] + pair[1]}')
                break

    print(f'Score: {score}')

if __name__ == "__main__":
    main()
