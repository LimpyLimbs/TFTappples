from flask import Flask, redirect, url_for
# url_for and redirect redirect users to other webpages

app = Flask(__name__)

# @app.route('/') is what the user will navigate to using a URL
@app.route('/')
def home():
    return 'Hello! this is the main page <h1>HELLO<h1>'

# @app.route('/<name>') is a way to pass a variable from the URL to the function
@app.route('/<name>')
def user(name):
    return f'Hello {name}'

# this is a redirect
# you have to put the function name in url_for not the route
@app.route('/admin')
def admin():
    return redirect(url_for('home'))

# this is what actually starts the server
if __name__ == '__main__':
    app.run(debug=True)