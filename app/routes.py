from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'user_name': 'Guillaume'}
    posts = [
                {
                    'author': {'user_name': 'Michel'},
                    'body': 'Beautiful day in Portland'
                },
                {
                    'author': {'user_name': 'Babeth'},
                    'body': 'The Avengers\' movie was so cool!'
                }]
    return render_template('index.html', title='Home', user=user, posts=posts)
