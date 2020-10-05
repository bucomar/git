# Flask sandbox.

from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/<szo>')
def echo(szo):
    return szo

@app.route('/<int:szam>')
def dupla(szam):
    return str(szam*2)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/upload', methods=['GET', 'POST'] )
def upload_file():
    if request.method == 'POST':
        f = request.files['the file']
        f.save('/var/www/uploads/uploaded_file.txt')
        return 'Fájl feltöltve'
    else:
        return 'Anyád!'



if __name__ == '__main__':
    app.run(debug=True)
