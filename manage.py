from flask_script import Manager, Server
from blog_app import app
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

manager = Manager(app)

manager.add_command('runserver', Server(
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 5000))
    )
)

if __name__ == '__main__':
    manager.run()