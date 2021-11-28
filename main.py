from historical_data import GetHistoricalData
import configparser
config = configparser.ConfigParser()

SELECTION = ["1", "2", "0"]

def main(config):
    while True:
        user_selection = input("What would you like to do?")
        if user_selection in SELECTION:
            break
    
    if user_selection == "1":
        symbol = config['coin']['symbol']
        interval = config['timeperiod']['interval']
        year = config['timeperiod']['year']
        month = config['timeperiod']['month']
        GetHistoricalData(symbol, interval, year, month)

if __name__ == "__main__":
    config.read('config.ini')
    main(config)