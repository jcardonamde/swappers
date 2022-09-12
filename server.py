from app import create_app
from app.controllers import users_controller
from config import config

config_class = config['development']
app = create_app(config_class)

if __name__ == "__main__":
    app.run()