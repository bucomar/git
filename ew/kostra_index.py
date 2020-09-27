from flask import Flask, redirect, url_for, render_template, request, session, send_file
import kostra_app

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('kostra_gen'))

@app.route('/download')
def download():
    path = 'kostra_68020_l.csv'
    return send_file(path, as_attachment=True)

@app.route('/kostra_gen', methods=['POST', 'GET'])
def kostra_gen():
    return render_template('kostra.html')
    if request.method == 'POST':
        # session.permanent = True
        # irc = request.form['rci']
        # session['irc'] = irc
        # local_rs_csv = kostra_app.local_rs_gen(irc)
        # return send_file(local_rs_csv, as_attachment=True)
        return redirect(url_for('download'))
    # else:
        # return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)


# def shutdown_server():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()
#
# @app.route('/down', methods=['POST'])
# def shutdown():
#     shutdown_server()
#     return 'Server shutting down...'
