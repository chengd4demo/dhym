from django.shortcuts import render

# Create your views here.
'''
登录
'''

def login(request):
    return render(request,'admin/dhym_login.html')


def home(request):
    return render(request,'admin/dhym_index.html')