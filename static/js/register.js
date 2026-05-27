//alert("register.js")弹窗
//整个网页加载完毕后再执行
function bindEmailCaptchaClick(){
 $("#captcha-btn").click(function(event){// ‘#’ 相当于属性id
       //$this代表当前按钮的jQuery对象
       var $this = $(this)
       //阻止默认事件（提交表单的事件）
       event.preventDefault();
       //获取框框里的值
       var email = $("input[name='email']").val();
//       alert(email)
       $.ajax({//通过jQuery的ajax来执行 发送邮箱验证码的蓝图
                url:"/auth/captcha/email?email="+email,//必须要写完整的路径
                method:"GET",
                //回调函数
                success:function(result){
                    var code = result['code'];
                    if(code ==200){
                        //关闭按钮的点击事件
                        $this.off("click")
                        var countdown = 100;
                        //setInterval函数
                        var timer = setInterval(function(){
                                //将数字绑定到按钮的文本内
                                $this.text(countdown);
                                countdown-=1;
                                if (countdown == 0){
                                        //如果计数时间为0了，清空计时器函数
                                        clearInterval(timer);
                                        $this.text("获取验证码");
                                        //重新绑定这个事件
                                        bindEmailCaptchaClick();
                                }
                        },1000);
                    }else{
                        alert(result['message']);
                    }
//                    console.log(result);
                    },
                fail:function(error){console.log(error);}
       })
   });
}

$(function (){
  bindEmailCaptchaClick();
})
