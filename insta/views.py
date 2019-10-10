from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
# 当有人发送request的时候，我把这个页面作为一个返回值显示出来
# HelloWord is-a TemplateView

class HellowWord(TemplateView):
    template_name = 'test.html'
