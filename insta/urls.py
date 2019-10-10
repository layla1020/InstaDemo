"""InstaDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from insta.views import HellowWord

urlpatterns = [
    path('', HellowWord.as_view(), name='HellowWord'), #当你传进来一个empty string（什么都不输入的时候）的时候，访问到HelloWord的view，调用as_view这个函数
    #由于这个view继承了TemplateView，所以TemplateView的as_view会继承下来
]