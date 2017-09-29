# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

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
        # print "response : ", response.content
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>待办事项</title>', response.content)
        self.assertTrue(response.content.endswith(b"</html>"))

