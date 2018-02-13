from flask import Flask,render_template,session,redirect,request,flash
app=Flask(__name__)
app.secret_key='safekey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate',methods=['POST'])
def validate():
    name=request.form['name']
    comment=request.form['comment']
    session['language']=request.form['language']
    session['location']=request.form['location']
    if len(name)>0 and len(comment)>0:
        session['name']=name
        session['comment']=comment
    else:
        flash('name and comment can not be blank!')
        return redirect('/')

    if len(comment)>120:
        flash('comment should be less than 120 words!')
        return redirect('/')

    return redirect('/show')

@app.route('/show')
def show():
    return render_template('show.html')


app.run(debug=True)