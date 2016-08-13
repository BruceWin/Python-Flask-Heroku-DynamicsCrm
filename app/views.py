from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"

@app.route('/')
@app.route('/peter')
def peter():
    return "Peter"
