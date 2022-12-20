from flask import Flask,render_template,request,redirect,session
from db import Database
import api
app = Flask(__name__) # app object
app.secret_key='12126nlpwebapp' # secretKey for the session
dbo = Database() # Database object
@app.route('/') # url
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response = dbo.insert(name,email,password)
    if response:
        return render_template('login.html',message='Registration Successful. Kindly login to proceed')
    else:
        return render_template('register.html',message='Email Already exist')

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('user_email')
    password=request.form.get('user_password')
    response = dbo.search(email,password)
    if response==1:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='Invalid Email/Password')

@app.route('/profile')
def profile():
    if 'logged_in' in session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if 'logged_in' in session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    text=request.form.get('ner_text')
    response = api.ner(text)
    return render_template('ner.html',response=response)

@app.route('/sentiment_analysis')
def sentiment_analysis():
    if 'logged_in' in session:
        return render_template('sentiment.html')
    else:
        return redirect('/')

@app.route('/perform_sentiment_analysis',methods=['post'])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    response = api.sentiment(text)
    sentiment = ""
    max_score = 0
    for i in response['sentiment']:
        if response['sentiment'][i] > max_score:
            sentiment=i
            max_score = response['sentiment'][i]
    result = {'sentiment':sentiment,'score':max_score}
    return render_template('sentiment.html',result=result)

@app.route('/abusive_detection')
def abusive_detection():
    if 'logged_in' in session:
        return render_template('abusive_detection.html')
    else:
        return redirect('/')

@app.route('/perform_abusive_detection',methods=['post'])
def perform_abusive_detection():
    text = request.form.get('abusive_text')
    response = api.abusive(text)
    return render_template('abusive_detection.html',response=response)


app.run(debug=True)