import pandas as pd

tickers = ["TIP", "IEF", "SPY", "IWM", "VEA", "VWO", "TLT", "PDBC", "VNQ"]
_current_prices = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
_1m_ago_prices = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
_3m_ago_prices = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
_6m_ago_prices = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
_12m_ago_prices = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
return_sums = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
start_date = "2019-03-09"
end_date = "2023-03-09"

# ETF 가격 데이터 가져오기
df = pd.DataFrame()
for ticker in tickers:
  df[ticker] = pd.read_csv(f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={int(pd.Timestamp(start_date).timestamp())}&period2={int(pd.Timestamp(end_date).timestamp())}&interval=1d&events=history&includeAdjustedClose=true", index_col="Date", parse_dates=True)["Adj Close"]
  #df.to_csv("save_" + ticker +".csv")

#각 ETF의 현재 가격, 1개월 전 가격, 3개월 전 가격, 6개월 전 가격, 12개월 전 가격
for ticker in tickers:
  _current_prices[ticker] = df[ticker][-1]
  _1m_ago_prices[ticker] = df[ticker][-22]
  _3m_ago_prices[ticker] = df[ticker][-66]
  _6m_ago_prices[ticker] = df[ticker][-132]
  _12m_ago_prices[ticker] = df[ticker][-252]

print("TIP ETF current:", _current_prices['TIP'])
print("TIP ETF 12m before :", _12m_ago_prices['TIP'])

print("IEF ETF current:", _current_prices['IEF'])
print("IEF ETF 12m before :", _12m_ago_prices['IEF'])

# ETF의 최근 1개월 수익률, 최근 3개월 수익률, 최근 6개월 수익률, 최근 12개월 수익률
_1m_returns = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
_3m_returns = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
_6m_returns = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}
_12m_returns = {'TIP':0.0, 'IEF':0.0, 'SPY':0.0, 'IWM':0.0, 'VEA':0.0, 'VWO':0.0, 'TLT':0.0, "PDBC":0.0, 'VNQ':0.0}

for ticker in tickers:
  _1m_returns[ticker] = ((_current_prices[ticker] - _1m_ago_prices[ticker]) / _1m_ago_prices[ticker]) * 100
  _3m_returns[ticker] = ((_current_prices[ticker] - _3m_ago_prices[ticker]) / _3m_ago_prices[ticker]) * 100
  _6m_returns[ticker] = ((_current_prices[ticker] - _6m_ago_prices[ticker]) / _6m_ago_prices[ticker]) * 100
  _12m_returns[ticker] = ((_current_prices[ticker] - _12m_ago_prices[ticker]) / _12m_ago_prices[ticker]) * 100

#각 ETF의 최근 1개월 수익률, 최근 3개월 수익률, 최근 6개월 수익률, 최근 12개월 수익률의 합
for ticker in tickers:
  return_sums[ticker] = _1m_returns[ticker] + _3m_returns[ticker] + _6m_returns[ticker] + _12m_returns[ticker]

print("TIP ETF total Momentum score:", round(return_sums['TIP'], 2))

if return_sums['TIP']<=0:
  print("TIP의 1/3/6/12개월 모멘텀스코어가 ", round(return_sums['TIP'], 2), "이므로 현재는 하락장입니다.")
  if return_sums['IEF']>0:
    print("중기채(IEF)의 1/3/6/12개월 모멘텀스코어는", round(return_sums['IEF'], 2), "이므로 HAA 전략의 투자 자산을 중기채(IEF ETF)로 바꾸세요.")
  else:
    print("중기채(IEF)의 1/3/6/12개월 모멘텀스코어도", round(return_sums['IEF'], 2), "이므로 HAA 전략의 투자 자산을 전부 달러로 현금화 해야 합니다.")
else:
  print("TIP의 1/3/6/12개월 모멘텀스코어가 ", round(return_sums['TIP'], 2), "이므로 현재는 상승장입니다. 투자자산 ETF 8종 중에서 모멘텀 스코어 상위 4종목을 산출합니다.")
  #"IEF", "SPY", "IWM", "VEA", "VWO", "TLT", "PDBC", "VNQ"의 1/3/6/12개월 모멘텀스코어를 비교하여 상위 4종 산출하여 출력하기
  ordered_sums_list = sorted(return_sums.items(), key=lambda x:x[1], reverse=True)
  cnt = 0
  for key, value in ordered_sums_list:
    if (cnt>=4):
      break
    if (key=='TIP'):
      continue
    print(key, ":", round(value, 2))
    cnt += 1
	