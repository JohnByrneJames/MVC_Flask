# **MVC | Model View Controller**

In python we are using the Flask micro-framework to develop a web application that follows the MVC development
pattern.

| Model                                                                                            	| View                                                                                                   	| Controller                                                                                                                                                       	|
|--------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Uses the models to retrieve  all of the necessary data, organises it, and sends it off to the... 	| The View, which then uses that data to render the final webpage presented to the user in their browser 	| The controller receives that request. Put simply, when a request comes in,   the controller, which handles our app’s business logic,   decides how to handle it. 	|


<img style="text-align: center" src="Flask/static/images/MVC_Diagram.png" alt="drawing" width="550"/>

**Importing the flask Module and using the micro-framework to incorporate MVC**
```python
from flask import Flask
```

In order for us to use flask we need to create an instance of our app like so...

```python
app = Flask(__name__)
```

> `Syntax to create flask instance (__name__)`

syntax for decorators to create a web route is @/route, Create a welcome method to display on home/ default page.
Whatever happens after the '/' will be the URL in the browser view.

```python
@app.route("/")  # Default page start http://127.0.0.1:5000/
def index():
    return user_page("John")
```

We also printed a basic HTML page with a header.

```python
@app.route("/")  # Default page start http://127.0.0.1:5000/
def index():
    return "<h1>Welcome to MVC with flask project</h1>"
```

**Important**

To run this application we first need to go to the **Terminal** and do the following:

* `set FLASK_ENV=development`
* `run FLASK`  _Whilst you are in the directory where the base flask app is located._

It is also essential that you add a block of code to run the app when you run it in the terminal. 

`debug=True ensure to update any changes without re-running the app`

```python
if __name__ == '__main__':
    app.run(debug=True)
```

### **Exercise**

We also created another function which took in a username, dynamically within the URL with a `<username>` tag in the `@app.route`
decorator.

```python
@app.route("/<username>")  # Default page start http://127.0.0.1:5000/<username>
def user_page(username):
    return f"<h1>Welcome to Python flask app dear {username} </h1>"
```

# HTML

We did some **HTML**, **Bootstrap** (a **HTML** framework that allows responsive design with a `mobile-first` directive)

We also did some inheritance or OOP web design using the 'extends' keyword. We created a `master.html` file that extends into
the `index.html` and shows everything as a result.

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{% block title %} Engineering 67 {% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
```

Here we showed that we want to get the block specified, as of now we have not specified what not to select so it takes all the
information in the master file. 

___

# Login Page with Optional Quiz

We have been tasked with creating a log in page using the skills we have developed so far in the academy. This log in page
is a good starting point as it is a very common element in many companies and is a great example to apply our skills including:
* **CSV**, **JSON** and **.TXT** file reading and writing
* **SQL** and **Database**
* **Secure** **Password** encryption and user authentication
* **Python** :snake:
* Python **API** requests, response Codes
* **MVC** the common and widely used Model, View and Controller design pattern
* **HTML** and **Bootstrap** along with **Flask** micro-framework

## To do List 

- [x] **Interview** 

- [x] **Email notes from interview to Shahrukh**
- [x] **Finish Profile and Summary**
- [ ] **MVC** using Flask (Exercise) GitHub Repo [**HERE**](https://github.com/JohnByrneJames/MVC_Flask/tree/54cc641928e32c68b95611c4cf4d515a55534657)
    - [ ] Make Login Page
    
    - [ ] Create authentication check for successful login
    - [ ] Incorporate API Status Code checking into Login too
    - [ ] Add functionality to get questions from CSV/ JSON file
    - [ ] Create a Quiz
    - [ ] 10 Questions
    - [ ] Multiple choice questions
    - [ ] Give feedback (Score)
`


**Great Learning Resources**

**Learn Flask with Python**
* [**Part 1**](https://realpython.com/introduction-to-flask-part-1-setting-up-a-static-site/)
* [**Part 2**](https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/)

## Documentation of Login Page

First of all I designed two web page using the popular CSS framework **Bootstrap**. One was a Login Page, and the other
was a Home page, this was the first part of the work that needed to be complete - it was to facilitate the login functionality and
successful transfer from Login to Home page when the login was done successfully.





