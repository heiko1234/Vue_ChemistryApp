

import psycopg2
import pandas as pd




def execute_sql(sql):
    #establishing the connection
    conn = psycopg2.connect(
        database="ideefix", user='postgres', password='postgres', host='127.30.0.1', port= '5432'
        # database="ideefix", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
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


