from urllib import request
from flask import *
import joblib
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index_main():
 return render_template('index.html')

@app.route('/index.html', methods=['GET'])
def index():
 return render_template('index.html')

@app.route('/register.html', methods=['GET'])
def reg():
 return render_template('register.html')

@app.route('/login.html', methods=['GET'])
def login():
 return render_template('login.html')

@app.route('/logout.html', methods=['GET'])
def logout():
 return render_template('index.html')
 
@app.route('/prediction.html', methods=['GET', 'POST'])
def home_page():
    res=""
    if request.method == 'POST':
        age = float(request.form.get('age'))
        sex = float(request.form.get('sex'))
        cp = float(request.form.get('cp'))
        bp = float(request.form.get('trestbps'))
        chol = float(request.form.get('chol'))
        fbs = float(request.form.get('fbs'))
        ecg = float(request.form.get('restecg'))
        thalach = float(request.form.get('thalach'))
        exang = float(request.form.get('exang'))
        oldpeak = float(request.form.get('oldpeak'))
        slope = float(request.form.get('slope'))
        ca = float(request.form.get('ca'))
        thal = float(request.form.get('thal'))
        print([age, sex, cp, bp, chol, fbs, ecg, thalach, exang, oldpeak, slope, ca, thal])
        loaded_model = joblib.load('rf_class')
        [res] = loaded_model.predict([[age, sex, cp, bp, chol, fbs, ecg, thalach, exang, oldpeak, slope, ca, thal]])
        if(res==1):
            res="Absence of heart diseases"
        else:
            res="There is a possibility of presence of heart disease(s)... Kindly consult a doctor"
        return render_template('prediction.html', result= res)
    return render_template('prediction.html', result= res)

