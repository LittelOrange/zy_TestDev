from django.db import models

# Create your models here.
#table = class  一张表对应一个类
#变量 = 字段（类型、长度）  一个字段对应表里边的字段(id和create_time一般每张表都必须)
class Project(models.Model):      #实际数据库里边的表名为user_app_project,会自动带上项目名
    """
    项目表
    """
    #查看django里边自带的类型：C:\Python37\Lib\site-packages\django\db\models\fields\__init__.py文件
    #django为每张表自动生成一个id，所以不需再创建id

    name = models.CharField("名称",max_length = 100, blank = False, null = True)    #此处不加名段名“名称”，会自动用字段名name
    describe = models.TextField("描述", default = "")
    status = models.BooleanField("状态", default = True)
    create_time = models.DateTimeField("创建时间", auto_now_add = True)

    def __str__(self):
        return self.name


class Module(models.Model):
    """
    模块表
    """
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    name = models.CharField("名称",max_length=100, blank=False, default = "")
    describe = models.TextField("描述", default= "")
    create_time = models.DateTimeField("创建时间", auto_now = True)

    def __str__(self):
        return self.name