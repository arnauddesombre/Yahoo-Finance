# Yahoo Finance

This Python 3 script allows the retrieval of quotes from Yahoo Finance.

There are 2 functions:

<b>yahoo_quote(symbol)</b><br>
retrieve the real-time quote for symbol, which can be any instrument supported by Yahoo Finance.

<b>yahoo_quotes(symbols)</b><br>
retrieve the real-time quote of all symbols in a list, which can be any instrument supported by Yahoo Finance. The retrieval is parallelized using threads to allow for an efficient execution.

Each quote returned in an object:
```
quote = yahoo_quote('^GSPC')  # symbol for S&P 500 (SPX)
print(quote.price, quote.net, quote.pct)  # price, net change, percentage change
```
