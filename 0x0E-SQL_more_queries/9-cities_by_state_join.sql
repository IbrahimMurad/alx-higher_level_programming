-- lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, states.name, cities.name FROM cities LEFT JOIN states ON cities.state_id = states.id;