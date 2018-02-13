from flask import Flask,render_template,session,flash,request,redirect
import re,datetime,time
app=Flask(__name__)
app.secret_key='safekey'
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^.*[A-Z]+.*[0-9]+.*$')
BIRTHDAY_REGEX = re.compile(r'^[01][0-9]/[0-3][0-9]/[1-2][09][0-9][0-9]$')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate',methods=['POST'])
def validate():
    email=request.form['email']
    fname=request.form['fname']
    lname=request.form['lname']
    password=request.form['password']
    cpassword=request.form['cpassword']
    birthday=request.form['birthday']
    new=time.mktime(datetime.datetime.now().timetuple())
    if len(email)==0 or len(fname)==0 or len(lname)==0 or len(password)==0 or len(cpassword)==0:
        flash('all fields must not be blank!','blank')
    elif not NAME_REGEX.match(fname):
        flash('first name not right!','fname')
    elif not NAME_REGEX.match(lname):
        flash('last name not right!','lname')
    elif len(password)<8 or len(cpassword)<8:
        flash('password need to be more than 8 words!','password')
    elif not EMAIL_REGEX.match(email):
        flash('email is not valid!','email')
    elif password!=cpassword:
        flash('repassword should be same as password!','match')
    elif not PASSWORD_REGEX.match(password):
        flash('password should have at least one number and one upper case letter!','password')
    elif not BIRTHDAY_REGEX.match(birthday):
        flash('not a valid birthday!','password')
    elif time.mktime(time.strptime(birthday, '%m/%d/%Y'))>new:
        flash('u born too late!','password')
    else:
        flash('Thank you for submit you message','success')
    return redirect('/')



app.run(debug=True)