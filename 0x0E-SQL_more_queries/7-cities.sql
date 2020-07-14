-- create a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create new table on a specific databse
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL,
state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id));