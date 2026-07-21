# SQL_more_queries

This project covers MySQL user management and privileges, table
constraints (NOT NULL, DEFAULT, UNIQUE, PRIMARY KEY, FOREIGN KEY), and
more advanced SELECT queries: subqueries, JOINs, LEFT JOINs, GROUP BY,
and aggregate counts across multiple related tables.

## Files

- `0-privileges.sql` — lists all privileges for user_0d_1 and user_0d_2
- `1-create_user.sql` — creates user_0d_1 with all privileges
- `2-create_read_user.sql` — creates a read-only user on a specific database
- `3-force_name.sql` — creates a table with a NOT NULL constraint
- `4-never_empty.sql` — creates a table with a DEFAULT value constraint
- `5-unique_id.sql` — creates a table with a UNIQUE constraint
- `6-states.sql` — creates the states table with an auto-increment PK
- `7-cities.sql` — creates the cities table with a FOREIGN KEY to states
- `8-cities_of_california_subquery.sql` — cities of California, via subquery
- `9-cities_by_state_join.sql` — cities and their states, via JOIN
- `10-genre_id_by_show.sql` — shows with at least one genre linked
- `11-genre_id_all_shows.sql` — all shows, genre NULL if none linked
- `12-no_genre.sql` — shows without any genre linked
- `13-count_shows_by_genre.sql` — number of shows per genre
- `14-my_genres.sql` — all genres of the show Dexter
- `15-comedy_only.sql` — all Comedy shows
- `16-shows_by_genre.sql` — all shows and their linked genres

## Usage

Each script is run by piping it into the `mysql` client, with the database
name passed as a command line argument where required:
