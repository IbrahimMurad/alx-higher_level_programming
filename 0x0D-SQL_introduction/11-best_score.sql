-- Display both the score and the name of records with score >= 10
-- from second_table of the database hbtn_0c_0.
-- ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;