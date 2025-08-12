import requests,sys

def get_price():
    apikey = '4a51603ff2223e1187452c0ced04cf959825ce4aaf121b64a847ec6a21a5b57a'
    url = f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={apikey}'

    try:
        resp = requests.get(url)
        resp_data = resp.json()
        return float(resp_data['data']['priceUsd'])

    except (requests.RequestException,KeyError):
        print('api error')


def main():
    if len(sys.argv) == 2:
        try:
            amount = get_price() * float(sys.argv[1])

            print(f'${amount:,.4f}')

        except ValueError:
            sys.exit('Command-line argument is not a number')

    else:
        sys.exit('Missing command-line argument')

if __name__ == '__main__':
    main()
