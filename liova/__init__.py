from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'change-me'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///liova.db'

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth_bp
    from .email import email_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(email_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/packages')
    def packages():
        return render_template('packages.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/faq')
    def faq():
        return render_template('faq.html')

    @app.route('/support')
    def support():
        return render_template('support.html')

    return app
