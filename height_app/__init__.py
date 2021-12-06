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

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://gqaykyrqekaaqo:fc0ccbec140035513e457fecde738273d4750450e2d47de1a22e85fec18e95ce@ec2-34-225-103-117.compute-1.amazonaws.com:5432/d8uluv6ocm72vm"
    
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from height_app.routes import main_route,users_route
    app.register_blueprint(main_route.bp)
    app.register_blueprint(users_route.bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()