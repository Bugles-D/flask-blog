from functools import wraps
from flask import g, redirect, url_for


def login_required(fun):

    @wraps(fun)#保留fun的信息
    def inner(*args,**kwargs):
         if g.user:
             print("正常执行原函数")
             return fun(*args,**kwargs)
         else:
             return redirect(url_for("auth.login"))

    return inner