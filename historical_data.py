import wget
from zipfile import ZipFile
import os.path
import csv
import pandas as pd

def GetHistoricalData(symbol, interval, year, month):
    if not os.path.isfile(f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv"):
        url = f"https://data.binance.vision/data/spot/monthly/klines/{symbol}/{interval}/{symbol}-{interval}-{year}-{month}.zip"
        output_directory = "Historical_Data"
        filename = wget.download(url, output_directory)
        
        with ZipFile(filename, "r") as history:
            history.extractall("Historical_Data")
        os.remove(filename)
    
        with open(f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv") as historical_data:
            data_list = csv.reader(historical_data)
            print("\n")
            data_points = []
            for row in data_list:
                data_points.append(row)
        os.remove(f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv")
        df = pd.DataFrame(data_points, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
        df.dateTime = pd.to_datetime(df.dateTime, unit='ms')
        df['date'] = df.dateTime.dt.strftime("%d/%m/%Y")
        df['time'] = df.dateTime.dt.strftime("%H:%M:%S")
        df = df.drop(['dateTime', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol','takerBuyQuoteVol', 'ignore'], axis=1)
        column_names = ["date", "time", "open", "high", "low", "close", "volume"]
        df = df.reindex(columns=column_names)
        df.to_csv(f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv")
    historical_data = f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv"
    return historical_data