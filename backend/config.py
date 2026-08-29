# import os
# from dotenv import load_dotenv

# load_dotenv()


# class Config:
#     SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql+psycopg://"
#         f"{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
#         f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
#         f"/{os.getenv('DB_NAME')}"
#     )

#     SQLALCHEMY_TRACK_MODIFICATIONS = False


import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-fallback-key')

    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False