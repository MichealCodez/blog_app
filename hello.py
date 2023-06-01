import os
import pdb
from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    # pdb.set_trace()
    return "Hello Flask!"

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)