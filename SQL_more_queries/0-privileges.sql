-- My privileges!
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1-z';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2-z';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILIGES;
