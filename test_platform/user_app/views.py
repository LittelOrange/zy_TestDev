from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# from user_app.models import Project,Module

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
                # response = HttpResponseRedirect("/project_manage/")
                # # response.set_cookie('user', username, 3600) #添加浏览器cookie
                # return response

                return HttpResponseRedirect("/manage/project_manage/")
            else:
                return render(request, "index.html",
                              {"error": "用户名或密码错误"}
                              )
    else:
        return render(request, "index.html")


@login_required
def logout(request):
    """
        退出登录
    :param request:
    :return:
    """
    auth.logout(request)  #清除用户的登录状态
    response = HttpResponseRedirect("/")
    return response






