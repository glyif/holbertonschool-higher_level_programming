-- creates db and assigns user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT ALL PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
