import json
import requests

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def case_manage(request):
    if request.method == "GET":
        return render(request,"case_manage.html",
                      {"type": "list"
        })
    else:
        return HttpResponse("404")


#创建接口
def debug(request):
    if request.method == "GET":
        return render(request,"api_debug.html",
                      {"type": "debug"
        })
    else:
        return HttpResponse("404")

#调试接口
def api_debug(request):
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")
        # print(parameter)
        # print(type(parameter))
        # payload = json.loads(parameter)
        payload = json.loads(parameter.replace("'", "\""))
        # print(payload)
        # print(type(payload))

        if method == "get":
            r = requests.get(url,params=payload)  #此处必须为requests，不能乱写，是导入的包
        if method == "post":
            r = requests.post(url,data=payload)
        print(r.text)
        return HttpResponse(r.text)
    else:
        return render(request,"api_debug.html",
                      {"type": "debug"
        })



