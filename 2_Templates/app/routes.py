from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Reese'}
    posts = [
        {
            'author': {'username': 'Mario'},
            'body': "It's-a-me!  Mario!"
        },
        {
            'author': {'username': 'Luigi'},
            'body': 'Here we go!'
        }
    ]
    return render_template('index.html', title='Mushroom Kingdom', user=user, posts=posts)
