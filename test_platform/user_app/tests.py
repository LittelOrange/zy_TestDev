from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.
class UserModelsTest(TestCase):
    """用户测试"""
    def setUp(self):
        User.objects.create_user("test1","test1@mail.com","abc123456")

    def test_createuser(self):
        """新建用户"""
        User.objects.create_user("test2","test2@mail.com","abc123456")
        user = User.objects.get(username = "test2")
        self.assertEqual(user.username, "test2")
        self.assertEqual(user.email, "test2@mail.com")

    def test_queryuser(self):
        """查询用户"""
        user = User.objects.get(username = "test1")
        self.assertEqual(user.username, "test1")
        self.assertEqual(user.email, "test1@mail.com")

    def test_updateuser(self):
        """更新用户"""
        user = User.objects.get(username = "test1")
        user.username = "test2"
        user.email = "test2@mail.com"
        user.save()
        usern = User.objects.get(username="test2")
        self.assertEqual(usern.email, "test2@mail.com")

    def test_user_delete(self):
        """ 删除用户 """
        user = User.objects.get(username="test1")
        user.delete()
        user = User.objects.filter(username="test1")
        self.assertEqual(len(user), 0)


class IndexPageTest(TestCase):
    """登录页测试"""

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        # print(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)   #请求成功的状态码为200
        self.assertTemplateUsed(response, 'index.html')


class LoginTest(TestCase):
    """登录动作测试"""

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'abc123456')
        self.client = Client()

    def test_login_null(self):
        """用户名密码为空"""
        login_data = {'username': '', 'password': ''}
        response = self.client.post('/login_action/', login_data)
        # print(response.context)    #这个也可以打印出来内容
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或者密码为空", login_html)


    def test_login_error(self):
        """用户名密码错误"""
        login_data = {'username': 'admin', 'password': '1832332'}
        response = self.client.post('/login_action/', login_data)
        # print(response.context)    #这个也可以打印出来内容
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码错误", login_html)


    def test_login_sucess(self):
        """登录成功"""
        login_data = {'username': 'admin', 'password': 'abc123456'}
        response = self.client.post('/login_action/', login_data)
        # response = self.client.post('/login_action/', data =login_data)    #这样也可以
        # print(response.context)    #这个也可以打印出来内容
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 302)








































