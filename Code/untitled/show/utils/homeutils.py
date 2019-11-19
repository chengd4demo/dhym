from show.models import dhym_Baner, dhym_video, dhym_Pureimage, dhym_ProductAdvantage, dhym_service, dhym_partners

'''
首页baner
'''
def get_baners(baners):
    baner_list = []
    for banerfor in baners:
        baner = dhym_Baner()
        baner.id = banerfor.id
        baner.baner_describe = banerfor.baner_describe
        baner.baner_image = '/static/'+str(banerfor.baner_image)
        baner_list.append(baner)
    return baner_list

'''
video
'''
def get_video(video_in):
    print('进入video............................')
    video_out = dhym_video()
    video_out.video_fifle = '/static/'+str(video_in.video_fifle)
    video_out.video_ch = video_in.video_ch
    video_out.video_us = video_in.video_us
    print('出去video............................')
    return video_out

'''
视频右边的4张图片
'''
def get_pureimage(pureimages):
    pureimage = dhym_Pureimage()
    pureimage.pureimage_one = '/static/'+str(pureimages.pureimage_one)
    pureimage.pureimage_two = '/static/'+str(pureimages.pureimage_two)
    pureimage.pureimage_three = '/static/'+str(pureimages.pureimage_three)
    pureimage.pureimage_four = '/static/'+str(pureimages.pureimage_four)

    return pureimage

'''
优势
'''
def get_productadvantage(productadvantages):
    print('优势 in---------------------------------------')
    productadvantage_list = []
    for productadvantage in productadvantages:
        productadvantagefor = dhym_ProductAdvantage()
        productadvantagefor.id = productadvantage.id
        productadvantagefor.productAdvantage_img = '/static/'+str(productadvantage.productAdvantage_img)
        productadvantagefor.productAdvantage_zh = productadvantage.productAdvantage_zh
        productadvantagefor.productAdvantage_us = productadvantage.productAdvantage_us
        productadvantagefor.productAdvantage_descride = productadvantage.productAdvantage_descride
        productadvantage_list.append(productadvantagefor)
    print('优势 out---------------------------------------')
    return productadvantage_list

'''
我们的服务
'''
def get_service(services):
    print('服务 in ...........................................')
    services_list = []
    for servicefor in services:
        service = dhym_service()
        service.id = servicefor.id
        service.service_img = '/static/'+str(servicefor.service_img)
        service.service_type = servicefor.service_type
        service.service_descride = servicefor.service_descride
        services_list.append(service)
    print('服务 out ...........................................')
    return services_list

'''
合作伙伴
'''
def get_partners(partners):
    print('合作伙伴 in ......................................')
    partners_list = []
    for partnerfor in partners:
        partner = dhym_partners()
        partner.id = partnerfor.id
        partner.partners_img = '/static/'+str(partnerfor.partners_img)
        partners_list.append(partner)
    print('合作伙伴 out ......................................')
    return partners_list