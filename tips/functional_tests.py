# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        sleep(1)
        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_retrieve_it_later(self):
        # bob 听说有一个在线待办事项应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000/tips/index/')

        # 他注意到网页的标题和头部包含'待办事项'这个词
        self.assertIn(u'待办事项', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(u'待办事项', header_text)

        # 他应邀输入一个待办事项
        inputbox = self.browser.find_element_by_id('new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         u'请输入待办事项')
        # 他在一个文本框中输入了"购买《Python核心编程》" 并点击提交按钮
        # 页面中显示了"1.购买《Python核心编程》"
        inputbox.send_keys(u'购买《Python核心编程》')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table(u'1:购买《Python核心编程》')

        # Bob在输入框中输入了'购买<测试驱动开发>'并点击提交按钮
        # 页面中显示了两个待办事项
        inputbox = self.browser.find_element_by_id('new_item')
        inputbox.send_keys(u'购买《测试驱动开发》')
        inputbox.send_keys(Keys.ENTER)
        #
        self.check_for_row_in_list_table(u'1:购买《Python核心编程》')
        self.check_for_row_in_list_table(u'2:购买《测试驱动开发》')
        self.fail('Finish the test!')


if __name__ == "__main__":
    unittest.main()
