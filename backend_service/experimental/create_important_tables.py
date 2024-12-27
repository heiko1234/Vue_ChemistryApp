


import psycopg2
import pandas as pd



def execute_sql(sql):
    #establishing the connection
    conn = psycopg2.connect(
        database="ideefix", user='postgres', password='postgres', host='127.30.0.1', port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()


    cursor.execute(sql)

    try:
        result = cursor.fetchall()

    except BaseException:
        result = cursor.rowcount
        if result == -1:
            result = "Done"

    # end everyting
    cursor.close()
    conn.close()

    return result





sql = """CREATE TABLE ideefix_ideas (
    idea_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    short_title VARCHAR(255) NOT NULL UNIQUE,
    idea_description TEXT NOT NULL
    )
    """


execute_sql(sql)






sql = """
CREATE TABLE ideefix_idea_status (
    id SERIAL PRIMARY KEY,
    idea_id INTEGER NOT NULL REFERENCES ideefix_ideas(idea_id),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);
"""

execute_sql(sql)



sql = """CREATE TABLE ideefix_idea_votes (
    id SERIAL PRIMARY KEY,
    idea_id INTEGER NOT NULL REFERENCES ideefix_ideas(idea_id),
    vote_count_good INTEGER NOT NULL DEFAULT 0,
    vote_count_bad INTEGER NOT NULL DEFAULT 0
    )
    """
execute_sql(sql)





sql = """CREATE TABLE feature_ideas (
    feature_id SERIAL PRIMARY KEY,
    feature_title VARCHAR(255) NOT NULL UNIQUE,
    feature_description TEXT NOT NULL
    )
    """

execute_sql(sql)



sql = """CREATE TABLE idea_feature_links (
    id SERIAL PRIMARY KEY,
    idea_id INTEGER NOT NULL REFERENCES ideefix_ideas(idea_id),
    feature_id INTEGER NOT NULL REFERENCES feature_ideas(feature_id)
    )
    """

execute_sql(sql)















