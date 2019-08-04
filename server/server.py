from flask import Flask, send_from_directory
app = Flask(__name__)


@app.route('/dock')
def hello():
    return send_from_directory(directory="/data/static/", filename='text.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
