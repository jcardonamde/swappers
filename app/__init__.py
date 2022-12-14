from flask import Flask, session
from flask_mail import Mail

app = Flask(__name__)
app.secret_key = "misuperclavesecreta12345***"
mail = Mail()

def create_app(config):
    app.config.from_object(config)
    mail.init_app(app)

    return app