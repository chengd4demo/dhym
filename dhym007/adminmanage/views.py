import hashlib

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from show.models import dhym_message, dhym_news

'''
登录
'''


def login(request):
    from show.models import dhym_root
    roots = dhym_root.objects.all()
    for root in roots:
        print('root = ', root.root_user)
    return render(request, 'admin/dhym_login.html')


'''
后台主页
'''


def home(request):
    return render(request, 'admin/dhym_index.html')


'''
默认加载页面
'''


def load(request):
    # data = {
    #     'hello':'hello',
    # }
    return render(request, 'admin/dhym_load.html')


'''
点击加载
'''


def dhym_load(request):
    print('进来了.........................')
    return render(request, 'admin/dhym_load.html')


'''
点击新闻添加 dhym_adminews
'''
@csrf_exempt
def dhym_adminews(request):
    print('进入到.............dhym_admimessage')
    if request.method == 'POST':
        print('===', request.POST)
        newname = request.POST.get('newname')
        # 获取页数，如果没有的话就给个默认值 1
        page = int(request.GET.get('page', 1))
        # 获取每页显示 10 条数据，如果没有就给个默认数据 5条
        per_page = int(request.GET.get('per_page', 5))
        # 查询所有新闻数据
        news = dhym_news.objects.filter(Q(news_title__startswith=newname)).order_by('-id')  # 根据id倒叙查询
        # for new in news:
        #     print('news_title = ', new.news_title)
        #     print('news_image = ', new.news_image)
        # 创建分页器对象,将数据集合让入里面，以及每页显示的数据
        paginator = Paginator(news, per_page)
        # 获取我们的具体页码,将页码传入
        page_object = paginator.page(page)
        # 将数据传入前端
        page_range = paginator.page_range  # 遍历页码数
        # 获取总页数
        numbs = paginator.num_pages
        data = {
            'page_object': page_object,
            'page_range': page_range,
            'numbs': numbs,
            'per_page': per_page,
            'newname':newname,
        }
        return render(request, 'admin/dhym_adminews.html', context=data)
    elif request.method == 'GET':
        # 获取页数，如果没有的话就给个默认值 1
        page = int(request.GET.get('page', 1))
        # 获取每页显示 10 条数据，如果没有就给个默认数据 5条
        per_page = int(request.GET.get('per_page', 5))
        # 查询所有新闻数据
        news = dhym_news.objects.all().order_by('-id')  # 根据id倒叙查询
        for new in news:
            print('news_title = ',new.news_title)
            print('news_image = ',new.news_image)
        # 创建分页器对象,将数据集合让入里面，以及每页显示的数据
        paginator = Paginator(news, per_page)
        # 获取我们的具体页码,将页码传入
        page_object = paginator.page(page)
        # 将数据传入前端
        page_range = paginator.page_range  # 遍历页码数
        # 获取总页数
        numbs = paginator.num_pages
        data = {
            'page_object': page_object,
            'page_range': page_range,
            'numbs': numbs,
            'per_page': per_page,
        }
        return render(request, 'admin/dhym_adminews.html', context=data)
    return render(request, 'admin/dhym_adminews.html')
'''
删除新闻
'''
def delnew(request):
    newId = int(request.GET.get('id'))
    print("id++++",id)
    result = dhym_news.objects.get(pk=newId)
    try:
        result.delete()
    except Exception as e:
        return JsonResponse({"status":'fail','msg':'删除失败'})

    return JsonResponse({"status": 'success', 'msg': '删除成功'})

'''
点击 dhym_admimessage
'''


@csrf_exempt
def dhym_admimessage(request):
    print('进入到.............dhym_admimessage')
    if request.method == 'POST':
        print('进入到..post.....................')
        print('===',request.POST)
        username = request.POST.get('mname')
        # messages = dhym_message.objects.all()
        # 获取页数，如果没有的话就给个默认值 1
        page = int(request.GET.get('page', 1))
        # 获取每页显示 10 条数据，如果没有就给个默认数据 5条
        per_page = int(request.GET.get('per_page', 6))
        messages = dhym_message.objects.filter(Q(message_name__startswith=username)|Q(message_phone__contains=username)).order_by('-id')
        # 创建分页器对象,将数据集合让入里面，以及每页显示的数据
        paginator = Paginator(messages, per_page)
        # 获取我们的具体页码,将页码传入
        page_object = paginator.page(page)
        # 将数据传入前端
        page_range = paginator.page_range  # 遍历页码数
        # 获取总页数
        numbs = paginator.num_pages
        data = {
            'page_object': page_object,
            'page_range': page_range,
            'numbs': numbs,
            'per_page': per_page,
            'mname':username,
        }
        return render(request, 'admin/dhym_admimessage.html', context=data)
    elif request.method == 'GET':
        # 获取页数，如果没有的话就给个默认值 1
        page = int(request.GET.get('page', 1))
        # 获取每页显示 10 条数据，如果没有就给个默认数据 5条
        per_page = int(request.GET.get('per_page',6))
        # 查询所有新闻数据
        messages = dhym_message.objects.all().order_by('-id')  # 根据id倒叙查询
        # 创建分页器对象,将数据集合让入里面，以及每页显示的数据
        paginator = Paginator(messages, per_page)
        # 获取我们的具体页码,将页码传入
        page_object = paginator.page(page)
        # 将数据传入前端
        page_range = paginator.page_range  # 遍历页码数
        # 获取总页数
        numbs = paginator.num_pages
        data = {
            'page_object': page_object,
            'page_range': page_range,
            'numbs': numbs,
            'per_page':per_page,
        }
        return render(request, 'admin/dhym_admimessage.html', context=data)
    return render(request, 'admin/dhym_admimessage.html')




'''
点击 新闻发布 dhym_addnews
'''
def dhym_addnews(request):

    return render(request, 'admin/dhym_addnews.html')


'''
login
'''
def password_encrypt(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    result = md5.hexdigest()
    print('密码：',result)
    return result

@csrf_exempt
def auth(request):
    from show.models import dhym_root
    userName = request.POST.get('user')
    try:
        user = dhym_root.objects.get(root_user=userName)
    except Exception as e:
        return render(request, 'admin/dhym_login.html', context={'errormsg': '用户名或密码错误'})
    if user:
        if password_encrypt(request.POST.get('pswd')) != user.root_pwd:
            return render(request, 'admin/dhym_login.html', context={'errormsg':'用户名或密码错误'})
        else:
            data = {
                'currenuser': user.root_user,
            }
            return render(request, 'admin/dhym_index.html', context=data)

'''
退出登录
'''
def loginout(request):
    return redirect(reverse('adminSecond:login'))
'''
删除留言
'''
def delmsg(request):
    msgId = int(request.GET.get('id'))
    print("id++++",id)
    result = dhym_message.objects.get(pk=msgId)
    try:
        result.delete()
    except Exception as e:
        return JsonResponse({"status":'fail','msg':'删除失败'})

    return JsonResponse({"status": 'success', 'msg': '删除成功'})
