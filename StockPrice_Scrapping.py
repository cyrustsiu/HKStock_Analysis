import requests
import bs4

def getStockPrice(num):

    url = 'http://www.aastocks.com/en/stocks/quote/detail-quote.aspx?symbol={}'.format(num)
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89",

    "Referer": "http://www.aastocks.com/en/stocks/quote/detail-quote.aspx"
    }
    
    res = requests.get(url, headers = headers)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    title = soup.select('.quote #cp_ucStockBar_litInd_StockName')[0].text
    price = soup.select('.content #labelLast span')[0].text.strip(" \xa0")    
    
    return (title + "(" + num + ")" + " : " +price)


#input your wanted stock number
stockList = ['00700','0005','0066']

#list stock price
for stockNum in stockList:
    print(getStockPrice(stockNum))
