from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world !'


@app.route('/first_seen')
def first_seen():
    return render_template('first_seen.html')


@app.route('/first')
def redirect_url_for():
    return redirect(url_for('first_seen'))




@app.route('/second_seen')
def second_seen():
    return render_template('second_seen.html')


@app.route('/second')
def x():
    return redirect('/second_seen')


if __name__ == '__main__':
    app.run(debug=True)
