from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninja_color(color):
    img='notapril.jpg'
    if color=='blue':
        img='leonardo.jpg'
    elif color=='orange':
        img='michelangelo.jpg'
    elif color=='red':
        img='raphael.jpg'
    elif color=='purple':
        img='donatello.jpg'
    return render_template('ninja_color.html',nimg='img/'+img)

app.run(debug=True)