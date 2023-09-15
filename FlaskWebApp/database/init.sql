CREATE DATABASE IF NOT EXISTS bmkm0kmnvlkfhidycazf;
use bmkm0kmnvlkfhidycazf;

CREATE TABLE visits (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT,
                        userName VARCHAR(10),
                        counter INTEGER
);

INSERT INTO visits (userName, counter) VALUES ('user', '0');