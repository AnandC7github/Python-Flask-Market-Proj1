from flask import Flask

app = Flask('app')


@app.route('/')         # python decorators - What url in your website i am going to navigate through
def hello_world():
  return '<h1>Changed Text!!!</h1>'

@app.route('/about')
def about_page():
  return '<h1>About Page</h1>'

app.run(host='0.0.0.0', port=8080)
