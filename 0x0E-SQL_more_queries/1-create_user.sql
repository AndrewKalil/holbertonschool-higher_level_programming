-- create use with a password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- granting priviledges to this new user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
