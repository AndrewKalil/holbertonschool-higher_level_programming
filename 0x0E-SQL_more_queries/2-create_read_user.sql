-- create a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- setting priviledges for this user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
