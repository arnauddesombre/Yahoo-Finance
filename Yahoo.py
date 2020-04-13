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

""" helper function, find attributes available for a quote """
def yahoo_attributes(symbol):
    url = 'https://finance.yahoo.com/quote/' + symbol
    page = requests.get(url).text
    soup = BeautifulSoup(page, features='lxml')
    spans = soup.find_all('span')
    for span in spans:
        print(span.attrs, span.text)

""" retrieve price / net change / pct change for 1 symbol """
def yahoo_quote(symbol, idx=None):
    url = 'https://finance.yahoo.com/quote/' + symbol
    page = requests.get(url).text
    soup = BeautifulSoup(page, features='lxml')
    price = soup.find_all('span', attrs={'data-reactid': 14})[0].text
    price = locale.atof(price)
    change = soup.find_all('span', attrs={'data-reactid': 16})[0].text
    net, pct = change.split(' ')
    net = locale.atof(net)
    pct = locale.atof(pct[1:-2])
    if idx == None:
        return Quote(price, net, pct)
    else:
        return Quote(price, net, pct), idx

""" retrieve price / net change / pct change for a list of symbols """
def yahoo_quotes(symbols):
    n = len(symbols)
    quotes = [None] * n
    # parallel retrieval of quotes
    with cf.ThreadPoolExecutor() as executor:
        futures = [executor.submit(yahoo_quote, symbols[idx], idx) for idx in range(n)]
        for future in cf.as_completed(futures):
            quote, idx = future.result()
            quotes[idx] = quote
    return quotes


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
if __name__ == "__main__":
    # print all available attributes
    symbol = 'IBM/?p=IBM'
    yahoo_attributes(symbol)
    print()

    # retrieve and print 1 quote
    symbol = 'MSFT/?p=MSFT'
    quote = yahoo_quote(symbol)
    print('{} : {:.2f} ({:+.2f}, {:+.2f}%)'.format(symbol, quote.price, quote.net, quote.pct))
    print()
    
    # retrieve and print a list of quotes
    symbols = ['^GSPC', 'EURUSD=X', 'GC=F']
    quotes = yahoo_quotes(symbols)
    for symbol, quote in zip(symbols, quotes):
        print('{} : {:.2f} ({:+.2f}, {:+.2f}%)'.format(symbol, quote.price, quote.net, quote.pct))
