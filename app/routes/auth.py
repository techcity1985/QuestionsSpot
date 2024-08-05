from flask import Blueprint, request, redirect, render_template, session

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
        return redirect('/dashboard')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')
