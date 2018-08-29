from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Reese'}
    return '''
    <html>
        <head>
            <title>Home Page - Micrblog</title>
        </head>
        <body>
            <h1>Hello, {0}!</h1>
        </body>
    </html>'''.format(user['username'])
