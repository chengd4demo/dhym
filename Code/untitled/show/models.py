from django.db import models

# Create your models here.
'''
baner:
图片
标题

标题：
小标题
大标题
英文标题
标题下描述

宣传视频：
      视频路劲
      中文标题
      英文标题

产品优势：
	图片
	中文标题
	英文标题
	产品优势描述
	标题外键------

服务：
	图片
	类型
	类型的描述
	标题外键------

合作伙伴：
	图片
	标题外键------
新闻类型：
	公司新闻动态
	行业相关新闻
新闻：
	展示图片
	新闻标题
	阅读次数
	发布时间
	简述文字
	第一段文字描述
	第一段文字配图
	第二段文字描述
	第二段文字配图
	第三段文字描述
	第三段文字配图
	第四段文字描述
	第四段文字配图
	第五段文字描述
	第五段文字配图
	第六段文字描述
	
支持：
	图片
	培训标题
	描述
	标题外键------

加盟流程：
	图片
	标题
	描述
	标题外键------

合作要求：
	图片
	标题
	描述
	标题外键------
专利：
	专利名称
	专利个数
公司简介：
	图片
	大标题描述
	小标题描述
	专利外键------
	
发展历史：
	标题
	描述
	时间
	标题外键------

选择我们：
	图片
	中文标题
	英文标题
	描述
	标题外键------

选择下面数据：
	图片
	标题
	数字
	描述

我们团队：
	图片
	英文名字
	职位
	标题外键------

专利证书：
	图片
	标题外键------	

留言：
	姓名
	电话
	邮箱
	内容
	
区域经理：
	区域姓氏
	地址
	电话
	邮箱

'''

'''
baner:轮播
图片
标题
'''
class dhym_Baner(models.Model):
      baner_image = models.ImageField(upload_to='images/main-slider',max_length=255, null=True,blank=True) #图片路劲
      baner_describe = models.CharField(max_length=64,null=True,blank=True)#baner图片的描述
      #数据库的名称
      class Meta:
            db_table = 'dhym_baner'

'''
标题：
小标题
大标题
英文标题
标题下描述
'''
class dhym_title(models.Model):
      title_small_title = models.CharField(max_length=12,null=True,blank=True)#标题中的小标题
      title_big_title = models.CharField(max_length=24,null=True,blank=True)#标题中的大标题
      title_us_title = models.CharField(max_length=48, null=True, blank=True)  # 标题中的英文标题
      title_describe = models.CharField(max_length=255, null=True, blank=True)  # 标题中的描述

      class Meta:
            db_table = 'dhym_title'

'''
宣传视频：
      视频路劲
      中文标题
      英文标题
'''
class dhym_video(models.Model):
      video_fifle = models.FileField(upload_to='video',null=True,blank=True)#视频
      video_ch = models.CharField(max_length=48,null=True,blank=True)#视频中文标题
      video_us = models.CharField(max_length=96,null=True,blank=True)#视频英文标题

      class Meta:
            db_table = 'dhym_video'
'''
宣传视频旁边的图片显示
'''
class dhym_Pureimage(models.Model):
      pureimage_one = models.ImageField(upload_to='images/resource',max_length=128,null=True,blank=True)#第一张图片
      pureimage_two = models.ImageField(upload_to='images/resource',max_length=128,null=True,blank=True)#第二张图片
      pureimage_three = models.ImageField(upload_to='images/resource',max_length=128,null=True,blank=True)#第三张图片
      pureimage_four = models.ImageField(upload_to='images/resource',max_length=128,null=True,blank=True)#第四张图片

      class Meta:
            db_table = 'dhym_Pureimage'

'''
产品优势：
	图片
	中文标题
	英文标题
	产品优势描述
	标题外键------
'''
class dhym_ProductAdvantage(models.Model):
      productAdvantage_img = models.ImageField(upload_to='images/icons',max_length=128,null=True,blank=True)#图片
      productAdvantage_zh = models.CharField(max_length=48,null=True,blank=True)#中文标题
      productAdvantage_us = models.CharField(max_length=48,null=True,blank=True)#英文标题
      productAdvantage_descride = models.CharField(max_length=255,null=True,blank=True)#产品描述
      productAdvantage_dhym_title = models.ForeignKey('dhym_title',null=True,on_delete=models.SET_NULL)#标题外键

      class Meta:
            db_table = 'dhym_ProductAdvantage'

'''
服务：
	图片
	类型
	类型的描述
	标题外键------
'''
class dhym_service(models.Model):
      service_img = models.ImageField(upload_to='images/resource',max_length=128,null=True,blank=True)#图片
      service_type = models.CharField(max_length=48,null=True,blank=True)#服务类型
      service_descride = models.CharField(max_length=128,null=True,blank=True)#服务的描述
      service_dhym_title = models.ForeignKey('dhym_title',null=True,on_delete=models.SET_NULL)#标题外键

      class Meta:
            db_table = 'dhym_service'

'''
合作伙伴：
	图片
	标题外键------
'''
class dhym_partners(models.Model):
      partners_img = models.ImageField(upload_to='images/clients',max_length=128,null=True,blank=True)#图片
      partners_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)  # 标题外键

      class Meta:
            db_table = 'dhym_partners'
'''
新闻：
	展示图片
	新闻标题
	阅读次数
	发布时间
	简述文字
	第一段文字描述
	第一段文字配图
	第二段文字描述
	第二段文字配图
	第三段文字描述
	第三段文字配图
	第四段文字描述
	第四段文字配图
	第五段文字描述
	第五段文字配图
	第六段文字描述
'''
class dhym_news(models.Model):
      news_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)#图片
      news_title = models.CharField(max_length=48,null=True,blank=True)#新闻标题
      news_count = models.IntegerField(max_length=11,null=True,blank=True)#阅读次数
      news_time = models.DateTimeField(auto_now_add=True)#发布时间
      news_describe = models.CharField(max_length=128,null=True,blank=True)#新闻简述文字
      news_one_describe = models.CharField(max_length=255,null=True,blank=True)#新闻第一段文字描述
      news_one_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)#新闻第一段文字描述配图
      news_two_describe = models.CharField(max_length=255, null=True, blank=True)  # 新闻第二段文字描述
      news_two_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)  # 新闻第二段文字描述配图
      news_three_describe = models.CharField(max_length=255, null=True, blank=True)  # 新闻第三段文字描述
      news_three_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)  # 新闻第三段文字描述配图
      news_four_describe = models.CharField(max_length=255, null=True, blank=True)  # 新闻第四段文字描述
      news_four_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)  # 新闻第四段文字描述配图
      news_five_describe = models.CharField(max_length=255, null=True, blank=True)  # 新闻第五段文字描述
      news_five_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)  # 新闻第五段文字描述配图
      news_sex_describe = models.CharField(max_length=255, null=True, blank=True)  # 新闻第六段文字描述

      class Meta:
            db_table = 'dhym_news'

'''
支持：
	培训标题
	描述
	标题外键------
'''
class dhym_support(models.Model):
      support_title = models.CharField(max_length=48,null=True,blank=True)#支持标题
      support_describe = models.CharField(max_length=128,null=True,blank=True)#支持描述
      support_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)#标题外键

      class Meta:
            db_table = 'dhym_support'


'''
加盟流程：
	图片
	标题
	描述
	标题外键------
'''
class dhym_process(models.Model):
      process_img = models.ImageField(upload_to='images/icons',max_length=128, null=True, blank=True)  # 流程图片
      process_title = models.CharField(max_length=48, null=True, blank=True)  # 流程标题
      process_describe = models.CharField(max_length=128, null=True, blank=True)  # 流程描述
      process_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)  # 标题外键

      class Meta:
            db_table = 'dhym_process'

'''
合作要求：
	标题
	描述
	标题外键------
'''
class dhym_requirements(models.Model):
      requirements_title = models.CharField(max_length=48, null=True, blank=True)  # 要求标题
      requirements_describe = models.CharField(max_length=128, null=True, blank=True)  # 要求描述
      requirements_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)  # 标题外键

      class Meta:
            db_table = 'dhym_requirements'

'''
公司简介专利
专利：
	专利名称
	专利个数
'''
class dhym_introductionPatent(models.Model):
      introductionPatent_name = models.CharField(max_length=48, null=True, blank=True)#专利名称
      introductionPatent_count = models.IntegerField(max_length=4,null=True,blank=True)#专利个数

      class Meta:
            db_table = 'dhym_introductionPatent'

'''
公司简介：
	图片
	大标题描述
	小标题描述
	专利外键------
'''
class dhym_Companyprofile(models.Model):
      Companyprofile_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)  # 公司简介图片
      Companyprofile_describe_big = models.CharField(max_length=128, null=True, blank=True) #大标题描述
      Companyprofile_describe_small = models.CharField(max_length=128, null=True, blank=True) #小标题描述
      Companyprofile_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)  # 标题外键

      class Meta:
            db_table = 'dhym_Companyprofile'

'''
发展历史：
	标题
	描述
	时间
	标题外键------
'''
class dhym_history(models.Model):
      history_title = models.CharField(max_length=128, null=True, blank=True) #历史标题
      history_describe = models.CharField(max_length=128, null=True, blank=True) #历史标题描述
      history_time = models.DateField(auto_now=True)#时间
      history_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)  # 标题外键

      class Meta:
            db_table = 'dhym_history'


'''
选择我们：
	中文标题
	英文标题
	描述
	标题外键------
'''
class dhym_Chooseus(models.Model):
      Chooseus_zh = models.CharField(max_length=48, null=True, blank=True)  # 中文标题
      Chooseus_us = models.CharField(max_length=48, null=True, blank=True)  # 英文标题
      Chooseus_describe = models.CharField(max_length=255, null=True, blank=True)  # 描述
      Chooseus_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)  # 标题外键

      class Meta:
            db_table = 'dhym_Chooseus'
'''
选择下面数据：
	图片
	标题
	数字
	描述
'''
class dhym_data(models.Model):
      data_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)     #选择下面数据图片
      data_title = models.CharField(max_length=32, null=True, blank=True)       #选择下面数据标题
      data_number =models.IntegerField(max_length=7,null=True,blank=True)         #选择下面数据数字
      data_describe = models.CharField(max_length=128, null=True, blank=True)   # 选择下面数据描述

      class Meta:
            db_table = 'dhym_data'
'''
我们团队：
	图片
	英文名字
	职位
	标题外键------
'''
class dhym_team(models.Model):
      team_img = models.ImageField(upload_to='images/resource',max_length=128, null=True, blank=True)  # 团队图片
      team_us = models.CharField(max_length=32, null=True, blank=True)  #团队英文名字
      team_position = models.CharField(max_length=32, null=True, blank=True)  #团队职位
      team_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)  # 标题外键

      class Meta:
            db_table = 'dhym_team'


'''
专利证书：
	图片
	标题外键------
'''
class dhym_certificate(models.Model):
      certificate_img = models.ImageField(upload_to='images/clients',max_length=128, null=True, blank=True)  # 专利图片
      certificate_dhym_title = models.ForeignKey('dhym_title', null=True, on_delete=models.SET_NULL)  # 标题外键

      class Meta:
            db_table = 'dhym_certificate'
'''
留言：
	姓名
	电话
	邮箱
	内容
'''
class dhym_message(models.Model):
      message_name = models.CharField(max_length=32,null=True,blank=True)#姓名
      message_phone = models.CharField(max_length=32,null=True,blank=True)#电话
      message_email = models.CharField(max_length=32,null=True,blank=True)#邮箱
      message_content = models.CharField(max_length=255,null=True,blank=True)#内容

      class Meta:
            db_table = 'dhym_message'

'''
区域经理：
	区域姓氏
	地址
	电话
	邮箱
'''
class dhym_manager(models.Model):
      manager_name = models.CharField(max_length=32,null=True,blank=True)#姓氏
      manager_address = models.CharField(max_length=32,null=True,blank=True)#地址
      manager_phone = models.CharField(max_length=32,null=True,blank=True)#电话
      manager_email = models.CharField(max_length=32,null=True,blank=True)#邮箱

      class Meta:
            db_table = 'dhym_manager'
