"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template, flash, redirect
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\temp\corona.accdb;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Registrierung') 
for row in cursor.fetchall():
    print (row)

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# @app.route('/')
@app.route('/hello')
def hello():
    """Renders a sample page."""
    return "Hello World!"


@app.route('/showMe')
def showMe():
    args = request.args
    if "message" in args:
        message = args["message"]
    if "parameter1" in args:
        parameter1 = args.get("parameter1")
    if "parameter2" in args:
        parameter2 = args.get("parameter2")
    if "parameter3" in args:
        parameter3 = args.get("parameter3")
    # print(message, parameter1, parameter2, parameter3)
    
    teil1 = "<html> \
        <head><title>Meine erste Webseite</title></head> \
        <body> \
            <h3>Request: " + "/showMe"
    teil2 = "</h3> <!-- Hier soll die Route ausgegeben werden --> \
            <p>This is an example web server.</p> \
            <p>It was called with parameters:</p>  " + parameter1 + parameter2 + parameter3
    teil3 = "<!-- Hier sollen alle Parameter ausgegeben werden --> \
        </body> \
        </html>"
    return teil1 + teil2 + teil3

@app.route('/showData')
def showData():
    args = request.args
    if "message" in args:
        message = args["message"]
    if "parameter1" in args:
        parameter1 = args.get("parameter1")
    if "parameter2" in args:
        parameter2 = args.get("parameter2")
    if "parameter3" in args:
        parameter3 = args.get("parameter3")
    print(message, parameter1, parameter2, parameter3)
    return message + parameter1 + parameter2 + parameter3

class MyForm(FlaskForm):
    date = StringField('Date', validators=[DataRequired()])
    temp = StringField('Temp', validators=[DataRequired()])
    signature = BooleanField('I sign')
    submit = SubmitField('Send to server')

@app.route('/myTemp', methods=['GET', 'POST'])
def myTemp ():
    form = MyForm()

    if form.validate_on_submit():
        flash('Date {}, temp. {}, signature={}'.format(
            form.date.data, form.temp.data, form.signature.data))
        return redirect('/myTemp')
    cursor.execute('''
                INSERT INTO grunddaten ([Date], Temp, Sign)
                VALUES('2020-06-22 20:44:00', 37.3, True)
            ''')
    conn.commit()
    return render_template('form.html', title='Meine Temperatur', form=form)

@app.route('/helloDB1')
def helloDB1():
    """Renders a sample page."""
    cursor.execute('''
                INSERT INTO Registrierung ([Name], Geschlecht, Postleitzahl)
                VALUES('Otto', 'm', 1234)
            ''')
    cursor.execute('INSERT INTO Registrierung ([Name], Geschlecht, Postleitzahl) VALUES (?, ?, ?)', ('Otto', 'm', 1234))
    conn.commit()
    return "Hello Database World! Wrote test data to DB."

@app.route('/helloDB')
def helloDB():
    # /helloDB?message=store&parameter1=Peter&parameter2=m&parameter3=55555
    """Renders a sample page."""
    args = request.args
    if "message" in args:
        message = args["message"]
    if "parameter1" in args:
        parameter1 = args.get("parameter1")
    if "parameter2" in args:
        parameter2 = args.get("parameter2")
    if "parameter3" in args:
        parameter3 = args.get("parameter3")
    print(message, parameter1, parameter2, parameter3)
    # return message + parameter1 + parameter2 + parameter3
    sqlStatement = '''(INSERT INTO Registrierung(Name, Geschlecht, Postleitzahl) VALUES (?, ?, ?))'''
    #sqlStatement = (
    #                "INSERT INTO Registrierung(Name, Geschlecht, Postleitzahl) "
    #               "VALUES (%s, %s, %s)"
     #               )
    print (sqlStatement)
    sqlData= (parameter1 + ',' + parameter2 + ',' + parameter3)
    print (sqlData)
#    cursor.execute(sqlStatement, sqlData)
    cursor.execute('INSERT INTO Registrierung ([Name], Geschlecht, Postleitzahl) VALUES (?, ?, ?)', (parameter1, parameter2, parameter3))
        
    conn.commit()
    return "Hello Database World! Wrote test data to DB."

    

if __name__ == '__main__':
    import os
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try: # Codezeile mit Verdacht auf Fehlermöglichkeit probieren
        PORT = int(os.environ.get('SERVER_PORT', '5555')) # zu testender Code
    except ValueError: # in Zeile drüber ist "ValueError"-Ausnahme passiert!
        PORT = 5555 # Fallback bei Exception
    app.run(HOST, PORT) # Server starten