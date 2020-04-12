'''
Retrieve financial instrument quotes from Yahoo Finance

tickers:
world indices: see https://finance.yahoo.com/world-indices
currencies:    see https://finance.yahoo.com/currencies
commodities:   see https://finance.yahoo.com/commodities
stocks:        find symbol, and use appropriate syntax (for MSFT: MSFT/?p=MSFT)
'''

from bs4 import BeautifulSoup
import concurrent.futures as cf
import requests
import locale

class Quote():
    __slots__ = ['price', 'net', 'pct']
    def __init__(self, price, net, pct):
        self.price = price
        self.net = net
        self.pct = pct

""" retrieve price / net change / pct change for 1 symbol """
def yahoo_quote(symbol, idx=None):
    url = 'https://finance.yahoo.com/quote/' + symbol
    page = requests.get(url).text
    soup = BeautifulSoup(page, features='lxml')
    # to find all possible attributes, use:
    #spans = soup.find_all('span')
    #for span in spans:
    #    print(span.attrs, span.text)
    price = soup.find_all('span', attrs={'data-reactid': 14})[0].text
    change = soup.find_all('span', attrs={'data-reactid': 16})[0].text
    change = change.split(' ')
    price = locale.atof(price)
    net = locale.atof(change[0])
    pct = locale.atof(change[1][1:-2])
    if idx == None:
        return Quote(price, net, pct)
    else:
        return Quote(price, net, pct), idx

""" retrieve price / net change / pct change for a list of symbols """
def yahoo_quotes(symbols):
    # parallel retrieval of quotes
    n = len(symbols)
    quotes = [None] * n
    with cf.ThreadPoolExecutor() as executor:
        futures = [executor.submit(yahoo_quote, TICKER[idx], idx) for idx in range(n)]
        for future in cf.as_completed(futures):
            quote, idx = future.result()
            quotes[idx] = quote
    return quotes


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
if __name__ == "__main__":
    # retrieve 1 quote
    symbol = 'MSFT/?p=MSFT'
    quote = yahoo_quote(symbol)
    print('{} : {:.2f} ({:+.2f}, {:+.2f}%)'.format(symbol, quote.price, quote.net, quote.pct))
    
    # retrieve a list of quotes
    symbols = ['^GSPC', 'EURUSD=X']
    quotes = yahoo_quotes(symbols)
    for symbol, quote in zip(symbols, quotes):
        print('{} : {:.2f} ({:+.2f}, {:+.2f}%)'.format(symbol, quote.price, quote.net, quote.pct))
