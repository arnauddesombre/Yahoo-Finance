# Yahoo Finance

This Python 3 script allows the efficient retrieval of quotes from Yahoo Finance.

There are 2 functions provided:

<b>yahoo_quote(symbol)</b><br>
Retrieve the real-time quote for symbol, which can be any instrument supported by Yahoo Finance.<br>
Return: 1 quote.

<b>yahoo_quotes(symbols)</b><br>
Retrieve the real-time quotes of all symbols in the list. The retrieval is parallelized using threads to allow for an efficient execution.<br>
Return: a list of quotes matching the symbols list.

Each quote is an object:
```
quote = yahoo_quote('^GSPC')  # symbol for S&P 500 (SPX)
print(quote.price, quote.net, quote.pct)  # price, net change, percentage change
```
