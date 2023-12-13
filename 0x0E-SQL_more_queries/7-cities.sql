-- Active: 1702391851621@@127.0.0.1@3306@hbtn_0d_usa
-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT PRIMARY key,
	state_id INT NOT NULL, Foreign Key (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);