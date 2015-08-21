from flask import render_template, flash, redirect
from FlaskPage import app
from .forms import InputForm

@app.route('/input',methods=['GET','POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        flash('Input submitted')
    return render_template('input.html',
                           title='Wind Analysis',
                           form=form)

@app.route('/')
@app.route('/index')
def index():
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
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)