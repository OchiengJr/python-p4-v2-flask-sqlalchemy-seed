# server/app.py

import os
from flask import Flask
from flask_migrate import Migrate
from models import db

# Create a Flask application instance 
app = Flask(__name__)

# Load configuration from environment variables or a configuration file
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'replace_this_with_a_secure_random_key')

# Initialize SQLAlchemy and Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Additional configuration and setup can go here

# Handle application-level errors
@app.errorhandler(500)
def internal_server_error(error):
    return '500 Internal Server Error', 500

@app.errorhandler(404)
def not_found_error(error):
    return '404 Not Found', 404

# Start the Flask application server if this file is run directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)

