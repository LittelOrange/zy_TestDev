from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from project_app.models import Project,Module
from .forms import ProjectForm


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


# @login_required
# def add_project(request):
#     '''
#     添加项目
#     '''
#     return render(request, "project_manage.html",
#                   {"type":"add"},
#                   )


@login_required
def add_project(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()

    return render(request,
                  "project_manage.html",{
                      'form':form,
                      "type":"add",
                  })
