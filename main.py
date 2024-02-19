from flask import Flask, render_template, request, redirect, url_for

app = Flask('app')


@app.route('/')         # python decorators - What url in your website i am going to navigate through
@app.route('/home')
def home_page():
  return render_template('home.html')

app.run(host='0.0.0.0', port=8080)
