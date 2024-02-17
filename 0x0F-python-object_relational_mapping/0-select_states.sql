USE hbtn_0e_0_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
SELECT states.id , states.name FROM states WHERE states.name REGEXP '^N' ORDER BY states.id ASC;
DROP TABLE states;