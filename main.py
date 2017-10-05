from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      

@app.route("/", methods=['GET', 'POST'])
def signup():    
    if request.method == 'GET':
        return render_template('signup.html')
    
    username = request.form['username']
    password = request.form['password']
    verifypass = request.form['verifypass']
    email = request.form['email']
    username_error=''
    password_error=''
    verify_error=''
    email_error=''
    count_at = email.count('@')
    count_period = email.count('.')

    if username == '' or ' ' in username:
        username_error = "Username invalid!"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between than 3 and 20 characters!"
    if password == ''  or ' ' in password:
        password_error = "Invalid Password!"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between than 3 and 20 characters!"
    if verifypass != password:
        verify_error = "Passwords don't match!"
    if email is not "":
        if len(email) < 3 or len(email) > 20 or count_at != 1 or count_period != 1 or ' ' in email:
            email_error = "Invalid Email!"
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/welcome")
def welcome(): 
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()