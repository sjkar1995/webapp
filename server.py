from flask import Flask
from markupsafe import escape

app = Flask(__name__)
#hello

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route('/main')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'