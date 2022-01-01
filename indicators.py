def rsi(self, historical_data, candle_amount):
    
    close_prices = []
    for row in historical_data:
        close_prices.append(round(float(row['close']), 2))
    # Needs closing candle data.
    window_length = int(self.strategy.rsi_period)
    rsi_sell_signal = float(self.strategy.rsi_sell)
    rsi_buy_signal = float(self.strategy.rsi_buy)
        # Define containers
    gains = []
    losses = []
    window = []

    # Define convenience variables
    prev_avg_gain = None
    prev_avg_loss = None

    rsi_output = []

    # Define output container with header
    output = [
        ['date', 'close', 'gain', 'loss', 'avg_gain', 'avg_loss', 'rsi']
    ]
    for i, price in enumerate(close_prices):

        # Skip first row but remember price
        if i == 0:
            window.append(price)
            output.append([i+1, price, 0, 0, 0, 0, 0])
            continue

        # Calculate price difference with previous period
        difference = round(close_prices[i] - close_prices[i - 1], 2)

        # Record positive differences as gains, negative as losses
        if difference > 0:
            gain = abs(difference)
            loss = 0
        elif difference < 0:
            gain = 0
            loss = abs(difference)
        else:
            gain = 0
            loss = 0
        gains.append(gain)
        losses.append(loss)

        # Don't calculate averages until n-periods data available
        if i < window_length:
            window.append(price)
            output.append([i+1, price, gain, loss, 0, 0, 0])
            continue

        # Calculate Average for first gain as SMA
        if i == window_length:
            avg_gain = sum(gains) / len(gains)
            avg_loss = sum(losses) / len(losses)

        # Use WSM after initial window-length period
        else:
            avg_gain = (prev_avg_gain * (window_length - 1) + gain) / window_length
            avg_loss = (prev_avg_loss * (window_length - 1) + loss) / window_length

        # Round for precision
        avg_gain = round(avg_gain, 2)
        avg_loss = round(avg_loss, 2)

        # Keep in memory
        prev_avg_gain = avg_gain
        prev_avg_loss = avg_loss

        # Calculate RS
        rs = round(avg_gain / avg_loss, 2)

        # Calculate RSI
        rsi = round(100 - (100 / (1 + rs)), 2)

        # Remove oldest values
        window.append(price)
        window.pop(0)
        gains.pop(0)
        losses.pop(0)
        if rsi <= rsi_buy_signal:
            buy = True
        else:
            buy = False
        if rsi >= rsi_sell_signal:
            sell = True
        else:
            sell = False

        # Save Data
        output.append([i+1, price, gain, loss, avg_gain, avg_loss, rsi, buy, sell])
        
        if i >= (len(historical_data)-candle_amount):
            if rsi <= rsi_buy_signal:
                buy = True
            else:
                buy = False
            if rsi >= rsi_sell_signal:
                sell = True
            else:
                sell = False
            for x in historical_data[-candle_amount:]:
                if round(float(x["close"]), 2) == price:
                    day = x["date"]
            rsi_output.append({"day": day, "price": price, "gain": gain, "loss": loss, "rsi": rsi, "buy":buy, "sell": sell})
    return rsi_output
    
        
def sma(Data, period):
    
    for i in range(len(Data)):
            try:
                Data[i] = (Data[i - period:i + 1])
        
            except IndexError:
                pass
    return Data