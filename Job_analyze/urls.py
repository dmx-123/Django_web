"""Job_analyze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from mainsite import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^accounts/login/$', views.my_login, name='login'),
    path(r'^accounts/logout/$', views.logout, name='logout'),
    path(r'^accounts/signup/$', views.signup, name='signup'),
    path(r'^accounts/set_password/$', views.set_password, name='set_password'),
    path(r'^accounts/info/$', views.myInfo, name='info'),
    path(r'^$', views.homepage, name='homepage'),  # 此行一定放在job_list行之上，否则出错
    path(r'^job/search/$', views.homepage_search, name='homepage_search'),
    path(r'^job_detail/(.+?)/search/$', views.job_detail_search, name='job_detail_search'),
    path(r'^job/(.+?)$', views.showjobs, name='job_list'),
    path(r'^job_detail/(.+?)$', views.show_job_detail, name='job_detail'),
]
