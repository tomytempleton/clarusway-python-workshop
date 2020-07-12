from flask import Flask
app = Flask(___name___)
@app.route(/)
def home()
   return 'This is home page for no path, <h1> Wellcome Home</h1>'
@app.route('/about')
def about
   return '<h1> This is my about page </h1></h1>'
@app.route('/error')
def error():
    return '<h1>Either you encountered an error or you are not authorized.</h1>'
@app.route('/hello')
def hello():
    return '<h1>Hello, World! </h1>'