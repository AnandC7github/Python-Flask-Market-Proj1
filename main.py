from flask import Flask

app = Flask('app')


@app.route('/')         # python decorators - What url in your website i am going to navigate through
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)
