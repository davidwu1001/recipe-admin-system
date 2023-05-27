#配置文件
SECRET_KEY= "sajfasjkfaksjfbajb"

# admin主题
FLASK_ADMIN_SWATCH = 'cerulean'
#mysql 开发环境
# HOSTNAME = "127.0.0.1"
# PORT = 3306
# USERNAME = "root"
# PASSWORD = "root"
# DATABASE = "flask-admin-test"
# SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
# mysql 生产环境
HOSTNAME = "49.233.27.20"
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "flask_admin_test"
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
# 管理系统主题
FLASK_ADMIN_SWATCH = 'cerulean'

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
# 设置相应的登录和注册URL
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SQLALCHEMY_TRACK_MODIFICATIONS = False