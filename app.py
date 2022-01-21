from flask import Flask, render_template, request, session, g
import edgedb
import historical_data as HDATA
import database as DB

app = Flask(__name__)
app.debug = True
app.config['TESTING'] = True
app.testing = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "SECRET_PROJECT_123"
#export FLASK_ENV=development

ALLOWED_TIMEFRAMES = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "1d"]
ALLOWED_COINS = ["BTCUSDT", "ETHUSDT", "ADAUSDT"]
AVAILABLE_INDICATORS = [{"name": "SMA", "description": "Simple moving average"}, {"name": "RSI", "description": "Relative Strenght Index"}]

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/historical/data", methods=["GET", "POST"])
def historical_data():
    base = request.form.get('historical_candle_data')
    if base != "candle-data":
        return render_template('historical_data.html', timeframes=ALLOWED_TIMEFRAMES, symbols=ALLOWED_COINS)
    else:
        symbol = request.form.get('symbol')
        interval = request.form.get('timeframe')
        daterange = request.form.get('data-range').split("-")
        month = int(daterange[1])
        year = int(daterange[0])
        
        # Create a connection to the database
        connection = edgedb.connect()
        
        #Check if selected date range exist in database, ifnot then download all data and import into the database.
        HDATA.Download_historical_data(connection, symbol, interval, month, year)
        
        # Fetch all data filtered on the selected date range.
        data = DB.get_month_data(connection, symbol, interval, month, year)
        
        # Close the connection to the database.
        connection.close()
        
        return render_template('historical_data.html', data=data)


@app.errorhandler(404)
def not_found(_):
    return render_template('404.html')

@app.route("/strategies", methods=["GET"])
def strategies():
    strategies = DB.grab_all_strategies()
    return render_template('strategies.html', strategies=strategies)


@app.route("/strategy/<name>")
def strategy_editor(name):
    pass

@app.route("/create/strategy", methods=["GET", "POST"])
def strategy_creation():
    # Todo 1. create appropriate html file for creating a strategy.
    # Todo 2. create strategy creator function in seperate strategy.py file.
    # Todo 3. create proper strategy importing to edgedb database.
    if request.method == "POST":
        strategy_name = request.form.get('strategy-name')
        description = request.form.get('strategy-description')
        stop_loss = float(request.form.get('strategy-stop-loss'))
        take_profit = float(request.form.get('strategy-take-profit'))
        success = DB.add_strategy(strategy_name, description, stop_loss, take_profit)
        if not success:
            return render_template('strategy_creation.html', error="A strategy with the same name already exists", available_indicators=AVAILABLE_INDICATORS)
        elif success:
            return render_template('strategies.html', strategies=DB.grab_all_strategies())

    elif request.method == "GET":
        return render_template('strategy_creation.html', available_indicators=AVAILABLE_INDICATORS)
    

if __name__ == '__main__':
    app.run(debug=True)
