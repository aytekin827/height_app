from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app controller part

migrate = Migrate()
db = SQLAlchemy()

def create_app():
    """
    create_app 함수는 어플리케이션 펙토리에 따른 패턴입니다. controller
    """
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5433/worldcup"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from height_app.routes import main_route,users_route
    app.register_blueprint(main_route.bp)
    app.register_blueprint(users_route.bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()