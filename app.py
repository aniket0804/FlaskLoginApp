from flask import Flask, render_template, redirect, request, session, abort, flash
import os
app = Flask(__name__)

@app.route('/')
def main():
	return render_template('layout.html')


@app.route('/home')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('home.html',msg="You're logged in",user=session.get('inputEmail'))


@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		if request.form['inputPassword'] == 'aniket' and request.form['inputEmail'] == 'aniket@devils.com':
			session['logged_in'] = True
			session['inputEmail'] = request.form['inputEmail'].split('@')[0]
			return redirect('/home')
		else:
			flash('wrong password!')
	return home()


@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route("/logout")
def logout():
	session['logged_in'] = False
	return home()


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)
