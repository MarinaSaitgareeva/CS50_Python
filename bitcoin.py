import sys
import requests

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    elif not sys.argv[1].replace(".", "").isnumeric():
        sys.exit("Command-line argument is not a number")

    else:
        number_of_bitcoins = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        usd_rate = float(data["bpi"]["USD"]["rate"].replace(",", ""))

        print(f"${round(usd_rate * number_of_bitcoins, 4):,}")

except requests.RequestException as e:
    print(e)
