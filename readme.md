# Scripts to rebalance and handle my ameritrade portfolio

`python return.py` to compute return. You need to have downloaded the `balance_history.csv` using `Export history` button under balance (full history!). To see how I computed the return open `return_math.md`.

`python rebalance.py` will tell you how many stocks to buy (positive) and sell (negative) for each position according to the portfolio you define on the same script. 

I assume that you have `credentials/credentials.json` and `credentials/client_id.py`. I added some examples, but note that `credentials.json` gets modified so you shouldn't expect to have the same format.

