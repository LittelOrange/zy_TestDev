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
        print(parameter)

        # payload = json.loads(parameter.replace("'", "\""))
        # print(payload)
        # print(type(payload))

        # if method == "get":
        #     r = requests.get(url,params=parameter)
        # if method == "post":
        #     r = requests.post(url,json=parameter)
        # print(r.text)
        # return HttpResponse("ok")



