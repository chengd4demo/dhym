from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaulttags import csrf_token
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from show.models import dhym_message, dhym_news

'''
查询全部新闻
'''
# @csrf_exempt
def news(request):
    # 获取页数，如果没有的话就给个默认值 1
    page = int(request.GET.get('page', 1))
    # 获取每页显示 10 条数据，如果没有就给个默认数据 5条
    per_page = int(request.GET.get('per_page', 2))
    #查询所有新闻数据
    news = dhym_news.objects.all().order_by('-id')#根据id倒叙查询
    news_list = dhym_news.objects.all()[0:10]
    for new in news:
        print('new_image = ',new.news_image)
        #print('content = ',new.news_content)
    # 创建分页器对象,将数据集合让入里面，以及每页显示的数据
    paginator = Paginator(news,per_page)
    # 获取我们的具体页码,将页码传入
    page_object = paginator.page(page)
    # 将数据传入前端
    page_range = paginator.page_range  # 遍历页码数
    #获取总页数
    numbs = paginator.num_pages
    data = {
        'page_object': page_object,
        'page_range': page_range,
        'numbs': numbs,
        'news_list':news_list,
    }
    #return HttpResponse('success!')
    return render(request,'getshow/new.html',context=data)

'''
根据id查询新闻
'''
def newsById(request):

    if request.method == 'GET':
        id = int(request.GET.get('id'))
        new = dhym_news.objects.filter(pk=id)[0]
        news_list = dhym_news.objects.all()[0:10]
        data = {
                'title':'新闻详情',
                'new':new,
                'news_list':news_list,
        }
        return render(request,'getshow/newsdata.html',context=data)
    return redirect(reverse('showSecond:news'))

'''
保存留言
'''
@csrf_exempt
def savemessage(request):
    if request.is_ajax():
        print(request.POST)
        username = request.POST.get('username')
        phoneNumber = request.POST.get('phoneNumber')
        textMessage = request.POST.get('textMessage')
        print('username = ',username)
        message = dhym_message()
        message.message_name = username
        message.message_phone = phoneNumber
        message.message_content = textMessage
        message.save()#保存数据
        return JsonResponse(data={'success': '谢谢您的留言,我们会尽快联系您！'})
    return JsonResponse(data={'success': '不好意思，不能接受！'})

'''
首页
'''
def index(request):
    return HttpResponse("<script>location.href='http://127.0.0.1/static/html/index.html'</script>")

