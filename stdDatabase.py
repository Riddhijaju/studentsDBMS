import sqlite3

def studentData():
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Lastname text,DOB text, Age text , Gender text ,Branch text , Mobileno text)")
    con.commit()
    con.close()

def addStdRec(StdID, Firstname, Lastname,DOB, Age, Gender ,Branch ,Mobileno):
    con = sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)",(StdID, Firstname, Lastname,DOB, Age, Gender ,Branch ,Mobileno))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    row =cur.fetchall()
    con.close()
    return row

def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(StdID="", Firstname="", Lastname="",DOB="", Age="", Gender="" ,Branch="" ,Mobileno=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Lastname=? OR DOB=? OR Age=? OR Gender=? OR Branch=? OR Mobileno=?",(StdID, Firstname, Lastname,DOB, Age, Gender ,Branch ,Mobileno))
    row = cur.fetchall()
    con.close()
    return row

def dataUpdate(id,StdID="", Firstname="", Lastname="",DOB="", Age="", Gender="" ,Branch="" ,Mobileno=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Lastname=?, DOB=? , Age=? , Gender=? ,Branch=?, Mobileno=?, WHERE id=?",(StdID, Firstname, Lastname,DOB, Age, Gender ,Branch ,Mobileno, id))
    con.commit()
    con.close()


studentData()