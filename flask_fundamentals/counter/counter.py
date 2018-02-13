from flask import Flask,session,render_template,redirect,request
app=Flask(__name__)
app.secret_key="safekeyhere"

@app.route('/')
def index():
    if not session.has_key('count'):
        session['count']=0
    else:
        session['count']=session['count']+1
    return redirect('/show')

@app.route('/counter',methods=['POST'])
def counter():
    session['count']=session['count']+int(request.form['addnum'])
    return redirect('/show')

@app.route('/reset',methods=['POST'])
def reset():
    session['count']=0
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('index.html',count=session['count'])


app.run(debug=True)
