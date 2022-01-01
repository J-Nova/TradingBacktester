module default {
    type Rsi {
        required link Strategy -> Rsi;
        required property overbought -> std::int64 {constraint min_value(0); constraint max_value(100);}
        required property oversold -> std::int64 {constraint min_value(0); constraint max_value(100);}
        required property period -> std::int64 {constraint min_value(1); constraint max_value(100);}
    };

    type Sma {
        required link Strategy -> Sma;
        required property short_period -> std::int64 {constraint min_value(1); constraint max_value(100);}
        required property long_period -> std::int64 {constraint min_value(1); constraint max_value(100);}
    };

    type Strategy {
        required property name -> std::str {constraint min_len_value(1); constraint exclusive;}
        required property description -> std::str;
        required property stop_loss -> std::int64 {constraint min_value(0);}
        required property take_profit -> std::int64 {constraint min_value(0);}
        required property creation_date -> std::str;
        required property update_date -> std::str;
    };


    type Chart_1m {
        required property candleid -> std::str {constraint exclusive;}
        required property symbol -> std::str;
        required property date -> std::str;
        required property time -> std::str;
        required property open -> std::float64;
        required property high -> std::float64;
        required property low -> std::float64;
        required property close -> std::float64;
        required property volume -> std::float64;
    };

    type Chart_5m {
        required property candleid -> std::str {constraint exclusive;}
        required property symbol -> std::str;
        required property date -> std::str;
        required property time -> std::str;
        required property open -> std::float64;
        required property high -> std::float64;
        required property low -> std::float64;
        required property close -> std::float64;
        required property volume -> std::float64;
    };

    type Chart_15m {
        required property candleid -> std::str {constraint exclusive;}
        required property symbol -> std::str;
        required property date -> std::str;
        required property time -> std::str;
        required property open -> std::float64;
        required property high -> std::float64;
        required property low -> std::float64;
        required property close -> std::float64;
        required property volume -> std::float64;
    };

    type Chart_30m {
        required property candleid -> std::str {constraint exclusive;}
        required property symbol -> std::str;
        required property date -> std::str;
        required property time -> std::str;
        required property open -> std::float64;
        required property high -> std::float64;
        required property low -> std::float64;
        required property close -> std::float64;
        required property volume -> std::float64;
    };


    type Chart_1h {
        required property candleid -> std::str {constraint exclusive;}
        required property symbol -> std::str;
        required property open -> std::float64;
        required property high -> std::float64;
        required property low -> std::float64;
        required property close -> std::float64;
        required property volume -> std::float64;
        required property date -> std::str;
        required property time -> std::str;
    };

    type Chart_2h {
        required property candleid -> std::str {constraint exclusive;}
        required property symbol -> std::str;
        required property date -> std::str;
        required property time -> std::str;
        required property open -> std::float64;
        required property high -> std::float64;
        required property low -> std::float64;
        required property close -> std::float64;
        required property volume -> std::float64;
    };

    type Chart_4h {
        required property candleid -> std::str {constraint exclusive;}
        required property symbol -> std::str;
        required property date -> std::str;
        required property time -> std::str;
        required property open -> std::float64;
        required property high -> std::float64;
        required property low -> std::float64;
        required property close -> std::float64;
        required property volume -> std::float64;
    };

    type Chart_1d {
        required property candleid -> std::str {constraint exclusive;}
        required property symbol -> std::str;
        required property date -> std::str;
        required property time -> std::str;
        required property open -> std::float64;
        required property high -> std::float64;
        required property low -> std::float64;
        required property close -> std::float64;
        required property volume -> std::float64;
    };

};