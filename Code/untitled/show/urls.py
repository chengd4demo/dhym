from django.urls import path

from show import views

'''
    
'''
urlpatterns = [
    path('index/', views.index, name='index'),
    path('merchants/', views.merchants, name='merchants'),
    path('news/', views.news, name='news'),
    path('newProduct/', views.newProduct, name='newProduct'),
    path('introduction/', views.introduction, name='introduction'),
    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
]