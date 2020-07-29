from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
# import Flask framework from flask Module
from database_connection import DatabaseConnector
# import a connection from the databaseConnector class

from quiz_handler_testing import QuizCreator

# import the quiz handler

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

def clear_quiz_sessions():
    # Destroy all session variables
    session['correct_answer'] = None
    session['question_score'] = None
    session['question_counter'] = None
    session['quiz_progress'].clear()

def create_quiz_questions():
    # Create question assortment from 15 questions in a JSON file
    quiz_instance = QuizCreator()
    quiz_instance.read_json_into_dict()
    quiz_instance.generate_unique_random_values()
    return quiz_instance


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))

    return wrap


@app.route("/quiz", methods=['GET', 'POST'])
@login_required
def quiz_page():
    # Start quiz by starting a quiz session variable, this also holds the question the user is on
    if not session.get('quiz_progress'):
        g.q = create_quiz_questions()  # get questions store in 'g.q'
        # random nums = list [] and questions is a dictionary {]
        # testing separate question counter
        session['question_counter'] = 0
        session['question_score'] = 0
        # Create session variable if there isn't one [question_ID, ongoing?, random_nums, questions, score]
        session['quiz_progress'] = [0, True, g.q.get_random_nums(), g.q.get_questions(), 0]
    # Check if this was called along with a post request (check for answer)
    elif request.method == 'POST':
        if request.form['question']:  # Check for response radio button ticked
            # Check if the user has entered the correct answer
            if request.form['question'] == session['correct_answer']:
                session['question_score'] += 1
        # Update question counter
        session['question_counter'] += 1

        if session['question_counter'] == 10:
            # flash("Quiz finished. Well done!")
            return redirect(url_for('results'))

    dict_QA = session['quiz_progress'][3].get('Question' +
                                              str(session['quiz_progress'][2][session.get('question_counter')]))

    # Debug help
    print()
    print("Question " + str(session.get('question_counter') + 1))
    print("Score " + str(session.get('question_score')))
    print(str(session.get('quiz_progress')))

    question = dict_QA['Question']
    question1 = str(dict_QA['A'][0])
    question2 = str(dict_QA['B'][0])
    question3 = str(dict_QA['C'][0])
    question4 = str(dict_QA['D'][0])

    for content in dict_QA:
        if content == "Question":
            continue
        elif dict_QA[content][1]:  # if this returns true set that as the correct answer
            session['correct_answer'] = content
            break

    # This is always called at the end
    return render_template("quiztemp.html", current_question=(session['question_counter'] + 1), question=question,
                           question1=question1, question2=question2, question3=question3, question4=question4)


@app.route("/results")
@login_required
def results():
    # Eventually will generate text file and email results, along with storing it in the database
    # work out percentage
    result = (session.get('question_score') / session.get('question_counter')) * 100

    result = "Congratulations! you got " + int(result).__str__() + "% of the questions correct."

    clear_quiz_sessions()

    return render_template("results.html", results=result)


@app.route("/")
def base():
    # g is a object specific for flask to store temporary objects
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


@app.route('/logout')
@login_required
def logout():
    flash("See you next time " + session['user'].title() + "!")
    try:
        clear_quiz_sessions()  # Clear quiz sessions if any
    except Exception:
        # This catches exceptions if the user logs out without doing the quiz.
        print("There was no session variables for the quiz..")

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
