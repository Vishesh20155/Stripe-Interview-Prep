from flask import Flask, request
import sqlite3
import uuid
import json

class Student:
    def __init__(self, firstname, lastname, department):
        self.id = uuid.uuid4().hex
        self.firstname = firstname
        self.lastname = lastname
        self.department = department

    def __str__(self):
        return f'id:{self.id} ' \
               f'firstname: {self.firstname}; ' \
               f'Lastname: {self.lastname}; ' \
               f'Department: {self.department}'

app = Flask(__name__)

def initialize():
    c = sqlite3.connect("student.db").cursor()
    print("@@@Helloooo")
    c.execute("CREATE TABLE IF NOT EXISTS STUDENTS("
              "id TEXT, firstname TEXT, lastname TEXT, department TEXT)"
              )
    c.connection.close()

@app.route('/')
def go_home():
    initialize()
    return 'Home Page'

@app.route('/students')
def get_students():
    c = sqlite3.connect("student.db").cursor()
    c.execute("SELECT * FROM STUDENTS")
    data = c.fetchall()
    return json.dumps(data)

@app.route('/students/<student_id>')
def get_student_by_id(student_id):
    c = sqlite3.connect("student.db").cursor()
    c.execute("SELECT * FROM STUDENTS WHERE id = ?", (student_id, ))
    data = c.fetchone()
    return json.dumps(data)

@app.route('/insert', methods = ['POST', 'GET'])
def add_student():
    db = sqlite3.connect("student.db")
    c = db.cursor()
    student = Student(request.form["firstname"],
                      request.form["lastname"],
                      request.form["department"]
                      )
    print(student)
    c.execute("INSERT INTO STUDENTS VALUES(?,?,?,?)",
              (student.id, student.firstname, student.lastname, student.department))
    db.commit()
    data = c.lastrowid
    print(data)
    return json.dumps(data)