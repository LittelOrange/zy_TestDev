import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from interface_app.forms import TestCaseForm
from interface_app.models import TestCase
from project_app.models import Project, Module
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
#用例列表
def case_manage(request):
    testcases = TestCase.objects.all()
    paginator = Paginator(testcases, 5) #每页显示5条数据

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)

    if request.method == "GET":
        return render(request,"case_manage.html",
                      {"type": "list",
                       "testcases":contacts,
        })
    else:
        return HttpResponse("404")

#按“用例名称”搜索用例
def search_case_name(request):

    if request.method == "GET":
        case_name = request.GET.get('case_name', "")
        cases = TestCase.objects.filter(name__contains=case_name)

        paginator = Paginator(cases, 5)  #每页显示5条数据
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # 如果页数不是整型, 取第一页.
            contacts = paginator.page(1)
        except EmptyPage:
            # 如果页数超出查询范围，取最后一页
            contacts = paginator.page(paginator.num_pages)

        return render(request,"case_manage.html",
                      {"type": "list",
                       "testcases":contacts,
                       "case_name": case_name,
        })
    else:
        return HttpResponse("404")





#创建/tiaoshi接口
def debug(request):
    form = TestCaseForm()
    if request.method == "GET":
        return render(request,"api_debug.html",
                      {"form":form,
                       "type": "debug",
        })
    else:
        return HttpResponse("404")

#调试接口
def api_debug(request):

    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")
        
        # payload = json.loads(parameter)
        payload = json.loads(parameter.replace("'", "\""))   #loads()：将字符串转换为字典;replace()：将单引号替换为双引号

        if method == "get":
            r = requests.get(url,params=payload)  #此处必须为requests，不能乱写，是导入的包
        if method == "post":
            r = requests.post(url,data=payload)
        # print(r.text)
        return HttpResponse(r.text)



def save_case(request):
    """
    保存测试用例
    """
    if request.method == "POST":
        name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        mid = request.POST.get("module", "")

        if url == "" or method == "" or req_type == "" or mid == "":
            return HttpResponse("必传参数为空")

        if parameter == "":
            parameter = "{}"

        if header == "":
            header = "{}"

        module_obj = Module.objects.get(name=module_name)

        case = TestCase.objects.create(name=name,
                                       module=module_obj,
                                       url=url,
                                       req_method=method,
                                       req_header=header,
                                       req_type=req_type,
                                       req_parameter=parameter
                                       )
        if case is not None:
            return HttpResponse("保存成功！")

    else:
        return HttpResponse("404")