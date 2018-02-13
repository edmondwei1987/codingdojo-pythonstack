from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    name=request.form['name']
    hobby=request.form['hobby']
    comment=request.form['comment']
    sex=request.form['sex']

    return render_template('info.html',iname=name,ihobby=hobby,icomment=comment,isex=sex)

app.run(debug=True)
