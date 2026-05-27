import wtforms
from wtforms.validators import Email,Length,EqualTo,InputRequired
from models import UserModel,EmailCapchaModel
from exts import db

# 用来验证前端提交的数据是否符合要求(表单验证器)
class RegisterForm(wtforms.Form):
        email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
        captcha = wtforms.StringField(validators=[Length(min=4,max=4,message="验证码格式错误")])
        username = wtforms.StringField(validators=[Length(min=3,max=20,message="用户名格式错误")])
        password = wtforms.StringField(validators=[Length(min=6,max=20,message="密码格式错误")])
        password_confirm = wtforms.StringField(validators=[EqualTo("password",message="两次密码不一致")])

        #自定义验证：
        #邮箱是否被注册了
        #验证码是否正确
        def validate_email(self,filed):
            email = filed.data
            user = UserModel.query.filter_by(email=email).first()
            if user:
                raise wtforms.ValidationError(message="该邮箱已经被注册")

        def validate_captcha(self, filed):
            captcha = filed.data
            email = self.email.data
            captcha_model = EmailCapchaModel.query.filter_by(email=email,capcha=captcha).first()
            if not captcha_model:
                raise wtforms.ValidationError(message="邮箱验证码错误！")


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码错误")])

class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3,max=100,message="输入的内容太少或太多")])
    content = wtforms.StringField(validators=[Length(min=1,message="内容有错误")])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=1,message="内容有错误")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须要传入问题id")])