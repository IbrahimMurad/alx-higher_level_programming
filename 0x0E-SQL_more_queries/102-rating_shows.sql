-- lists all shows from hbtn_0d_tvshows_rate by their rating
WITH rating_table AS (SELECT show_id, SUM(rate) AS rating FROM tv_show_ratings GROUP BY show_id)
SELECT tv_shows.title, rating_table.rating FROM tv_shows JOIN rating_table ON rating_table.show_id = tv_shows.id ORDER BY rating DESC;