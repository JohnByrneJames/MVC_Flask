from flask import Flask
# import Flask framework from flask Module

# In order for us to use flask we need to create an instance of our app
app = Flask(__name__)
# Syntax to create flask instance (__name__)

# syntax for decorators to create a web route is @/route
# Create a welcome method to display on home/ default page
@app.route("/")  # Default page start http://127.0.0.1:5000/
def index():
    return user_page("John")
    # return "<h1>Welcome to MVC with flask project</h1>"
# index method will be called at the endpoint (place where we connect to)

@app.route("/<username>")  # Default page start http://127.0.0.1:5000/<username>
def user_page(username):
    return f"<h1>Welcome to Python flask app dear {username} </h1>"


# syntax to run app -> Check instance (5), check route (10) run function (11)
if __name__ == '__main__':
    app.run(debug=True)
# debug=True ensure to update any changes without re-running the app
# Make sure you run it in the terminal whilst in the directory where flask is, also use >>> set FLASK_ENV=development

# ~Exercise~
# create a function called welcome_user
# create a decorator to link the page /user
# return "Welcome to Python flask app dear <name>"
