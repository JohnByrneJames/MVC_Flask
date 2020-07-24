from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
# import Flask framework from flask Module
from database_connection import DatabaseConnector
# import a connection from the databaseConnector class

# In order for us to use flask we need to create an instance of our app
app = Flask(__name__)
# Syntax to create flask instance (__name__)

# Sessions are only visible on the server side, they store data about the user.
# However to the client these sessions have IDs and are encrypted, therefore cannot be viewed
# To enable this we need to create a secret key.

# This key should always be completely random
# Near impossible to guess (so use a random key generate E.G. encrypted)
# Protects the session from being accessed client side
app.secret_key = "my precious"

# In browser in >>>storage you can see the session in >>>cookies. (In Mozilla)
# syntax for decorators to create a web route is @/route
# Create a welcome method to display on home/ default page

def connect_db():
    # Connection to the database is made here ~
    db_instance = DatabaseConnector("LAPTOP-23G2NM6G", "websiteDB")
    return db_instance.establish_connection()


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route("/")
def base():
    # g is a object specific to flask to store temporary objects
    # Here we are storing the connection to the database
    g.db = connect_db()
    cur = g.db.execute('SELECT * FROM Users')
    users = [dict(firstName=row[1], surname=row[2], username=row[3], password=row[4]) for row in cur.fetchall()]
    g.db.close()
    return render_template("index.html", users=users)

@app.route("/homepage")
@login_required  # If the user tries to access this page without a key (logged in) then they are redirected to login
def homepage():
    username = None
    if session['user']:
        username = session['user']

    return render_template("homepage.html", username=username)

@app.route("/login", methods=['GET', 'POST'])  # Default page start http://127.0.0.1:5000/<username>
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'john' or request.form['password'] != '123':
            if not session.get('attempts'):
                session['attempts'] = 0
            elif session.get('attempts') == 3:
                session.pop('attempts', None)  # Delete attempt counter
                flash("You have been locked out for 10 minutes...")
                return redirect(url_for('base'))
            session['attempts'] += 1
            error = 'Invalid Credentials. Try again. Attempt  [' + session['attempts'].__str__() + ']'
        else:
            # if session['attempts']:
            #     session.pop('attempts', None)  # Delete attempt counter

            session['logged_in'] = True  # Create session key
            session['user'] = request.form['username']
            return redirect(url_for('homepage'))
    return render_template("login.html", error=error)

@app.route('/quiz')
@login_required
def quiz_page():



@app.route('/logout')
@login_required
def logout():
    flash("See you next time " + session['user'].title() + "!")
    session.pop('logged_in', None)  # Delete session key
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly (so this will only respond to the 404 error)
    return render_template("404page.html"), 404


# syntax to run app -> Check instance (5), check route (10) run function (11)
# debug=True ensure to update in live time whilst making changes
# Make sure you run it in the terminal whilst in the directory where flask is, also use >>> set FLASK_ENV=development
if __name__ == '__main__':
    app.run(debug=True)
