-- lists all cities contained in the database hbtn_0d_usa
SELECT tv_genres.name FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id WHERE tv_shows.title='Dexter' ORDER BY tv_genres.name ASC;