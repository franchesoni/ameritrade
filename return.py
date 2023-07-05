# Import the client
from td.client import TDClient
import datetime
import numpy as np
from pathlib import Path
from credentials.client_id import client_id
credentials_path = str(Path(__file__).parent / 'credentials/credentials.json')


# follow guide here to refresh token https://developer.tdameritrade.com/content/simple-auth-local-apps if needed
# Create a new session, credentials path is required.
sess = TDClient(
    client_id=client_id,
    redirect_uri="http://localhost",
    credentials_path=credentials_path,
)
# Login to the session
sess.login()
# get accounts and current info
today = datetime.date.today()
account_info = sess.get_accounts(fields=["positions"])
assert len(account_info) == 1
account = account_info[0]["securitiesAccount"]
accountId = account["accountId"]
positions = account["positions"]
current_balance = account["currentBalances"]
current_amount = current_balance["liquidationValue"]

# get transactions
years = 4
transactions = []  # all transactions
for y in range(years):  # go back years
    transactions += sess.get_transactions(
        account=accountId,
        transaction_type="ALL",
        start_date=datetime.date.today() - datetime.timedelta(days=365 * (y + 1)),
        end_date=datetime.date.today() - datetime.timedelta(days=365 * y),
    )
# filter transactions to get transfers
transfers = sorted([
    (datetime.date.fromisoformat(t["settlementDate"]), t["netAmount"])
    for t in transactions
    if t["type"] in ["ELECTRONIC_FUND", "WIRE_IN"]
])
t_dates, t_amounts = list(map(list, zip(*transfers)))

# read balance history file
with open("balance_history.csv", "r") as f:
    lines = f.readlines()
header = lines[0]
entries = lines[1:-5]
endnote = lines[-5:]

balance = sorted([
    (
        datetime.datetime.strptime(
            entry.split(r'","')[0].replace(r'"', "").replace("\n", ""), "%m/%d/%Y"
        ).date(),
        float(entry.split(r'","')[1].replace(r'"', "").replace("\n", "").replace(",", ""))
    )
    for entry in entries
])
dates, amounts = list(map(list, zip(*balance)))
dates.append(today); amounts.append(current_amount)
t_dates.append(today); t_amounts.append(0)  # assume we did a transaction today

f_inds = [ind for ind, date in enumerate(dates) if date in t_dates]


rates = []
for ind in range(1, len(f_inds)):
    date_i, date_f = t_dates[ind-1], t_dates[ind]
    dT = (date_f - date_i).days
    v_ti = amounts[f_inds[ind-1]]
    v_tf = amounts[f_inds[ind]]
    f_tf = t_amounts[ind]
    abs_rate = ((v_tf - f_tf) / v_ti)  # around 1
    r_ti_tf = abs_rate ** (1 / dT) - 1
    rates.append((date_i, date_f, dT, v_ti, r_ti_tf))

    print('-'*30)
    print('dates:', date_i, date_f)
    print('time diff in days:', dT)
    print('initial amount:', v_ti)
    print('final amount:', v_tf - f_tf)
    print('abs rate:', (-1 + abs_rate) * 100)
    print('daily rate:', r_ti_tf * 100)
    print('annual rate:', ((r_ti_tf+1)**365-1) * 100)
    

dT_full = sum([r[2] for r in rates])
daily_rate = np.prod([(1+r[4])**(r[2] / dT_full) for r in rates]) - 1
annual_rate = (1 + daily_rate)**365 - 1

print('-'*30)
print('portfolio annual rate:', annual_rate)
print('-'*30)
print('absolute return:', (current_amount -  sum(t_amounts)) / sum(t_amounts))
print('initial:', sum(t_amounts))
print('final:', current_amount)



