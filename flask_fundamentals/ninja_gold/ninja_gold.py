from flask import Flask,render_template,session,redirect
import random,datetime
app=Flask(__name__)
app.secret_key='safekey'

@app.route('/')
def index():
    if not "gold" in session:
        session['gold']=0
    if not "log" in session:
        session['log']=[]
    return render_template('index.html')

@app.route('/process_money/<location>')
def process(location):
    if location=='farm':
        result=random.randint(10,20)
    elif location=='cave':
        result=random.randint(5,10)
    elif location=='house':
        result=random.randint(2,5)
    elif location=='casino':
        result=random.randint(-50,50)
    session['gold']+=result
    win_or_loss='win'
    if result>0:
        log_str="Earn {} golds from the {}!({})".format(result,location,time_now())
    else:
        log_str="Enter a casino and lost {} golds...ouch...({})".format(abs(result),time_now())
        win_or_loss='loss'
    session['log'].append((win_or_loss,log_str))
    return redirect('/')


def time_now():
    time=datetime.datetime.now()
    return "{}/{}/{} {}:{}".format(time.year,time.month,time.day,time.hour,time.minute)



@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
