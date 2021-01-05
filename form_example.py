from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'hmaumsdkaann'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All Fields are required !!!')
			return render_template('contact.html', form = form)
		else:
			return render_template('success.html')

	if request.method == 'GET':
		return render_template('contact.html', form = form)

if __name__ == '__main__':
	app.run(debug=True)




