import os
from flask import Flask
from src.auth import auth
from src.bookmarks import bookmarks
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
   

    if test_config is None:
        # load the instance config, if it exists, when not testing
       app.config.from_mapping(
        SECRET_KEY= os.environ.get('SECRET_KEY')
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        
   
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Application Factory Function'
    app.register_blueprint(auth,url_prefix="/api/auth")
    app.register_blueprint(bookmarks,url_prefix="/api/v1/bookmarks")
    return app