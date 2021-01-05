from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'chaudharyhamdanch@gmail.com'
app.config['MAIL_PASSWORD'] = 'ChH@mdan894'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
	msg = Message('Automatic Mail Send karna seekha apun ', sender= 'chaudharyhamdanch@gmail.com', recipients=['yourappsandgames@gmail.com'])
	msg.body = "Hello Guysss ! This mail is sent from Flask Mail Extension ... Fully Automated :)"
	mail.send(msg)
	return "Mail Sent"

if __name__ == '__main__':
	app.run(debug=True)

