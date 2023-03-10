import pandas as pd
import requests, json
from datetime import datetime
from api_handler import BMEApiHandler


class EqwAlgo:
    
    def __init__(self, algo_tag, n_days):
        self.algo_tag = algo_tag
        self.n_days = n_days
        self.apih = BMEApiHandler()
        self.df_close = None   
    
    def get_all_data(self):
        maestro = self.apih.get_ticker_master()
        data_close_all = {}
        for _, row in maestro.iterrows():
            tck = row.ticker
            print(f"Download: {tck}", end=' ')
            close_data = self.apih.get_close_data(tck)
            data_close_all[tck] = close_data    
            df_close = pd.DataFrame(data_close_all)
        self.df_close = df_close

    def send_allocs_backtest(self):
        self.apih.delete_allocs(self.algo_tag)
        for date, data in self.df_close.iloc[::self.n_days].iterrows():
            print(date)
            tcks_activos = data.dropna().index
            alloc = 1/tcks_activos.shape[0]
            allocations_to_sent = [
                {'ticker': tck, 'alloc': alloc}
                for tck in tcks_activos
            ]
            date = date.strftime('%Y-%m-%d')
            self.apih.send_alloc(self.algo_tag, date, allocations_to_sent)
    
    def run_algo_backtest(self):
        self.get_all_data()
        self.send_allocs_backtest()
        print(apih.exec_algo(self.algo_tag))
    
    def get_result_timeout(self):
        metrics, trades = self.apih.get_exec_results(self.algo_tag)
        print(metrics)
        
    def get_allocs(self):
        self.apih.get_allocs(self.algo_tag)
        
        
    def run_day(self):          
        maestro = self.apih.get_ticker_master()
        tck_today = maestro[maestro.end_date == ''].ticker

        alloc = 1/tck_today.shape[0]
        allocations_to_sent = [
            {'ticker': tck, 'alloc': alloc}
            for tck in tck_today
        ]
        today = datetime.now()
        date = today.strftime('%Y-%m-%d')
        self.apih.send_alloc(self.algo_tag, date, allocations_to_sent)

        
        
    def run_day_comp(self):
        allocs = self.apih.get_allocs(self.algo_tag)
        last_day_alloc = pd.Timestamp(allocs.index[-1])
        
        today = datetime.now()
        days_delta = (today - last_day_alloc).days
        
        if days_delta > self.n_days:

            print('me toca rebal')     
            maestro = self.apih.get_ticker_master()
            tck_today = maestro[maestro.end_date == ''].ticker

            alloc = 1/tck_today.shape[0]
            allocations_to_sent = [
                {'ticker': tck, 'alloc': alloc}
                for tck in tck_today
            ]
            today = datetime.now()
            date = today.strftime('%Y-%m-%d')
            self.apih.send_alloc(self.algo_tag, date, allocations_to_sent)
        else:
            print('no toca')
        



