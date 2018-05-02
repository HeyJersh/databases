"""
Project: Fun with SQLite Databases
Goal: Learn how to build and maintain databases in Python and SQLite3
Author: Joshua Gomez (Kaizen)
"""

# DB Dependencies
import sqlite3
# For printing neatly
import pandas as pd

# Create a DB connection
db = sqlite3.connect('hubway.db')

# Create a query method for Pandas
def run_query(query):
    return pd.read_sql_query(query, db)

# Create some Queries
longest_trip_duration = """
    SELECT start_date, bike_number, duration
    FROM trips
    ORDER BY duration DESC
    LIMIT 10;
"""

longest_duration_registered = """
    SELECT *
    FROM trips
    WHERE (duration >= 9990) AND (sub_type = 'Registered')
    ORDER BY duration DESC
"""

total_trips_registered = """
    SELECT COUNT(*) as "Total number of trips by a registered member"
    FROM trips
    WHERE (sub_type = 'Registered')

"""

# Print results in a neat fashion
print(run_query(total_trips_registered))

