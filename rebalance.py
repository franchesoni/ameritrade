# Import the client
from td.client import TDClient
import numpy as np
from pathlib import Path
from credentials.client_id import client_id
credentials_path = str(Path(__file__).parent / 'credentials/credentials.json')


# follow guide here to refresh token https://developer.tdameritrade.com/content/simple-auth-local-apps if needed
# Create a new session, credentials path is required.
sess = TDClient(
    client_id=client_id,
    redirect_uri='http://localhost',
    credentials_path=credentials_path,
)
# Login to the session
sess.login()
account_info = sess.get_accounts(fields=['positions'])
assert len(account_info) == 1
account_info = account_info[0]['securitiesAccount']
positions = account_info['positions']
current_balance = account_info['currentBalances']
liquidation_value = current_balance['liquidationValue']

PORTFOLIO = {
    "cash": 0,  # cash is trash
    "mchi": 8,  # china
    "cxse": 12,  # china
    "pin": 10,  # india
    "vti": 4,  # US (5)
    "vug": 3,  # US (5)
    "vxf": 3,  # US (5)
    "scha": 4,  # US (5)
    "xlc": 1,  # US (5)
    "msft": 2,  # US  (2.5)
    "vcr": 1,  # US  (2.5)
    "esgu":2,  # US  (2.5)
    "smh": 50,  # semiconductors
    }
assert np.sum(list(PORTFOLIO.values())) == 100, f'sum is {np.sum(list(PORTFOLIO.values()))}'
percentages = {k.upper(): v / 100 for k, v in PORTFOLIO.items()}
target_amounts = {k.upper(): v * liquidation_value for k, v in percentages.items()}

simple_positions = {}
for position in positions:
    ticker = position['instrument']['symbol']
    quote = sess.get_quotes(instruments=[ticker])
    bid, ask = quote[ticker]['bidPrice'], quote[ticker]['askPrice']
    per_spread = 100 * (ask - bid) / bid
    avg_price = (bid + ask) / 2
    simple_positions[ticker] = {'price':avg_price, 'per_spread':per_spread, 'value':position['marketValue']}

    print('---'*20)
    print(ticker)
    print(f"market value: {position['marketValue']} USD with {position['longQuantity']} shares")
    print(f"current market value: {position['longQuantity'] * avg_price} USD")

print('==='*20)
to_correct = {}
for ticker in simple_positions:
    print('---'*20)
    print('correct', ticker)
    print(f"{(target_amounts[ticker] - simple_positions[ticker]['value'] ) / simple_positions[ticker]['price']} shares", f"with {simple_positions[ticker]['per_spread']}% spread")

