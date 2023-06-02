from flask import Flask, url_for, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        return f'<h1>Welcome {request.values["user"]}!</h1>'
    return '<form method="post" action="/"><input type="text" name="user"><p><input type="password"><p><input type="submit" value="Submit"></form>'

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True)