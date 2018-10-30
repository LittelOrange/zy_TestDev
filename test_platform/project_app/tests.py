from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from project_app.models import Project

# Create your tests here.

class ProjectTest(TestCase):
    """项目管理测试"""

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'abc123456')
        Project.objects.create(name = "测试平台项目", describe = "描述")
        self.client = Client()
        login_data = {'username': 'admin', 'password': 'abc123456'}
        response = self.client.post('/login_action/', data = login_data)

    def test_project_manage(self):
        """项目管理测试"""
        response = self.client.post('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        print(project_html)
        # self.assertEqual(response.status_code, 200)
        self.assertIn("退出",project_html)
        self.assertIn("测试平台项目", project_html)
