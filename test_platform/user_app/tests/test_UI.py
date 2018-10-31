from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project

class LoginTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        """初始化数据"""
        User.objects.create_user("admin", "admin@mail.com", "admin@123456")
        Project.objects.create(name="测试平台项目", describe="描述")

    def test_login(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('')
        self.driver.find_element_by_id('LoginButton').click()
        error_hint = self.driver.find_element_by_id("error").text
        # print(error_hint)
        self.assertEqual("用户名或者密码为空",error_hint)

    def test_login_error(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("test11")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("abcde")
        sleep(1)
        self.driver.find_element_by_id('LoginButton').click()
        error_hint = self.driver.find_element_by_id("error").text
        # print(error_hint)
        self.assertEqual("用户名或密码错误", error_hint)

    def test_login_success(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("admin")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("admin@123456")
        sleep(1)
        self.driver.find_element_by_id('LoginButton').click()
        error_hint = self.driver.find_element_by_class_name("navbar-brand").text
        print(error_hint)
        self.assertEqual("测试平台", error_hint)



class ProjectManageTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.driver = Chrome()
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        super().tearDownClass()
        # pass

    def setUp(self):
        """登录"""
        User.objects.create_user("admin", "admin@mail.com", "admin@123456")
        Project.objects.create(name="测试平台项目1", describe="描述1")
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.driver.find_element_by_name("username").send_keys('admin')
        self.driver.find_element_by_name("password").send_keys('admin@123456')
        sleep(3)
        self.driver.find_element_by_id("LoginButton").click()

    def test_select_project(self):
        """查询"""
        name = self.driver.find_element_by_id("list").text
        print(name)
        self.assertIn("测试平台项目1",name)


    def test_create_project(self):
        """创建项目"""
        self.driver.find_element_by_id("CreateButton").click()
        sleep(2)
        name_input = self.driver.find_element_by_name("name")
        name_input.send_keys("测试平台项目2")
        self.driver.find_element_by_name("describe").send_keys("此处为测试平台项目2的具体描述内容")
        sleep(2)
        self.driver.find_element_by_id("create").click()
        sleep(2)
        name = self.driver.find_element_by_id("list").text
        self.assertIn("测试平台项目2", name)


    def test_update_project(self):
        """修改项目"""
        self.driver.find_element_by_id("update").click()
        sleep(2)
        name = self.driver.find_element_by_name("name")
        name.clear()
        name.send_keys("测试平台项目2")
        self.driver.find_element_by_id("save").click()
        sleep(2)
        name2 = self.driver.find_element_by_id("list").text
        self.assertIn("测试平台项目2", name2)

    def test_delete_project(self):
        """删除项目"""
        self.driver.find_element_by_id("delete").click()
        sleep(2)
        name = self.driver.find_element_by_id("list").text
        # print(name)
        self.assertNotIn("测试平台项目1", name)
