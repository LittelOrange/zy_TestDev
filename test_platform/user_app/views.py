from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, "index.html")

#处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "index.html",
                          {"error": "用户名或者密码为空"}
                          )
        else:
            user = auth.authenticate(username = username,password = password)

            if user is not None:
                auth.login(request, user)#记录用户登录状态
                request.session['user'] = username
                response = HttpResponseRedirect("/project_manage/")
                # response.set_cookie('user', username, 3600) #添加浏览器cookie
                return response

                # return render(request, "project_manage.html",{"user": user })
            else:
                return render(request, "index.html",
                              {"error": "用户名或密码错误"}
                              )


def project_manage(request):
    username = request.session.get('user','') #读取浏览器session
    # username = request.COOKIES.get('user','')  #读取浏览器cookie
    return render(request, "project_manage.html",{"user":username})






