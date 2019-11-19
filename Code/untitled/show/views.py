from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from show.models import dhym_Baner, dhym_title, dhym_video, dhym_Pureimage, dhym_ProductAdvantage, dhym_service, \
    dhym_partners, dhym_support, dhym_process
from show.utils.Merchantsutils import get_process
from show.utils.homeutils import get_baners, get_video, get_pureimage, get_productadvantage, get_service, get_partners

'''
首页显示
'''
def index(request):
    #baner
    baners = dhym_Baner.objects.all()
    baners = get_baners(baners)
    #最终目标
    onetitles = dhym_title.objects.filter(id=1)[0]
    #宣传视频
    video = get_video(dhym_video.objects.filter(id=1)[0])
    #宣传视频右边的4张图片
    pureimage = get_pureimage(dhym_Pureimage.objects.filter(id=1)[0])
    #产品优势标题
    twotitles = dhym_title.objects.filter(id=2)[0]
    #产品优势
    productadvantages = get_productadvantage(dhym_ProductAdvantage.objects.all())
    #服务标题
    servicestitles = dhym_title.objects.filter(id=3)[0]
    #我们的服务
    services = get_service(dhym_service.objects.all())
    #合作伙伴标题
    partnerstitles = dhym_title.objects.filter(id=4)[0]
    #合作伙伴
    partners = get_partners(dhym_partners.objects.all())
    data = {
        'title':'首页',
        'baners':baners,
        'onetitles':onetitles,
        'video':video,
        'pureimage':pureimage,
        'twotitles':twotitles,
        'productadvantages':productadvantages,
        'servicestitles':servicestitles,
        'services':services,
        'partnerstitles':partnerstitles,
        'partners':partners,
    }
    return render(request,'dhym_show/home.html',context=data)

'''
招商加盟界面
'''
def merchants(request):
    # 支持标题
    supporttitles = dhym_title.objects.filter(id=5)[0]
    #支持
    supports = dhym_support.objects.all()
    #流程标题
    processtitles = dhym_title.objects.filter(id=6)[0]
    process_list = get_process(dhym_process.objects.all())
    data = {
        'title':'招商加盟',
        'supporttitles':supporttitles,
        'supports':supports,
        'processtitles':processtitles,
        'process_list':process_list,
    }
    return render(request,'dhym_show/ChinaMerchants.html',context=data)

'''
新闻，分页，每页5条内容
'''
def news(request):
    data = {
        'content':'content'
    }
    return render(request,'dhym_show/news.html',context=data)
'''
新闻详情，Id 查询当前新闻
'''
def newProduct(request):
    data = {

    }
    return render(request, 'dhym_show/newscontent.html', context=data)
'''
公司简介
'''
def introduction(request):
    data = {

    }
    return render(request,'dhym_show/Introduction.html',context=data)
'''
联系我们
'''
def contact(request):
    data = {

    }
    return render(request,'dhym_show/contact.html',context=data)
'''
留言板块，保存留言信息
'''
def message(request):

    return JsonResponse(data={'a':'b'})

