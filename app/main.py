from flask import Flask, Response


app = Flask(__name__)


@app.get("/")
def home():
    return 'Raja Sharma'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)