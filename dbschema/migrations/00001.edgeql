CREATE MIGRATION m1rzyx3jfoeixpt5kotbcrmmehdsrsh5vt4vkpr5dntoss4dfmi3dq
    ONTO initial
{
  CREATE TYPE default::Chart_15m {
      CREATE REQUIRED PROPERTY candleid -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY close -> std::float64;
      CREATE REQUIRED PROPERTY date -> std::str;
      CREATE REQUIRED PROPERTY high -> std::float64;
      CREATE REQUIRED PROPERTY low -> std::float64;
      CREATE REQUIRED PROPERTY open -> std::float64;
      CREATE REQUIRED PROPERTY symbol -> std::str;
      CREATE REQUIRED PROPERTY time -> std::str;
      CREATE REQUIRED PROPERTY volume -> std::float64;
  };
  CREATE TYPE default::Chart_1d {
      CREATE REQUIRED PROPERTY candleid -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY close -> std::float64;
      CREATE REQUIRED PROPERTY date -> std::str;
      CREATE REQUIRED PROPERTY high -> std::float64;
      CREATE REQUIRED PROPERTY low -> std::float64;
      CREATE REQUIRED PROPERTY open -> std::float64;
      CREATE REQUIRED PROPERTY symbol -> std::str;
      CREATE REQUIRED PROPERTY time -> std::str;
      CREATE REQUIRED PROPERTY volume -> std::float64;
  };
  CREATE TYPE default::Chart_1h {
      CREATE REQUIRED PROPERTY candleid -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY close -> std::float64;
      CREATE REQUIRED PROPERTY date -> std::str;
      CREATE REQUIRED PROPERTY high -> std::float64;
      CREATE REQUIRED PROPERTY low -> std::float64;
      CREATE REQUIRED PROPERTY open -> std::float64;
      CREATE REQUIRED PROPERTY symbol -> std::str;
      CREATE REQUIRED PROPERTY time -> std::str;
      CREATE REQUIRED PROPERTY volume -> std::float64;
  };
  CREATE TYPE default::Chart_1m {
      CREATE REQUIRED PROPERTY candleid -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY close -> std::float64;
      CREATE REQUIRED PROPERTY date -> std::str;
      CREATE REQUIRED PROPERTY high -> std::float64;
      CREATE REQUIRED PROPERTY low -> std::float64;
      CREATE REQUIRED PROPERTY open -> std::float64;
      CREATE REQUIRED PROPERTY symbol -> std::str;
      CREATE REQUIRED PROPERTY time -> std::str;
      CREATE REQUIRED PROPERTY volume -> std::float64;
  };
  CREATE TYPE default::Chart_2h {
      CREATE REQUIRED PROPERTY candleid -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY close -> std::float64;
      CREATE REQUIRED PROPERTY date -> std::str;
      CREATE REQUIRED PROPERTY high -> std::float64;
      CREATE REQUIRED PROPERTY low -> std::float64;
      CREATE REQUIRED PROPERTY open -> std::float64;
      CREATE REQUIRED PROPERTY symbol -> std::str;
      CREATE REQUIRED PROPERTY time -> std::str;
      CREATE REQUIRED PROPERTY volume -> std::float64;
  };
  CREATE TYPE default::Chart_30m {
      CREATE REQUIRED PROPERTY candleid -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY close -> std::float64;
      CREATE REQUIRED PROPERTY date -> std::str;
      CREATE REQUIRED PROPERTY high -> std::float64;
      CREATE REQUIRED PROPERTY low -> std::float64;
      CREATE REQUIRED PROPERTY open -> std::float64;
      CREATE REQUIRED PROPERTY symbol -> std::str;
      CREATE REQUIRED PROPERTY time -> std::str;
      CREATE REQUIRED PROPERTY volume -> std::float64;
  };
  CREATE TYPE default::Chart_4h {
      CREATE REQUIRED PROPERTY candleid -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY close -> std::float64;
      CREATE REQUIRED PROPERTY date -> std::str;
      CREATE REQUIRED PROPERTY high -> std::float64;
      CREATE REQUIRED PROPERTY low -> std::float64;
      CREATE REQUIRED PROPERTY open -> std::float64;
      CREATE REQUIRED PROPERTY symbol -> std::str;
      CREATE REQUIRED PROPERTY time -> std::str;
      CREATE REQUIRED PROPERTY volume -> std::float64;
  };
  CREATE TYPE default::Chart_5m {
      CREATE REQUIRED PROPERTY candleid -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY close -> std::float64;
      CREATE REQUIRED PROPERTY date -> std::str;
      CREATE REQUIRED PROPERTY high -> std::float64;
      CREATE REQUIRED PROPERTY low -> std::float64;
      CREATE REQUIRED PROPERTY open -> std::float64;
      CREATE REQUIRED PROPERTY symbol -> std::str;
      CREATE REQUIRED PROPERTY time -> std::str;
      CREATE REQUIRED PROPERTY volume -> std::float64;
  };
  CREATE TYPE default::Rsi {
      CREATE REQUIRED LINK Strategy -> default::Rsi;
      CREATE REQUIRED PROPERTY overbought -> std::int64 {
          CREATE CONSTRAINT std::max_value(100);
          CREATE CONSTRAINT std::min_value(0);
      };
      CREATE REQUIRED PROPERTY oversold -> std::int64 {
          CREATE CONSTRAINT std::max_value(100);
          CREATE CONSTRAINT std::min_value(0);
      };
      CREATE REQUIRED PROPERTY period -> std::int64 {
          CREATE CONSTRAINT std::max_value(100);
          CREATE CONSTRAINT std::min_value(1);
      };
  };
  CREATE TYPE default::Sma {
      CREATE REQUIRED LINK Strategy -> default::Sma;
      CREATE REQUIRED PROPERTY long_period -> std::int64 {
          CREATE CONSTRAINT std::max_value(100);
          CREATE CONSTRAINT std::min_value(1);
      };
      CREATE REQUIRED PROPERTY short_period -> std::int64 {
          CREATE CONSTRAINT std::max_value(100);
          CREATE CONSTRAINT std::min_value(1);
      };
  };
  CREATE TYPE default::Strategy {
      CREATE REQUIRED PROPERTY name -> std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::min_len_value(1);
      };
      CREATE REQUIRED PROPERTY stop_loss -> std::int64 {
          CREATE CONSTRAINT std::min_value(0);
      };
      CREATE REQUIRED PROPERTY take_profit -> std::int64 {
          CREATE CONSTRAINT std::min_value(0);
      };
  };
};
