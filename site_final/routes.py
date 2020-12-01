from . import app
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')

@app.route('/')
@app.route('/layout')
def layoutpage():
    return render_template('layout.html')

@app.route('/')
@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/')
@app.route('/contact')
def contactpage():
    return render_template('contact.html')

@app.route('/')
@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/')
@app.route('/post')
def postpage():
    return render_template('post.html')

@app.route('/')
@app.route('/posts')
def postspage():
    return render_template('posts.html')

@app.route('/')
@app.route('/serv')
def servicopage():
    return render_template('servico.html')

@app.route('/')
@app.route('/loja')
def lojapage():
    return render_template('loja.html')