from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

'''
留言
'''
class dhym_message(models.Model):
      message_name = models.CharField(max_length=16,null=False,blank=False)#留言姓名，不能为空
      message_phone = models.CharField(max_length=32,null=False,blank=False)#手机号码，不能为空
      message_content = models.TextField(max_length=255,null=False,blank=False)#留言内容，不能为空
      message_time = models.DateTimeField(default=timezone.now,verbose_name='留言时间')#系统自动记录留言时间
      #映射到数据库名称
      class Meta:
            db_table = 'dhym_message'
'''
新闻
'''
class dhym_news(models.Model):
      news_image = models.ImageField(upload_to='news',max_length=128,null=True,blank=True)#新闻标题图片
      news_title = models.CharField(max_length=64,null=False,blank=False)#新闻标题
      news_user = models.CharField(max_length=32,null=False,blank=False)#发布人
      news_date = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')#新闻发布时间
      news_count = models.BigIntegerField(null=False,blank=False)#新闻阅读次数
      news_paper = models.CharField(max_length=255,null=False,blank=False)#新闻标题简述
      news_content = HTMLField()#详情内容
      # 映射到数据库名称
      class Meta:
            db_table = 'dhym_news'

'''
admin
'''
class dhym_root(models.Model):
      root_user = models.CharField(max_length=32,null=False,blank=False)#账号
      root_pwd = models.CharField(max_length = 32,null=False,blank=False)#密码

      # 映射到数据库名称
      class Meta:
            db_table = 'dhym_root'