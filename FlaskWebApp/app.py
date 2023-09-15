import mysql.connector
import os
from flask import Flask, render_template
app = Flask(__name__)

config = {
    'user': os.getenv("MYSQL_ADDON_USER"),
    'password': os.getenv("MYSQL_ADDON_PASSWORD"),
    'host': os.getenv("MYSQL_ADDON_HOST"),
    'port': os.getenv("MYSQL_ADDON_PORT"),
    'database': os.getenv("MYSQL_ADDON_DB")
}

def get_db_connection():
    conn = mysql.connector.connect(**config)
    return conn

@app.route('/')
def hello_world():
    initDb()

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("UPDATE visits SET counter = (counter + 1) WHERE userName = 'user'")

    cursor.execute("SELECT * FROM visits WHERE userName = 'user'")
    visits = cursor.fetchall()

    conn.commit()
    cursor.close()
    cursor.close()
    return render_template('index.html', visits=visits)

def initDb():
    print("INIT DB......")

    conn = get_db_connection()
    if not checkTableExists(conn, "visits"):
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE visits (id INTEGER PRIMARY KEY AUTO_INCREMENT,userName VARCHAR(10),counter INTEGER)")
        conn.commit()

        cursor.execute("INSERT INTO visits (userName, counter) VALUES ('user', '0')")
        conn.commit()

        conn.close()

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

if __name__ == '__main__':
    app.run(host='0.0.0.0')
