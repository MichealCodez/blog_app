from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')

from blog import views
from author import views