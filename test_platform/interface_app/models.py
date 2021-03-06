from django.db import models
from project_app.models import Module
# Create your models here.
class TestCase(models.Model):
    """
    用例表
    """
    # project = models.ForeignKey(Project, on_delete = models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=100, blank=False, default = "")
    url = models.TextField("URL",default = "")
    req_method = models.CharField("请求方法", max_length=10, default="")
    req_type = models.CharField("参数类型", max_length=10, default="")
    req_header = models.TextField("Header", default="")
    req_parameter = models.TextField("参数", default="")
    response_assert = models.TextField("验证", default="")

    create_time = models.DateTimeField("创建时间", auto_now = True)

    def __str__(self):
        return self.name