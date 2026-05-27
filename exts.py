from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
#这个文件的存在意义是为了解决循环引用（项目初始化步骤）
db =SQLAlchemy()
mail = Mail()