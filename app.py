from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
	return "Hello World"

@app.route('/admin')
def admin():
	return "Hello Admin"

@app.route('/guest/<guest>')
def guest(guest):
	return "Hello %s as guest..."%guest

@app.route('/info')
def info():
	return "Made by Hamdan !!!"


@app.route('/user/<name>')
def home(name):
	if name == 'admin':
		return redirect(url_for('admin'))
	else:
		return redirect(url_for('guest',guest=name))

if __name__ == '__main__':
	app.run(debug=True)

