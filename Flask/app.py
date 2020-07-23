from flask import Flask, render_template, redirect, url_for, request, session, flash
# import Flask framework from flask Module

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

# In browser in storage you can see the session in cookies.

# Simple Redirect Function
@app.route("/")
def base():
    return


@app.route("/homepage")
def homepage():
    username = None
    if session['user']:
        username = session['user']

    return render_template("master.html", username=username)

# syntax for decorators to create a web route is @/route
# Create a welcome method to display on home/ default page
@app.route("/login", methods=['GET', 'POST'])  # Default page start http://127.0.0.1:5000/<username>
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'john' or request.form['password'] != '123':
            error = 'Invalid Credentials. Try again.'
        else:
            session['logged_in'] = True  # Create session key
            session['user'] = request.form['username']
            return redirect(url_for('homepage'))
    return render_template("login.html", error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Delete session key
    return redirect(url_for('login'))


# Login functionality with GEt, POST methods of HTTP
# import request to use the methods check status code
# add control flow to redirect the user according to the status code


# syntax to run app -> Check instance (5), check route (10) run function (11)
if __name__ == '__main__':
    app.run(debug=True)
# debug=True ensure to update any changes without re-running the app
# Make sure you run it in the terminal whilst in the directory where flask is, also use >>> set FLASK_ENV=development
