import pandas as pd
from collections import Counter
path='/Users/pankaj/dev/git/nse_equity_analysis/nse_equity_analysis/moneycontrol/data/20180410/large-cap_stocks.csv'
#path='/Users/pankaj/dev/git/nse_equity_analysis/nse_equity_analysis/moneycontrol/data/20180410/small-and-mid-capstocks.csv'
#path='/Users/pankaj/dev/git/nse_equity_analysis/nse_equity_analysis/moneycontrol/data/diversified-equitystocks.csv'
#path='/Users/pankaj/dev/git/nse_equity_analysis/nse_equity_analysis/moneycontrol/data/20180410/small-and-mid-cap_stocks.csv'
large_cap=pd.read_csv(path, header=None)
secort_count=Counter(large_cap[5])
stock_counter=Counter(large_cap[0])
print(large_cap)