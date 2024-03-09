from flask import Flask, request
import db, os

if os.getenv('FLASK_PORT') is None:
    PORT = 3000
else:
    PORT = os.getenv('FLASK_PORT')

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

@app.route('/db/<name>', methods = ['GET', 'POST'])
def webDB(name):
    if request.method == 'GET':
        data, path = db.load(name)
        return data
    if request.method == 'POST':
        args = request.get_json(force=True)
        db.update(name, args)
        return args

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)