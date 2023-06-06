from blog_app import app

@app.route('/')
def home():
    return 'Hey Flask Blog!'