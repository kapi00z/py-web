from flask import Flask, jsonify
import books, json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

@app.route('/books')
def bookList():
    with open(f"{books.bookDir}/books.json", 'r') as file:
        data = json.loads(file.read())
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)