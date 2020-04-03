import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This-is-a-secret-key'
