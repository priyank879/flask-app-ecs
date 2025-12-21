from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello bhaiyo, welcome to DevOps priyank is hero in a devops and cloud eng '
 
@app.route('/health')
def health():
    return 'Server is up and running'
