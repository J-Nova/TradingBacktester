CREATE MIGRATION m1loajym2fitjvzxsznownbzl4koifb625pniazbyktlluefxvu4ga
    ONTO m13beddrqh67jrrnyw4jys4jcpyw5rnn34fsczltdce5ucx2dwcbsq
{
  ALTER TYPE default::Strategy {
      CREATE REQUIRED PROPERTY creation_date -> std::str {
          SET REQUIRED USING (.name);
      };
  };
};
