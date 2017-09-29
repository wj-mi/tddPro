# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from tips.views import index
from tips.models import Item
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

    # def test_index_view_post_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['things'] = 'a new list item'
    #
    #     response = index(request)
    #     self.assertEqual(Item.objects.count(), 1)
    #     new_item = Item.objects.first()
    #     self.assertEqual(new_item.text, 'a new list item')
    #
    #     self.assertIn('a new list item', response.content.decode('utf-8'))
    #     expected_html = render_to_string(
    #         'index.html', {'new_item_text': 'a new list item'}
    #     )
        # self.assertEqual(response.content.decode('utf-8'), expected_html)

    def test_index_page_only_save_item_when_necessary(self):
        request = HttpRequest()
        index(request)
        self.assertEqual(Item.objects.count(), 0)

    def test_index_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['things'] = 'a new list item'

        response = index(request)
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'a new list item')

    def test_index_redirect_after_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['things'] = 'a new list item'

        response = index(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/tips/index/')

    def test_index_display_all_list_items(self):
        Item.objects.create(text="item1")
        Item.objects.create(text="item2")

        request = HttpRequest()
        response = index(request)

        self.assertIn('item1', response.content.decode('utf-8'))
        self.assertIn('item2', response.content.decode('utf-8'))



class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second item'
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(), 2)

        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]
        self.assertEqual(first_saved_item.text, 'The first list item')
        self.assertEqual(second_saved_item.text, 'The second item')

