from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello dosto, welcome to DevOps priyank is hero in a devops and cloud engineering field '
 
@app.route('/health')
def health():
    return 'Server is up and running'
