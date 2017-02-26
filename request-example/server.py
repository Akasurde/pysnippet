import os
from flask import Flask, request, jsonify, redirect, session, url_for
from werkzeug.utils import secure_filename
import const

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = const.temp
app.secret_key = 'WHILEYOUREADTHISIWILLHACKYOU'

@app.route('/example1/')
def handle_index():
    return "Hello World from requests"

@app.route('/example1/json')
def handle_index_json():
    userdict = {'username': const.username, 'password': const.password}
    return jsonify(userdict)

@app.route('/example2/json', methods=['POST'])
def handle_example_post():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        print username, password
        return jsonify({"status": "OK", "msg": "User verified"})

@app.route('/example4/', methods=['POST'])
def example_4_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({"status": "OK", "msg": "File uploaded "
                                                   "successfully"})

@app.route('/example6/index')
def example_6_index():
    if 'username' in session:
        username = session['username']
        return jsonify({"status": "OK", "msg": "You are {0}".format(username)})
    return jsonify({"status": "NOTOK", "msg": "Please Login"})

@app.route('/example6/login', methods=['POST'])
def example_6_login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('example_6_index'))

@app.route('/example6/logout')
def example_6_logout():
    session.pop('username', None)
    return redirect(url_for('example_6_index'))

if __name__ == "__main__":
    app.run(port=int(const.port))

