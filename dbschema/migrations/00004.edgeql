CREATE MIGRATION m1o3kec2pbnnez4pjcczdwoocdqzhohjhwf4r4bviz432qcdybyvaq
    ONTO m1loajym2fitjvzxsznownbzl4koifb625pniazbyktlluefxvu4ga
{
  ALTER TYPE default::Strategy {
      CREATE REQUIRED PROPERTY update_date -> std::str {
          SET REQUIRED USING (.name);
      };
  };
};
