from django.urls import path

from adminmanage import views

'''
    接口
'''
urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('load/', views.load, name='load'),
    path('dhym_load/', views.dhym_load, name='dhym_load'),
    path('dhym_adminews/', views.dhym_adminews, name='dhym_adminews'),
    path('delnew/', views.delnew, name='delnew'),
    path('dhym_admimessage/', views.dhym_admimessage, name='dhym_admimessage'),
    path('dhym_addnews/', views.dhym_addnews, name='dhym_addnews'),
    path('auth/', views.auth, name='auth'),
    path('loginout/',views.loginout, name='loginout'),
    path('delmsg/', views.delmsg, name='delmsg'),

]
