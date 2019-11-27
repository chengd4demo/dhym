$(function(){
	
	var outerHeight = $('#heigths').outerHeight();//获取顶部固定高度
	var windowHeight = $(window).height();   //获取浏览器窗口高度 
	var documentHeight = $(document).height(); //获取文档高度
	var outerWidth = $('#widths').outerWidth(); //获取左边固定宽度
	var windowWidth = $(window).width();   //获取浏览器窗口宽度 
	var documentWidth = $(document).width(); //获取文档宽度
	//设置iframe高度,宽度

	$('#iframes').css({
		'height':documentHeight-outerHeight,
		'width':documentWidth-outerWidth-15,
	})
	//默认选中加载页面
	$('.sidebar-submenu a').eq(0).css('color','#fff')
	//鼠标点击触发事件
	$('.sidebar-submenu a').click(function(){
		var attrs = $(this).attr("name");
		//更换src属性值
		$('#iframes').attr('src','/adminmanage/'+attrs)
		//设置当前a标签选中颜色
		$(this).css('color','#fff').parent('li').siblings().children('a').css('color','')
	})
	
})
