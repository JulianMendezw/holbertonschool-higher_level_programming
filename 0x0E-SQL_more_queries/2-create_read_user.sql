-- script that creates the database hbtn_0d_2 and the user user_0d_2.
-- Only if no exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d2.* TO 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

