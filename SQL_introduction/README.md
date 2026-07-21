# SQL_introduction

This project covers the fundamentals of SQL and relational databases using
MySQL: listing and creating databases, creating and describing tables,
inserting and updating records, filtering with WHERE, sorting with
ORDER BY, and aggregating data with COUNT, AVG, and GROUP BY.

## Files

- `0-list_databases.sql` — lists all databases on the server
- `1-create_database_if_missing.sql` — creates database `hbtn_0c_0` if missing
- `2-remove_database.sql` — deletes database `hbtn_0c_0` if it exists
- `3-list_tables.sql` — lists all tables of a database
- `4-first_table.sql` — creates `first_table` (id, name)
- `5-full_table.sql` — prints the full description of `first_table`
- `6-list_values.sql` — lists all rows of `first_table`
- `7-insert_value.sql` — inserts a row into `first_table`
- `8-count_89.sql` — counts records with id = 89 in `first_table`
- `9-full_creation.sql` — creates `second_table` and inserts sample rows
- `10-top_score.sql` — lists records ordered by score, descending
- `11-best_score.sql` — lists records with score >= 10
- `12-no_cheating.sql` — updates a record's score by name only
- `13-change_class.sql` — deletes records with score <= 5
- `14-average.sql` — computes the average score
- `15-groups.sql` — counts records grouped by score
- `16-no_link.sql` — lists records with a non-null name, sorted by score

## Usage

Each script is run by piping it into the `mysql` client, with the database
name passed as a command line argument where required:
