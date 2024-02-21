@app.route('/')  # python decorators - What url in your website i am going to navigate through
@app.route('/home')
def home_page():
return render_template('home.html')


@app.route('/market')
def market_page():
items = Item.query.all()
return render_template('market.html', items=items)


if __name__ == '__main__':

#DATA-BASE CODE HERE --------------------------
with app.app_context():
  # # drop the database tables
  # db.drop_all()
  # # create database and table
  # db.create_all()

  app.run(host='0.0.0.0', port=3000, debug=True)