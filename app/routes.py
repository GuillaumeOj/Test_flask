from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Guillaume'}
    posts = [
                {
                    'author': {'username': 'Michel'},
                    'body': 'Beautiful day in Portland'
                },
                {
                    'author': {'username': 'Babeth'},
                    'body': 'The Avengers\' movie was so cool!'
                }]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        message = f'Login requested for {form.username.data},'
        message += f' remember_me={form.remember_me.data}'
        flash(message)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
