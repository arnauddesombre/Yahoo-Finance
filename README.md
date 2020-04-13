# Yahoo Finance

This Python 3 script allows the efficient retrieval of quotes from Yahoo Finance.

There are 2 functions provided:

<b>yahoo_quote(symbol)</b><br>
Retrieve the real-time quote for symbol, which can be any instrument supported by Yahoo Finance.<br>
Return: 1 quote.

<b>yahoo_quotes(symbols)</b><br>
Retrieve the real-time quotes of all symbols in the list. The retrieval is parallelized using threads to allow for an efficient execution (it takes about the same time to retrieve 1 quote or a list of quote).<br>
Return: a list of quotes matching the symbols list.

Each quote is an object:
```
quote = yahoo_quote('^GSPC')  # symbol for S&P 500 (SPX)
print(quote.price, quote.net, quote.pct)  # price, net change, percentage change
```
Note that it's easy to retrieve more attributes for a quote. Use helper function yahoo_attributes(symbol) to print all attributes available for a symbol, and update ```class Quote():``` and ```def yahoo_attributes(symbol):``` as needed.
For example, to get the volume traded, just update the class to include ```volume``` and add ```volume = soup.find_all('span', attrs={'data-reactid': 96})[0].text``` and  ```volume = locale.atof(volume)``` to the function. Be aware that not all attributes are available for all quotes.
