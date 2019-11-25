from django.urls import path

from adminmanage import views

'''
    接口
'''
urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
]
