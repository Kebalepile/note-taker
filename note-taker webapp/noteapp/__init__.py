import os 
from uuid import uuid4
from flask import Flask

def create_app():
    app = Flask(
    __name__, 
    instance_relative_config=True,
     template_folder="./static/views")
    app.config.from_mapping(
        SECRET_KEY=uuid4(),
        # DATABASE=os.path.join(app.instance_path,
        #                      'note_app.sqlite')
    )
    try:
         os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import routes
    from . import pwa
    # from . import auth
    # from . import db

    app.register_blueprint(pwa.bp)
    app.register_blueprint(routes.bp)
    # app.register_blueprint(auth.bp)
    # db.init_app(app)

    return app

