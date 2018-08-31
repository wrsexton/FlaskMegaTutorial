import os

class Config(object):
    # Protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
