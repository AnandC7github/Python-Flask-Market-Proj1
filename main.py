from market import app

#checks if the run.py has executed directly and not imported 
if __name__ == '__main__':
  app.run(host="0.0.0.0", port=3000, debug=True)