# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from tips.views import ListsView
from tips.models import Item
# Create your tests here.


# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)


class ListsViewTest(TestCase):

    def test_lists_page_only_save_item_when_necessary(self):
        self.client.get('/tips/lists/')
        self.assertEqual(Item.objects.count(), 0)

    def test_lists_can_save_a_post_request(self):
        self.client.post('/tips/lists/', {'list': 'a new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'a new list item')

    def test_lists_redirect_after_post(self):
        response = self.client.post('/tips/lists/',
                                    data={'list': 'a new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/tips/lists/')

    def test_lists_display_all_list_items(self):
        Item.objects.create(text="item1")
        Item.objects.create(text="item2")

        response = self.client.get('/tips/lists/')

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

