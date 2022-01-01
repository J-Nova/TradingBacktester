import wget
from zipfile import ZipFile
import os.path
import csv
import pandas as pd
from datetime import datetime
import calendar
from database import insert_chart_data
import urllib.request


def Download_historical_data(connection, symbol, interval, month, year):
    """[Downloads historical data from binance servers.]
    
    Args:
        connection ([connection]): [Connection to edgedb database. (Example: "edgedb.connect()")]\n
        symbol ([str]): [Currency to download data on. Example: ("BTCUSDT")]\n
        interval ([str]): [Timeframe/Interval to download data on. Example: ("5m")]\n
        month ([int]): [Month to download data on. Example: ("05")]\n
        year ([int]): [Year to download data on. Example: ("2021")]
    """    
    today = int(datetime.now().strftime("%d"))-1
    # Check if current day data exists in database, otherwise download data.
    if connection.query(f"SELECT Chart_{interval} {{}} filter .date ilike '{today}/{month}/{year}' and .symbol ilike '{symbol}';"):
        return True
    else:
        num_days = calendar.monthrange(year, month)[1]
        
        # Check if month and year are equal to current date. ifso set num_days to the current previous day.
        if month == int(datetime.now().strftime("%m")) and year == int(datetime.now().strftime("%Y")):
            num_days = int(datetime.now().strftime("%d"))-1
        
        if int(month) < 10:
            month =  "0"+str(month)
        
        data_points = []
        
        for day in range(1, num_days+1):
            if day < 10:
                day = "0"+str(day)
                
            url = f"https://data.binance.vision/data/spot/daily/klines/{symbol}/{interval}/{symbol}-{interval}-{year}-{month}-{day}.zip"
            output_directory = "Historical_Data"
            
            try:
                # Download zip file and extract its data after extraction remove downloaded zip file.
                filename = wget.download(url, output_directory)
                with ZipFile(filename, "r") as history:
                    history.extractall(output_directory)
                os.remove(filename)

                # Append all rows in extracted csv file and append them to data_points and remove csv file afterwards.
                with open(f"Historical_Data/{symbol}-{interval}-{year}-{month}-{day}.csv") as historical_data:
                    data_list = csv.reader(historical_data)
                    for row in data_list:
                        data_points.append(row)
                os.remove(f"Historical_Data/{symbol}-{interval}-{year}-{month}-{day}.csv")
            # If the url is not found, then switch over to download the full month of data.
            except urllib.error.HTTPError:
                # Clear all previous appended data points.
                data_points = []
                
                url = f"https://data.binance.vision/data/spot/monthly/klines/{symbol}/{interval}/{symbol}-{interval}-{year}-{month}.zip"
                filename = wget.download(url, output_directory)
                with ZipFile(filename, "r") as history:
                    history.extractall("Historical_Data")
                os.remove(filename)
                
                with open(f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv") as historical_data:
                    data_list = csv.reader(historical_data)
                    for row in data_list:
                        data_points.append(row)
                os.remove(f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv")
                break
        
        # Create a pandas DataFrame from the data points into a csv file.
        df = pd.DataFrame(data_points, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
        df.dateTime = pd.to_datetime(df.dateTime, unit='ms')
        df['date'] = df.dateTime.dt.strftime("%d/%m/%Y")
        df['time'] = df.dateTime.dt.strftime("%H:%M:%S")
        df = df.drop(['dateTime', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol','takerBuyQuoteVol', 'ignore'], axis=1)
        column_names = ["date", "time", "open", "high", "low", "close", "volume"]
        df = df.reindex(columns=column_names)
        df.to_csv(f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv")
        
        # Open created csv file and read in each row into a list.
        with open(f"Historical_Data/{symbol}-{interval}-{year}-{month}.csv") as csvfile:
            data_lines = list(csv.DictReader(csvfile, fieldnames=["row", "date", "time", "open", "high", "low", "close", "volume"]))
        historical_data = data_lines[1:]
        
        # Insert data into the database.
        insert_chart_data(connection, historical_data, interval, symbol)
        return True

# GetHistoricalData(edgedb.connect(), "BTCUSDT", "30m", 12, 2021)