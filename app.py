from flask import Flask, session,g
import config
from exts import *
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

# 项目初始化的一系列操作
app = Flask(__name__)
#绑定配置
app.config.from_object(config)
#db绑定app
db.init_app(app)
mail.init_app(app)
#第二节的步骤，绑定app和SQAlchemy()
"""        terminal执行
1.python -m flask db init  只需要执行第一次
2.python -m flask db migrate
3,python -m flask db upgrade 
"""
migrate = Migrate(app,db)



#注册
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


#钩子函数hook，中间拦截一下。before_request/before_first_request/after_request
#请求到达视图函数前，拦截一下
@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    #给g函数
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)

@app.context_processor
def my_context_processor():
    return {"user":g.user}


if __name__ == '__main__':
    app.run('0.0.0.0')