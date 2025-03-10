from flask import Flask
import os

print(os.getcwd())

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=port)