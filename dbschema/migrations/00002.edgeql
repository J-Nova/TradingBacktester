CREATE MIGRATION m13beddrqh67jrrnyw4jys4jcpyw5rnn34fsczltdce5ucx2dwcbsq
    ONTO m1rzyx3jfoeixpt5kotbcrmmehdsrsh5vt4vkpr5dntoss4dfmi3dq
{
  ALTER TYPE default::Strategy {
      CREATE REQUIRED PROPERTY description -> std::str {
          SET REQUIRED USING (.name);
      };
  };
};
