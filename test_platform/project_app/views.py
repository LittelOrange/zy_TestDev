from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project,Module

# Create your views here.
@login_required  #判断用户是否登录
def project_manage(request):
    '''
    项目列表管理
    '''
    username = request.session.get('user','') #读取浏览器session
    # username = request.COOKIES.get('user','')  #读取浏览器cookie
    project_all = Project.objects.all
    return render(request, "project_manage.html",{
        "user":username,
        "projects":project_all,
        "type":"list"
    })


@login_required
def add_project(request):
    '''
    添加项目
    '''
    return render(request, "project_manage.html",
                  {"type":"add"},
                  )


