__author__ = 'Mrsong'

from flask import  Flask
from flask_bootstrap import Bootstrap
from app.config import config
from flask_login import LoginManager

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
   # app = Flask(__name__,
   #             static_folder="../dist/static",
  #              template_folder="../dist"
   #             )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)

    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth/')
    return app