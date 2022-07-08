import sqlite3
def database():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute('Create table if not EXISTS Parking (serial_no integer primary key autoincrement, type text Not Null,reg_num varchar(14) not null unique,name varchar(20),contact varchar(11),checkIn text not null,checkOut text,fare int)')
    con.commit()
database()