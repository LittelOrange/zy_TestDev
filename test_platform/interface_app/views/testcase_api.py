import json
import requests
from test_platform import common
from interface_app.models import TestCase
from project_app.models import Project, Module


# Create your views here.
#获取项目的模块列表
def get_project_list(request):
    """
    获取项目模块列表
    :param request:
    :return: 项目接口列表
    """
    if request.method == "GET":
        project_list = Project.objects.all()
        data_list = []
        for project in project_list:
            project_dict = {
                "name": project.name
            }
            module_list = Module.objects.filter(project_id=project.id)
            if len(module_list) != 0:
                module_name = []
                for module in module_list:
                    module_name.append(module.name)

                project_dict["moduleList"] = module_name
                data_list.append(project_dict)
        return common.response_succeed(data=data_list)
    # return JsonResponse({"success": "true", "data": dataList})
    else:
        return common.response_failed("请求方法错误")



#获取接口信息
def get_case_info(request):
    """
    获取接口数据
    :param request:
    :return:
    """
    if request.method == "POST":
        case_id = request.POST.get("caseId","")
        print(case_id)
        if case_id == "":
            # return JsonResponse({"success":"false","message":"case is NULL."})
            return common.response_failed("用例id为空")

        case_obj = TestCase.objects.get(pk = case_id)
        # print("模块id:",case_obj.module_id)
        # mid = case_obj.module_id
        # module_obj = Module.objects.get(id = mid)
        module_obj = Module.objects.get(id=case_obj.module_id)

        module_name = module_obj.name   # 模块名称
        # pid = module_obj.project_id
        # # print("项目ID",pid)
        # project_obj=Project.objects.get(id = pid)
        # project_name = project_obj.name
        project_name = Project.objects.get(id=module_obj.project_id).name  # 项目名称

        case_info ={
            "module_name":module_name,
            "project_name":project_name,
            "name":case_obj.name,
            "url": case_obj.url,
            "reqMethod": case_obj.req_method,
            "reqType":case_obj.req_type,
            "reqHeader": case_obj.req_header,
            "reqParameter": case_obj.req_parameter,
            "assertText": case_obj.rep_assert,
        }
    #     return JsonResponse({"success": "true", "message": "ok","data":case_info})
    #
    # else:
    #     return HttpResponse("404")
        return common.response_succeed(data=case_info)
    else:
        return common.response_failed("请求方法错误")



# 调试接口
def api_debug(request):
    """
    HTTP接口调试
    :param request:
    :return: 接口调用结果
    """

    if request.method == "POST":
        url = request.POST.get("req_url","")
        method = request.POST.get("req_method","")
        parameter = request.POST.get("req_parameter","")
        type_ = request.POST.get("req_type", "")

        if url == "" or method == "" or type_ == "":
            return common.response_failed("必传参数为空")

        # payload = json.loads(parameter)
        payload = json.loads(parameter.replace("'", "\""))  # loads()：将字符串转换为字典;replace()：将单引号替换为双引号

        if method == "get":
            if type_ == "from":
                r = requests.get(url, params=payload)  # 此处必须为requests，不能乱写，是导入的包
            else:
                return common.response_failed("参数类型错误")

        if method == "post":
            if type_ == "from":
                r = requests.post(url, data=payload)
            elif type_ == "json":
                r = requests.post(url, json=payload)
            else:
                return common.response_failed("参数类型错误")
        # print(r.text)
        # return HttpResponse(r.text)

        return common.response_succeed(data=r.text)
    else:
        return common.response_failed("请求方法错误")

#保存测试用列
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
        module_name = request.POST.get("module", "")
        assert_text = request.POST.get("assert_text", "")

        if url == "" or method == "" or req_type == "" or module_name == "":
            # return HttpResponse("必传参数为空")
            return common.response_failed("必传参数为空")

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
                                       req_parameter=parameter,
                                       rep_assert=assert_text
                                       )
        if case is not None:
            # return HttpResponse("保存成功！")
            return common.response_succeed("保存成功！")


    else:
        return HttpResponse("请求方法错误")
        # return common.response_failed("请求方法错误")


#验证预期结果
def api_assert(request):
    """
    对测试用例的断言进行验证
    :param request:
    :return:
    """
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        if result_text=="" or assert_text =="":
            # return JsonResponse({"success":"false",message:"验证的数据不能为空"})
            return common.response_failed("验证的数据不能为空")
        try:
            assert assert_text in result_text
        except AssertionError:
    #         return JsonResponse({"success": "false", message: "验证失败"})
    #     else:
    #         return JsonResponse({"success": "false", message: "验证通过"})
    # else:
    #     return HttpResponse("404")
            return common.response_failed("验证失败!")
        else:
            return common.response_succeed("验证成功!")
    else:
        return common.response_failed("请求方法错误")


#更新接口
def update_case(request):
    """
    更新接口测试用例
    :param request:
    :return:
    """
    if request.method == "POST":
        case_id = request.POST.get("cid", "")
        name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        module_name = request.POST.get("module", "")
        assert_text = request.POST.get("assert_text", "")
        print("接口id", case_id)

        if url == "" or method == "" or req_type == "" or module_name == "" or assert_text == "":
            return common.response_failed("必传参数为空")

        if parameter == "":
            parameter = "{}"

        if header == "":
            header = "{}"

        module_obj = Module.objects.get(name=module_name)
        case_obj = TestCase.objects.filter(id=case_id).update(
                module=module_obj,
                name=name,
                url=url,
                req_method=method,
                req_header=header,
                req_type=req_type,
                req_parameter=parameter,
                rep_assert=assert_text
            )
        if case_obj == 1:
            return common.response_succeed("更新成功！")
        else:
            return common.response_failed("更新失败！")
    else:
        return common.response_failed("请求方法错误")


