import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("postgresql://postgres:GfNetsUGDSLmcrevlDTXKfKatziHNoCo@junction.proxy.rlwy.net:23638/railway", "sqlite:///local.db")  # Use Railway URL no .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False
