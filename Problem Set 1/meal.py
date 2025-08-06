def main():
    
    time = convert(input("What  time is it?"))
    print(time)

    if (time >= 7) and (time <= 8):
        print("Breakfast time")
    elif (time >= 12) and (time <= 13):
        print('Lunch time')
    elif (time >= 18) and (time <= 19):
        print('Dinner time')
    else:
        pass


def convert(time):
    hours,minutes = time.split(':')

    return int(hours) + int(minutes)/60


if __name__ == "__main__":
    main()
