# from flask import render_template
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
#

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('COVID_19.html')

if __name__ == '__main__':
    app.run(debug=Thrue)
