import csv
from historical_data import Download_historical_data
import configparser
from datetime import datetime
from datetime import timedelta
import indicators
from calendar import monthrange
import database
config = configparser.ConfigParser()


class backtest(object):
    def __init__(self, symbol, interval, year, month, strategy_object):
        self.__symbol = symbol
        self.__interval = interval
        self.__year = int(year)
        self.__month = int(month)
        self.__strategy = strategy_object
        self.buys = 0
        self.sells = 0
        self.left_open = 0
        self.profit = 0
        self.avg_holding_time = 0
        self.backtest_date = datetime.now()
    
    @property
    def symbol(self):
        return self.__symbol
    @property
    def interval(self):
        return self.__interval
    @property
    def year(self):
        return self.__year
    @property
    def month(self):
        return self.__month
    @property
    def strategy(self):
        return self.__strategy
    
    def create_simulation(self):
        print(f"Running backtest with {self.strategy.name}")
        strategies = self.strategy.strats_in_use
        to_year = self.__year
        to_month = self.__month
        a_date = datetime(to_year, to_month, 1)
        longest_period = timedelta(self.strategy.Lperiod)
        days_amount = monthrange(to_year, to_month)[1]


        if self.interval in ["1m", "3m", "5m", "15m", "30m"]:
            interval = int(self.interval.replace('m', ""))
            minutes_in_month = days_amount * 1440
            candle_amount = int(minutes_in_month / interval)
            print(candle_amount, "CANDLE AMOUNT")
        elif self.interval in ['1h', '2h', '4h', '6h', '8h', '12h']:
            hours_in_month = days_amount * 24
            hour_candle_amount = hours_in_month / self.interval
        elif self.interval == "1d":
            days_in_month = days_amount * 1
            days_candle_amount = days_in_month / self.interval
        
        new_date = a_date - longest_period
        from_year = new_date.strftime("%Y")
        from_month = new_date.strftime("%m")
        print(f"Grabbing historical data from {from_year}-{from_month}/{to_year}-{to_month}")
        
        # Downloads historical data based on the setting provided from the binance and stores in a csv file.
        historical_data = Download_historical_data(self.symbol, self.interval, from_year, from_month, to_year, to_month) # Instead of a fixed year and month, make it able to grab data in a range of time.)
        
        with open("Historical_Data/backtest_data.csv") as csvfile:
            data_lines = list(csv.DictReader(csvfile, fieldnames=["row", 'date', "time", "open", "high", "low", "close", "volume"]))
        historical_data = data_lines[1:]
        
        
        # for close_candles in historical_data:
        #     print(close_candles["close"])
        
        
        for strategy in strategies:
            # for _ in range(days_amount):
                
            if strategy == "rsi":
                rsi_data = indicators.rsi(self, historical_data, candle_amount)
                for signal in rsi_data[candle_amount:]:
                    if signal["buy"] == True:
                        print("BUYBUYBUYBUYBUY")

            if strategy == "sma":
                pass
    
    
    def __str__(self):
        return f"Backtest ran on: {self.backtest_date}."

def strategy_creator():
    strategy_name = input("What is the name of the strategy: ")
    stop_loss = input("Stop loss % (Leave empty if not applicable): ")
    take_profit = input("Take profit %: ")
    database.add_strategy(strategy_name, stop_loss, take_profit)


def available_strategies():
    # TODO Grab all available strategies from the database.
    pass

def avail_indicators():
    # TODO Grab all available indicators from the database.
    pass