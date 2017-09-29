# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.


class IndexView(View):

    def get(self, request):
        print 'in index'
        return render(request, 'index.html')

    def post(self, request):
        data = request.POST.get('things', '')
        return render(request, 'index.html')


def index(request):
    if request.method == 'POST':
        return render(request, 'index.html',
                      {'new_item_text': request.POST['things']})
    print 'in index'
    return render(request, 'index.html')