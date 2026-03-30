import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
    
    url = os.environ.get("DATABASE_URL")
    data_file = "sqlite:///" + os.path.join(BASE_DIR, "instance", "expense_tracking_system.db")
    
    SQLALCHEMY_DATABASE_URI = (url or data_file)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    