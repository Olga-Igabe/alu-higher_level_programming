# python-object_relational_mapping

This project covers connecting Python to a MySQL database two ways: raw
SQL queries via `MySQLdb`, and Object-Relational Mapping (ORM) via
`SQLAlchemy`. It also demonstrates a real SQL injection vulnerability and
how to fix it with parameterized queries.

## Files

- `0-select_states.py` — lists all states (MySQLdb)
- `1-filter_states.py` — lists states starting with 'N' (MySQLdb)
- `2-my_filter_states.py` — filters states by name (vulnerable to SQL injection)
- `3-my_safe_filter_states.py` — filters states by name (safe from SQL injection)
- `4-cities_by_state.py` — lists all cities with their state, single query (MySQLdb)
- `5-filter_cities.py` — lists city names for a given state (MySQLdb, safe)
- `model_state.py` — SQLAlchemy State model
- `6-model_state.py` — creates the states table via SQLAlchemy
- `7-model_state_fetch_all.py` — lists all states (SQLAlchemy)
- `8-model_state_fetch_first.py` — prints the first state (SQLAlchemy)
- `9-model_state_filter_a.py` — lists states containing 'a' (SQLAlchemy)
- `10-model_state_my_get.py` — finds a state's id by name, safely (SQLAlchemy)
- `11-model_state_insert.py` — inserts a new state (SQLAlchemy)
- `12-model_state_update_id_2.py` — updates a state's name (SQLAlchemy)
- `13-model_state_delete_a.py` — deletes states containing 'a' (SQLAlchemy)
- `model_city.py` — SQLAlchemy City model, with a FK to states
- `14-model_city_fetch_by_state.py` — lists all cities with their state (SQLAlchemy join)

## Usage

Each script takes MySQL connection arguments:
./0-select_states.py <mysql_user> <mysql_password> <database>
./2-my_filter_states.py <mysql_user> <mysql_password> <database> <state_name>
## Requirements

- `mysqlclient` (provides the `MySQLdb` module)
- `SQLAlchemy`
