from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', myname=name)

@app.route('/mk/moksh')
def names():
    return 'second page aagya'

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

app.run()