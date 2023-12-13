-- lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, states.name, cities.name FROM cities, states WHERE cities.state_id = states.id;