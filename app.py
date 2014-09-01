from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/submit', methods=['POST'])
def submit():
  street = request.form['street']
  unit = request.form['unit']
  city = request.form['city']
  email = request.form['email']

  return ('Received:<br />' +
    street + '<br />' +
    unit + '<br />' +
    city + '<br />' +
    email )

if __name__ == '__main__':
  # TODO: remove before pushing to server 
  app.debug = True
  app.run()
