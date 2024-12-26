

# cd backend_service/
# source .venv/bin/activate
# python3


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





# sql = """CREATE TABLE entity (
#         entity_id SERIAL PRIMARY KEY,
#         entity_name VARCHAR(255) NOT NULL,
#         UNIQUE(entity_name)
#     )
#     """


# create a table

# sql = """CREATE TABLE ideefix_ideas (
#     idea_id SERIAL PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL,
#     short_title VARCHAR(255) NOT NULL UNIQUE,
#     idea_description TEXT NOT NULL
#     )
#     """


# execute_sql(sql)


sql = "SELECT * FROM ideefix_ideas"
execute_sql(sql)


# ggf. löschen und mit Schema neu anfangen, wo active und inactive Ideen getrennt sind





# sql = "DROP TABLE ideefix_ideas"


# first test entry

# my_name = "John Doe"
# my_email = "John.Doe@xyz.com"
# my_short_title = "My first idea"
# my_idea_description = "This is a very good idea, with a long and detailed description."


# sql = f"""
#     INSERT INTO ideefix_ideas(name, email, short_title, idea_description)
#     VALUES('{my_name}', '{my_email}', '{my_short_title}', '{my_idea_description}')
#     """

# execute_sql(sql)



# sql = "SELECT * FROM ideefix_ideas"
# execute_sql(sql)




my_name = "Jane Doe"
my_email = "Jane.Doe@xyz.com"
my_short_title = "My idea for the id returning"
my_idea_description = "This is another very good idea, with a long and detailed description."

sql = f"""
    INSERT INTO ideefix_ideas(name, email, short_title, idea_description)
    VALUES('{my_name}', '{my_email}', '{my_short_title}', '{my_idea_description}')
    RETURNING idea_id;
"""

execute_sql(sql)



sql = "SELECT idea_id FROM ideefix_ideas ORDER BY idea_id DESC LIMIT 1"
execute_sql(sql)








# create a table for setting ideas active or inactive in an own table

sql = """
CREATE TABLE ideefix_idea_status (
    id SERIAL PRIMARY KEY,
    idea_id INTEGER NOT NULL REFERENCES ideefix_ideas(idea_id),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);
"""

execute_sql(sql)



# Insert a new idea and get the idea_id
my_name = "Alice Smith"
my_email = "Alice.Smith@xyz.com"
my_short_title = "My new idea"
my_idea_description = "This is a fantastic idea, with a detailed description."

sql = f"""
    INSERT INTO ideefix_ideas(name, email, short_title, idea_description)
    VALUES('{my_name}', '{my_email}', '{my_short_title}', '{my_idea_description}')
    RETURNING idea_id;
"""

new_idea_id = execute_sql(sql)[0][0]
new_idea_id


# Insert into ideefix_idea_status with the new idea_id
sql = f"""
    INSERT INTO ideefix_idea_status(idea_id, is_active)
    VALUES({new_idea_id}, TRUE);
"""

execute_sql(sql)

# check working


sql = "SELECT * FROM ideefix_idea_status"
execute_sql(sql)


sql = "SELECT * FROM ideefix_ideas"
execute_sql(sql)



sql = """
        SELECT *
        FROM ideefix_ideas
        JOIN ideefix_idea_status ON ideefix_ideas.idea_id = ideefix_idea_status.idea_id
        WHERE ideefix_idea_status.is_active = TRUE
    """
execute_sql(sql)



# Drop the ideefix_idea_status table
sql = "DROP TABLE IF EXISTS ideefix_idea_status"
execute_sql(sql)

# Drop the ideefix_ideas table
sql = "DROP TABLE IF EXISTS ideefix_ideas"
execute_sql(sql)




# create a table

sql = """
CREATE TABLE ideefix_votes (
    id SERIAL PRIMARY KEY,
    idea_id INTEGER NOT NULL REFERENCES ideefix_ideas(id),
    vote_value INTEGER NOT NULL,  -- 1 for upvote, -1 for downvote
);
"""


execute_sql(sql)

