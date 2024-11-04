import os
from pprint  import pprint

try:
    from tinkoff.invest import Client
except ModuleNotFoundError:
    from .tinkoff.invest import Client

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        # pprint(client.users.get_accounts())
        pprint(client.instruments.find_instrument())




if __name__ == "__main__":
    main()
