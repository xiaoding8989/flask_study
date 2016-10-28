from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html',title="flask_basic")

@app.route('/about')
def about():
    return "I am about....."

@app.route('/project/')
def projects():
    return "The project page"

@app.route('/services')
def services():
    return "I am serviecs....."

if __name__ == '__main__':
    app.run(debug=True)
