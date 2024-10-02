from mysql import connector
# i am checking if database exists
dbname = 'consistancy'

a_conn = connector.connect(
    host = 'localhost',
    user = 'Ruhi',
    passwd = 'Ruhi@5084'
)

cur = a_conn.cursor()
cur.execute(f"Show Databases")
res = cur.fetchall()
if (dbname,) in res:
    print("Database exists")
else:
    cur.execute(f"Create Database {dbname}")
    print("Database created")
    a_conn.commit()

a_conn.close()

the_db_conn = connector.connect(
    host = 'localhost',
    user = 'Ruhi',
    passwd = 'Ruhi@5084',
    database = dbname
)

cur = the_db_conn.cursor()

Query_create_my_progress = """
create table if not exists my_progress (Today datetime Default current_timestamp primary key,
The_topic VARCHAR(255),
    The_test_result INT,
    The_suggestion TEXT)
"""
Query_create_struggles = """
CREATE TABLE if not exists struggles (
    The_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP primary key,
    The_struggle TEXT,
    The_suggestion TEXT
)
"""
Query_create_ideas_table = """
CREATE TABLE if not exists ideas (
    The_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP primary key,
    Category VARCHAR(255),
    Idea_heading VARCHAR(255),
    Idea_description TEXT,
    Implementable BOOLEAN,
    Status ENUM('implemented', 'implementing', 'understood', 'understanding', 'not reached')
)
"""
cur.execute(Query_create_my_progress)
cur.execute(Query_create_struggles)
cur.execute(Query_create_ideas_table)
the_db_conn.commit()
the_db_conn.close()

def connnecting():
    db = connector.connect(
        host = 'localhost',
        user = 'Ruhi',
        passwd = 'Ruhi@5084',
        database = dbname
    )

    cur = db.cursor()
    return db,cur
