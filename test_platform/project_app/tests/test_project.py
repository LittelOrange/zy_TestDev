from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from project_app.models import Project

# Create your tests here.



class ProjectTest(TestCase):
    """项目管理测试"""

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'abc123456')
        Project.objects.create(name = "测试平台项目1", describe = "描述1")
        self.client = Client()
        login_data = {'username': 'admin', 'password': 'abc123456'}
        response = self.client.post('/login_action/', data = login_data)

    def test_project_manage(self):
        """项目管理测试"""
        response = self.client.post('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        # print(project_html)
        # self.assertEqual(response.status_code, 200)
        self.assertIn("退出",project_html)
        self.assertIn("测试平台项目", project_html)



    def test_project_query(self):
        """查询项目"""
        project = Project.objects.get(name = "测试平台项目1")
        self.assertEqual(project.name, "测试平台项目1")
        self.assertEqual(project.describe, "描述1")

    def test_project_update(self):
        """更新项目"""
        project = Project.objects.get(name="测试平台项目1")
        project.name = "测试平台项目2"
        project.describe = "改了描述内容"
        project.save()
        project2 = Project.objects.get(name="测试平台项目2")
        self.assertEqual(project.describe, "改了描述内容")

    def test_project_delete(self):
        """ 删除项目 """
        project = Project.objects.get(name="测试平台项目1")
        project.delete()
        project = Project.objects.filter(name="测试平台项目1")
        self.assertEqual(len(project), 0)

    def test_add_project(self):
        """测试增加项目"""
        Project.objects.create(name="测试平台项目2", describe="项目2描述")
        project = Project.objects.get(name="测试平台项目2")
        self.assertEqual(project.name, '测试平台项目2')
        self.assertEqual(project.describe, '项目2描述')




