from django.urls import path

from show import views

'''
    接口
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('newsById/', views.newsById, name='newsById'),
    path('savemessage/', views.savemessage, name='savemessage'),

]
