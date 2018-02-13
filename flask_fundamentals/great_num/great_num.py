from flask import Flask,render_template,redirect,session,request
import random
app=Flask(__name__)
app.secret_key='safekey'

@app.route('/')
def index():
    session['number']=random.randrange(0,101)
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('index.html')

@app.route('/guess',methods=['POST'])
def guess():
    num = request.form['number']
    success ='no'
    if int(num)>int(session['number']):
        msg='TOO HIGH'
    elif int(num)<int(session['number']):
        msg='TOO LOW'
    elif int(num)==int(session['number']):
        msg=num+' was the number!'
        success ='yes'

    return render_template('result.html',massege=msg,succ=success)

app.run(debug=True)