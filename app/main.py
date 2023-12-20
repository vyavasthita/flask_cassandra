from flask import Flask, Response
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


app = Flask(__name__)


@app.get("/")
def home():
    cluster = Cluster(['dse'])
    session = cluster.connect()

    return 'Raja Sharma'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)