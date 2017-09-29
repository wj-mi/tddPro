# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from tips.views import index
# Create your tests here.


# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)


class IndexViewTest(TestCase):
    def test_url_resolves_to_index_view(self):
        found = resolve('/tips/index/')
        self.assertEqual(found.func, index)

    def test_index_return_correct_html(self):
        request = HttpRequest()
        response = index(request)
        # 将responde.content 转化为Unicode 方便对比字符串而不是字节
        expected_html = render_to_string('index.html')
        self.assertTrue(response.content.decode('utf8'), expected_html)

        # self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        # self.assertIn(b'<title>待办事项</title>', response.content)
        # self.assertTrue(response.content.endswith(b"</html>"))

    def test_index_view_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['things'] = 'a new list item'

        response = index(request)
        self.assertIn('a new list item', response.content.decode('utf-8'))
        expected_html = render_to_string(
            'index.html', {'new_item_text': 'a new list item'}
        )
        # self.assertEqual(response.content.decode('utf-8'), expected_html)

