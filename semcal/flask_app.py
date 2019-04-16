import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'This is python.semcal.org. time.time() returned {time.time()}'


if __name__ == '__main__':
    app.run()
