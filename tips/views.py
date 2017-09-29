# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from models import Item
# Create your views here.


class IndexView(View):

    def get(self, request):
        items = Item.objects.all()
        return render(request, 'index.html', {'items': items})

    def post(self, request):
        item = Item.objects.create(text=request.POST['things'])
        return redirect('/tips/index/')


def index(request):
    if request.method == 'POST':
        # new_item_text = request.POST.get('things', '')
        item = Item.objects.create(text=request.POST['things'])
        return redirect('/tips/index/')
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})