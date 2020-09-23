# from flask import render_template
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
#

# @app.route('/')
# def home():
#     return render_template('COVID_19.html')


from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('testindex.html', content='Béla', description='macska', mekkora='nagy')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'


## 1. lesson
# @app.route('/')
# def home():
#     return '<h1>Hello!</h1> COVID_19.html itt nem megy a html'
#
# @app.route('/<name>')
# def user(name):
#     return f'Hello {name}! '
#
# @app.route('/admin')
# def admin():
#     return redirect(url_for('user', name='Admin!'))

if __name__ == '__main__':
    app.run(debug=True)
