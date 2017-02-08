from flask import Flask
from flask import render_template
from .forms import LoginForm

app = Flask(__name__)
#app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.config.TestConfig')
#app.config.from_pyfile('config.py')

print app.config["CFG"]


@app.route('/')
def hello_world():
    return 'Hello World!'


"""
@app.route('/idx')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''
"""


@app.route('/idx')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template("index.html",
                           # title='Home',
                           user=user)


@app.route('/index1')
def index1():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index2.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)

if __name__ == '__main__':
    app.run(port=5000)
