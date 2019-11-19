from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
'''
__init__：没有参数，在服务器响应的第一个请求的时候自动调用，用户确定时候启动该中间件

process_request(self, request): 在执行视图前被调用，每个请求上都会被调用，不主动进行返回或返回HttpResponse对象

process_view(self, request, view_func,view_args, view_kwargs):调用视图之前执行，每个请求都会调用，不主动进行返回或返回HttpResponse对象

process_template_response(self, request, response)：在视图刚好执行完后进行调用，每个请求都会调用，不主动进行返回或返回HttpResponse对象

process_response(self, request, response):所有响应返回浏览器之前调用，每个请求都会调用，不主动进行返回或返回HttpResponse对象

process_exception(self, request, exception):当视图抛出异常时调用，不主动进行返回或返回HttpResponse对象

'''
class webMiddle(MiddlewareMixin):
    # 执行视图前被调用的函数，这个方法还可以设置权限
    def process_request(self,request):
        #print('META = ',request.META)
        print('当前访问服务器的ip为：', request.META.get('REMOTE_ADDR'))
        print('访问端口：',request.META.get('SERVER_PORT'))
    #路劲出错之后重定向到首页
    def process_exception(self,request,exception):
        return redirect(reverse('webSecond:index'))