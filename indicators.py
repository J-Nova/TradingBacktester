def RSI(rsi_period, rsi_sell_signal, rsi_buy_signal):
    # Needs closing candle data.
    window_lenght = rsi_period
    gains = []
    losses = []
    window = []
    
    prev_avg_gain = None
    prev_avg_loss = None
    
    
    output = [['date', 'close', 'gain', 'loss', 'avg_gain', 'avg_loss', 'rsi']]
