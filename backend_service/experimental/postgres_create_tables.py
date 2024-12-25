




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



sql = """CREATE TABLE ideefix_ideas (
    idea_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    short_title VARCHAR(255) NOT NULL UNIQUE,
    idea_description TEXT NOT NULL
    )
    """


execute_sql(sql)


sql = "SELECT * FROM ideefix_ideas"
execute_sql(sql)




# sql = "DROP TABLE ideefix_ideas"


# first test entry

my_name = "John Doe"
my_email = "John.Doe@xyz.com"
my_short_title = "My first idea"
my_idea_description = "This is a very good idea, with a long and detailed description."


sql = f"""
    INSERT INTO ideefix_ideas(name, email, short_title, idea_description)
    VALUES('{my_name}', '{my_email}', '{my_short_title}', '{my_idea_description}')
    """

execute_sql(sql)



sql = "SELECT * FROM ideefix_ideas"
execute_sql(sql)





