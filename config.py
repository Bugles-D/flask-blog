HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE =  'newbd'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = f'mysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
SQLALCHEMY_DATABASE_URI = DB_URI

#配置邮箱（这是指发送方）
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "957261510@qq.com"
#qq邮箱的授权码
MAIL_PASSWORD = "aamemfkdibkgbgaa"
MAIL_DEFAULT_SENDER = "957261510@qq.com"

#在app.py设置同理 app.secret_key = '123asdcxvsdfa'
SECRET_KEY = "12asdzxcvasfasdfa"