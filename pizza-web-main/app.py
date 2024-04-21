from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
import random
import string
from flask_mysqldb import MySQL

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'supersecretkey'

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'projectdemo969@gmail.com'  
app.config['MAIL_PASSWORD'] = 'qneq ajdm sxes yyza' 
app.config['MAIL_DEFAULT_SENDER'] = 'projectdemo969@gmail.com'  

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'saurabh123'
app.config['MYSQL_DB'] = 'asproject2'

mail = Mail(app)
mysql = MySQL(app)

# Function to generate OTP
def generate_otp():
    return ''.join(random.choices(string.digits, k=4))

@app.route('/')
def index():    
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employees WHERE employee_id = %s AND name = %s AND email = %s", (employee_id, name, email))
        user = cur.fetchone()
        cur.close()

        if user:
            otp = generate_otp()
            session['otp'] = otp
            session['user'] = user
            msg = Message('OTP Verification', recipients=[email])
            msg.body = f'Your OTP for login: {otp}'
            mail.send(msg)
            return redirect(url_for('verify'))
        else:
            return "Invalid credentials"

    return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        entered_otp = request.form['otp1'] + request.form['otp2'] + request.form['otp3'] + request.form['otp4'] 
        if session.get('otp') == entered_otp:
            session.pop('otp')
            user = session.pop('user')
            return redirect(url_for('pizza_site'))
        else:
            message = "Invalid OTP. Please try again."
            return render_template('verify.html', message=message)
    return render_template('verify.html')

@app.route('/pizza')
def pizza_site():
    return render_template('pizza.html')
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        email = request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employees (employee_id, name, email) VALUES (%s, %s, %s)", (employee_id, name, email))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('admin'))

    return render_template('admin.html')


@app.route('/admin.html')
def employee_added():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
