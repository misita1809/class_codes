from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def welcome():
    return 'Welcome to my web page'

@app.route('/mishita')
def mishi():
    return 'Dikho k ye second page hai'

@app.route('/user')
def user_form():
    return '''
    <form method="POST" action="http://127.0.0.1:5000/user-data">
           <div><label>First Name: <input type="text" name="fname"></label></div>
           <div><label>Last Name: <input type="text" name="lnm"></label></div>
           <input type="submit" value="Submit">
    </form>
    '''
@app.route('/user-data', methods=['GET','POST'])

def user_data():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        result = '''
                    '''

        return result.format(first_name, last_name)

@app.route('/html_file')
def htmlPage():
    return render_template('file_01.html')

@app.route('/welcome_file/<name>')
def welcome_01(name):
    return render_template('welcome_file.html',myname=name)
app.run()