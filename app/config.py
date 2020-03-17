from app.secrets import SECRET_KEY, MAIL_USER, MAIL_PASS


class Config:
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = MAIL_USER
    MAIL_PASSWORD = MAIL_PASS
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/site.db'
