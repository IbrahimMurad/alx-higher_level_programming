USE hbtn_0e_0_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
SELECT states.id , states.name FROM states WHERE states.name = 'Arizona';
TRUNCATE TABLE states;
SELECT * FROM states;
DROP TABLE states;


, 'root', '42724464', 'hbtn_0e_0_usa', "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"