from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, From Flask!'

@app.route('/auth')
def auth_handling():
    return "<h1>Login Page</h1><h2>Some thing</h2>"

if __name__ == "__main__":
    app.run(debug=True, port=9000)
