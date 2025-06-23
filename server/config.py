class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:pharaoh@localhost:5432/show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-key"
