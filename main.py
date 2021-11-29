from historical_data import GetHistoricalData
import configparser
import pickle
import os
from datetime import datetime
config = configparser.ConfigParser()


class strategy(object):
    def __init__(self, strategy_name, stop_loss, take_profit):
        self.name = strategy_name
        self.strats_in_use = []
        self.stop_loss = stop_loss
        self.take_profit = take_profit


    def rsi(self, period, buy, sell):
        self.rsi_period = period
        self.rsi_buy = buy
        self.rsi_sell = sell
        self.strats_in_use.append("rsi")
        
    def __str__(self):
        return(f"Strategy name: {self.name}, indicators in use: {self.strats_in_use}")

class backtest(object):
    def __init__(self, symbol, interval, year, month, strategy_object):
        self.__symbol = symbol
        self.__interval = interval
        self.__year = year
        self.__month = month
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
        pass
    
    
    def __str__(self):
        return f"Backtest ran on: {self.backtest_date}."

def config_editor(indicators):
    strategy_name = input("What is the name of the strategy: ")
    stop_loss = input("Stop loss % (Leave empty if not applicable): ")
    take_profit = input("Take profit %: ")
    strategy_config = strategy(strategy_name, stop_loss, take_profit)
    
    for indicator in indicators:
        if indicator == "rsi":
            # Prints current data for rsi indicator and asks for new settings.
            rsi_period = input("Please input your desired RSI period: ")
            rsi_buy = input("Please input your desired buy below value: ")
            rsi_sell = input("Please input your desired sell above value: ")
            strategy_config.rsi(rsi_period, rsi_buy, rsi_sell)
    
    # writes the changes to the strategy file.
    # strategy_name = strategy_name.replace(" ", "_")
    with open(f"strategies/{strategy_name}.strategy", 'wb') as configfile:
        configfile.truncate(0)
        pickle.dump(strategy_config, configfile)
    print("Saved strategy configuration\n")
    print(strategy_config)


def available_strategies():
    available_strategies = []
    directory = "strategies"
    for filename in os.scandir(directory):
        if filename.is_file():
            strategy_name, _ = os.path.splitext(filename)
            strat_name = strategy_name.split("/")[1]
            available_strategies.append(strat_name)
    return available_strategies

def main(config):
    selection = ["1", "2", "0"]
    while True:
        print("0: Exit program.\n1: Run backtest on historical data.\n2: Create or edit a strategy.")
        while True:
            user_selection = input("What would you like to do: ")
            if user_selection in selection:
                break
        
        if user_selection == "1":
            # Asks user if he wants to read settings from config or input his own settings.
            read_from_config = input("Read settings from config file: Y/N? ")
            if read_from_config.upper() in ["Y", "YES"]:
                symbol = config['coin']['symbol']
                interval = config['timeperiod']['interval']
                year = config['timeperiod']['year']
                month = config['timeperiod']['month']
            else:
                symbol = input("Symbol: Example; BTCUSDT: ")
                interval = input("Interval: Example; 5m: ")
                year = input("Year: Example; 2021: ")
                month = input("Month: Example; 09: ")
            # Downloads historical data based on the setting provided from the binance and stores in a csv file.
            historical_data = GetHistoricalData(symbol, interval, year, month)
            strats = available_strategies()
            for index, strategy in enumerate(strats):
                print(f"{index} - {strategy}")
            selected = input("Please select a strategy to use with backtesting: ")
            while not selected.isdigit() or int(selected) not in range(0, len(strats)):
                selected = input("Please select a strategy to use with backtesting: ")
                
            selected = int(selected)
            strategy = strats[selected]
            print(f"Running backtest with {strats[selected]} on {historical_data.split('/')[1]}")
            with open(f"strategies/{strategy}.strategy",'rb') as file:
                    strategy_object = pickle.load(file)
            backtest_object = backtest(symbol, interval, year, month, strategy_object)
            print(backtest_object)
            

            
        elif user_selection == "2":
            # Get all available indicators and print them.
            available_indicators = config['available_indicators']['available_indicators'].split(',')
            for index, indicator in enumerate(available_indicators):
                print(f"{index} - {indicator}")
            print("-1 ~ Exit strategy picker")
            # Asks user on which indicator to add to their strategy.
            indicators = []
            while True:
                indicator = input("Which indicators would you like to use in your strategy: ")
                # Break loop if one or more indicators are selected.
                if indicator == "-1" and len(indicators) >= 1:
                    break
                # While user input is not in available_indicators then make it input again.
                while not indicator.isdigit() or indicator.isdigit() and int(indicator) not in range(0, len(available_indicators)):
                    print("That is not a valid selection.")
                    indicator = input("For which indicator would you like to edit/create a config: ")
                
                indicator = int(indicator)
                print(f"Adding {available_indicators[indicator]} to strategy.")
                indicators.append(available_indicators[indicator])
            # Start creating the strategy object.
            config_editor(indicators)

        
        elif user_selection == "0":
            exit("Goodbye!")

if __name__ == "__main__":
    config.read('config.ini')
    main(config)