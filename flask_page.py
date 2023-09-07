from flask import Flask, redirect, url_for, render_template
# url_for and redirect redirect users to other webpages

app = Flask(__name__)

# @app.route('/') is what the user will navigate to using a URL
@app.route('/')
def home():
    return render_template('index.html')

# this is what actually starts the server
if __name__ == '__main__':
    app.run(debug=True)