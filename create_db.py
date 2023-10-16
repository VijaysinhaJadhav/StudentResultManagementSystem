import sqlite3
#the above line is used for database withour installing external software

def create_db():
    con=sqlite3.connect(database="rms.db")
    #the above line is used to create an empty database

    cur=con.cursor()
    #the above line is used to execute the sql query

    cur.execute("CREATE TABLE IF NOT EXISTS course (cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,fees text,description text)")
    #the above line is used CREATE TABLE and keep the CID AUTOCREMENT 
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER PRIMARY KEY AUTOINCREMENT,name text, email text, gender text, dob text, contact text, admission text, course text, state text, city text, pin text, address text)")
    #the above line is used CREATE TABLE and keep the CID AUTOCREMENT 
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result (rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    #the above line is used CREATE TABLE and keep the CID AUTOCREMENT 
    con.commit()

    con.close()




create_db()    