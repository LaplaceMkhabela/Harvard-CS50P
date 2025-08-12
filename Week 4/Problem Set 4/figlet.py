import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        text = input('in: ')
        text = figlet.figlet_format(text)

    elif len(sys.argv) == 3 and ((sys.argv[1] == '-f') or (sys.argv[1] == '--font')):
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])

            text = input('in: ')
            text = figlet.renderText(text)
        else:
            sys.exit('Invalid usage')

    else:
        sys.exit('Invalid usage')

    print(text)

if __name__ == '__main__':
    main()
