import random
import string
import time
from flask import Blueprint, request, jsonify, redirect, url_for,session
from flask import render_template
from flask_mail import Message
from werkzeug.security import generate_password_hash,check_password_hash #防止数据库被盗，黑客去撞库

from .forms import RegisterForm, LoginForm

from models import EmailCapchaModel, UserModel
from exts import *

#url_prefix就像建立了一个文件夹一样
bp = Blueprint('auth',__name__,url_prefix='/auth')


#创建视图
@bp.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email =form.email.data
            password =form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱没有注册")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password,password):
                session['user_id']=user.id
                return redirect("/")

        else:
            print(form.errors)
            return redirect(url_for("logout"))

@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@bp.route('/register',methods=["GET","POST"])
def register():
    #1.验证用户提交的邮箱和验证码对应是否正确
    #2.表单验证flask-wtf
    if request.method == "GET":
        return render_template('register.html')
    else:
        #像一个合格的门卫一样，检查信息是否准确，准确了才能注册
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = UserModel(email=email,username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            time.sleep(1)
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("register"))

@bp.route('/captcha/email')
def get_email_captcha():
    """从邮箱中获取验证码"""
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source,4)#生成的是列表
    str = "".join(captcha)
    print(str)
    message = Message(subject='万丈的注册验证码', recipients=[email], body=f"您的验证码是：{str}，请在10分钟内登录。")
    mail.send(message)
    #为了后面验证，需要把邮箱和验证码放入临时数据库去
    email_captcha = EmailCapchaModel(email=email,capcha=str)
    db.session.add(email_captcha)
    db.session.commit()
    #RESTful API
    #{code:200/400/500,message:'',data:{}}
    return jsonify({"code": 200, "message": "", "data": None})

@bp.route('/mail/test')
def mail_test():
    """这个可以绑定到发送邮件"""
    #这是接收方
    message = Message(subject='message邮箱测试',recipients=["riajeh@edbnu.com"],body="这是第一次测试邮件")
    mail.send(message)
    return f'邮件发送成功：{message}'