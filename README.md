# Yahoo Finance

This Python 3 script allows the efficient retrieval of quotes from Yahoo Finance.

There are 2 functions provided:

<b>yahoo_quote(<i>symbol</i>)</b><br>
Retrieve the real-time quote for <i>symbol</i>, which can be any instrument supported by Yahoo Finance.<br>
Return: 1 quote.

<b>yahoo_quotes(<i>symbols</i>)</b><br>
Retrieve the real-time quotes of all <i>symbols</i> in the list. The retrieval is parallelized using threads to allow for an efficient execution (it takes about the same time to retrieve 1 quote or a list of quote).<br>
Return: a list of quotes matching the <i>symbols</i> list.

Each quote returned is an object:
```
quote = yahoo_quote('^GSPC')  # symbol for S&P 500 (SPX)
print(quote.price, quote.net, quote.pct)  # price, net change, percentage change
```
It is very easy to update the code to retrieve more attributes for a quote. Use helper function <b>yahoo_attributes(<i>symbol</i>)</b> to print all attributes available for a particular <i>symbol</i>, and update ```class Quote()``` and ```def yahoo_attributes(symbol)``` as needed.
For example, to get the volume traded, update the class to include ```volume``` and update the function to include:
```
volume = soup.find_all('span', attrs={'data-reactid': 96})[0].text
volume = locale.atof(volume)
...
return Quote(price, net, pct, volume)
```
Be aware that not all attributes are available for all quotes. If you include the volume in your class Quote(), ```yahoo_quote('^GSPC')``` will throw an error as volume is not available for the S&P 500.
