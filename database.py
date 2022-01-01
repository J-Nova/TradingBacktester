import edgedb
from datetime import datetime



def insert_chart_data(connection, data, timeframe, symbol):
    """[Inserts donwloaded data into database.]

    Args:
        connection ([connection]): [Connection to edgedb database. (Example: "edgedb.connect()")]\n
        data ([list]): [List of dictionaries. Each dictionary cointains a data point. (Example: "[{date: "date", time: "time", open: "open", etc}]")]\n
        timeframe ([str]): [timeframe of chart (Example: "5m")]\n
        symbol ([str]): [symbol of currency (Example: "BTCUSDT")]
    """    
    # Go through each row in data list and insert data into database unless it already exists in database.
    for row in data:        
        date = row['date']
        time = row['time']
        open = round(float(row['open']), 2)
        high = round(float(row['high']), 2)
        low = round(float(row['low']), 2)
        close = round(float(row['close']), 2)
        volume = float(row['volume'])
        candleid = f"{symbol}:{date}:{time}"
        insert_data = f"""
                        candleid := <str>$candleid,
                        symbol := <str>$symbol, 
                        date := <str>$date,
                        time := <str>$time,
                        open := <float64>$open, 
                        high := <float64>$high, 
                        low := <float64>$low, 
                        close := <float64>$close, 
                        volume := <float64>$volume
                        """
        insert_row = f"INSERT Chart_{timeframe} {{{insert_data}}} UNLESS CONFLICT on .candleid;"
        
        connection.query(insert_row, candleid=candleid, symbol=symbol, date=date, time=time, open=open, high=high, low=low, close=close, volume=volume)


def get_month_data(connection, symbol, interval, month, year):
    """[Selects all data filtered on date range, and specific symbol.]

    Args:
        connection ([connection]): [Connection to edgedb database. (Example: "edgedb.connect()")]\n
        symbol ([str]): [Currency to filter data on. Example: ("BTCUSDT")]\n
        interval ([str]): [Timeframe/Interval to filter data on. Example: ("5m")]\n
        month ([int]): [Month to filter data on. Example: ("05")]\n
        year ([int]): [Year to filter data on. Example: ("2021")]

    Returns:
        [list]: [list of objects containing data.]
    """    
    # Select all data filtered on date range, and specific symbol.
    month_data = connection.query(f"SELECT Chart_{interval} {{date, time, open, high, low, close, volume}} filter .date ilike '%{month}/{year}' and .symbol ilike '{symbol}';")
    return month_data




def test():
    connection = edgedb.connect()
    data = connection.query("SELECT Chart_2h {date, time, open, high, low, close, volume} filter .symbol ilike '%BTC%';")
    print(data)


def grab_chart_closing_data(connection, filter_date):
    closing_data = connection.query(f"SELECT Chart_5m {{date}} filter .date ilike '%{filter_date}' ;")
    for object in closing_data:
        print(object.date)


def add_strategy(strategy_name, description, stop_loss, take_profit):
    connection = edgedb.connect()
    date = str(datetime.now())
    
    if connection.query(f"SELECT Strategy {{}} filter .name ilike '{strategy_name}' ;"):
        return False
    else:
        insert_data = """
                    name := <str>$name, 
                    description := <str>$description,
                    stop_loss := <float64>$stop_loss,
                    take_profit := <float64>$take_profit,
                    creation_date := <str>$creation_date,
                    update_date := <str>$update_date
                """
        insert_row = f"INSERT Strategy {{{insert_data}}} UNLESS CONFLICT ON .name"
        connection.query(insert_row, name=strategy_name, description=description, stop_loss=stop_loss, take_profit=take_profit, creation_date=date, update_date = date)
        return True


def grab_all_strategies():
    connection = edgedb.connect()
    strategies = connection.query("SELECT Strategy {name, description} ;")
    connection.close()
    return strategies