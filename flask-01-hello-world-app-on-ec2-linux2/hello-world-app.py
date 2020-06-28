from flask import Flask

app = Flask(___name__)

@app.route('/')
def hello():
    return 'Hello World from Tomy'

print('name of this app....: ', ___name___)

if ___name___=='___main___':
    app.run(debug=True)