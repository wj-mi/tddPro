# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_retrieve_it_later(self):
        # bob 听说有一个在线待办事项应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000/tips/index')

        # 他注意到网页的标题和头部包含'待办事项'这个词
        self.assertIn(u'待办事项', self.browser.title)
        self.fail("Finish the test!")

        # 他应邀输入一个待办事项

        # 他在一个文本框中输入了"购买<Python核心编程>" 并点击提交按钮
        # 页面中显示了"1.购买<Python核心编程>"

        # Bob在输入框中输入了'购买<测试驱动开发>'并点击提交按钮
        # 页面中显示了两个待办事项


if __name__ == "__main__":
    unittest.main()
