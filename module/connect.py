import psycopg2
import sys


def DB_CURSOR(sql):

    try:
        conn = psycopg2.connect(
            database="DBMS", user="stu", password="nukim", host="localhost")

        cursor = conn.cursor()

        cursor.execute(sql)

        data = cursor.fetchall()

        return data

    except psycopg2.Error as error:
        print(error)

    finally:
        conn.close()
