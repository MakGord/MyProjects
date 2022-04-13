
import requests
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
start = "2000-04-04"
end = '2022-04-12'

def get_crypto_price(symbol, start, end):
    api_url = f'https://data.messari.io/api/v1/markets/binance-{symbol}-usdt/metrics/price/time-series?start={start}&end={end}&interval=1d'
    raw = requests.get(api_url).json()
    df = pd.DataFrame(raw['data']['values'])
    df = df.rename(columns = {0:'date',1:'open',2:'high',3:'low',4:'close',5:'volume'})
    df['date'] = pd.to_datetime(df['date'], unit = 'ms')
    df = df.set_index('date')
    return df
one_n="XLU"
Master="XGD.TO"
sectors=["XLC","XLY","XLP","XLE","XLF","XLV","XLI","XLB","XLRE","XLK","XLU"]
sectors=["XLB","XLP","XLU"]
sectors=["SLV"]
#one = (yf.download(one_n,start,end,interval="1d").dropna())
Master_d = (yf.download(Master,start,end,interval="1wk").dropna()).Close


#loop
fig, ax = plt.subplots()
datf=pd.DataFrame()
for i in sectors:
    temp=(yf.download(i,start,end,interval="1wk").dropna()).Close
    datf=datf.append(temp)
    ax.plot(temp/Master_d,label=i)
    #print(datf)

ax.legend()
#one = (yf.download(one_n,start,end,interval="1d").dropna())
#two = (yf.download(two_n,start,end,interval="1d").dropna())
#df = pd.DataFrame()
#print(np.array([one.index]))
#ratio['close']=one.close/two.close
#df['close']=(one.Close/two.Close)
#df['open']=(one.Open/two.Open)
#c=c[0]

#df
#print(df)

#fig, ax = plt.subplots()
#ax.plot(df.close)
#plt.title(one_n+" / "+two_n)
plt.show()