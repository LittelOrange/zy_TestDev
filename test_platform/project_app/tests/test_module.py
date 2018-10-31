from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from project_app.models import Project,Module


class ModuleTest(TestCase):
    """模块管理测试"""

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'abc123456')
        project = Project.objects.create(name="测试平台项目1", describe="描述1")
        Module.objects.create(project = project.name, name ="模块1", describe = "模块1的描述")
        self.client = Client()
        login_data = {'username': 'admin', 'password': 'abc123456'}
        response = self.client.post('/login_action/', data = login_data)

    def test_project_manage(self):
        """项目管理测试"""
        response = self.client.post('/manage/module_manage/')
        module_html = response.content.decode("utf-8")
        print(module_html)
        # self.assertEqual(response.status_code, 200)
        # self.assertIn("退出",project_html)
        self.assertIn("模块1", module_html)



    # def test_module_query(self):
    #     """查询项目"""
    #     module = Module.objects.get(name = "模块1")
    #     self.assertEqual(module.name, "模块1")
    #     self.assertEqual(module.describe, "模块1的描述")
    #
    # def test_module_update(self):
    #     """更新项目"""
    #     module = Module.objects.get(name="模块1")
    #     module.name = "模块2"
    #     module.describe = "更改模块1的描述"
    #     module.save()
    #     module2 = Module.objects.get(name="模块2")
    #     self.assertEqual(module2.describe, "更改模块1的描述")
    #
    # def test_pmodule_delete(self):
    #     """ 删除模块 """
    #     module = Module.objects.get(name="模块2")
    #     module.delete()
    #     module = Module.objects.filter(name="模块2")
    #     self.assertEqual(len(module), 0)