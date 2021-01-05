from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'hmaumsdkaann'

@app.route('/')
def index():
	return render_template('index1.html')

@app.route('/login',methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or \
		request.form['password'] != 'admin':
			error = 'Invalid Username or Password!!! Please try again...'
		else:
			flash('You were successfully logged in')
			flash('log out before login again')
			return redirect(url_for('index'))
	return render_template('log_in.html', error=error)

if __name__ == '__main__':
	app.run(debug=True)




