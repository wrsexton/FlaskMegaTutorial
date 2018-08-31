from flask import render_template
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
