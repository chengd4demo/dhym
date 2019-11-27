$(function () {
    // 正则匹配cookie中的csrftoken，传入cookie名字
    // function getCookie(name) {
    //     var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    //     return r ? r[1] : undefined;
    // }
    // $('#sfg').click(function () {
    //     //跳转
    //     location.href='/show/news/'
    // })
    //ajax提交form表单的方式
    $('#contact-form').submit(function () {
            if ($.trim($("input[name=username]").val()).length == 0) {
                alert('亲，您还没输入名字哟！')
                return false
            }
            var res = /^[\u4e00-\u9fa5]+$/;

            if (!res.test($.trim($("input[name=username]").val()))) {
                alert('亲，请输入您正确的名字，方便我们联系您')
                return false
            }
            if ($.trim($("input[name=username]").val()).length <= 1 || $.trim($("input[name=username]").val()).length >= 5) {
                alert('亲，请输入正确的名字(2-5)个汉字，谢谢哟')
                return false
            }
            if ($.trim($("input[name=phoneNumber]").val()).length == 0) {
                alert('亲，您还没有输入手机号哟！')
                return false
            } else {
                if (isPhoneNo($.trim($("input[name=phoneNumber]").val())) == false) {
                    alert('亲，您的手机号输入错误哟！')
                    return false
                }
            }
            if($.trim($("textarea[name=textMessage]").val()).length <= 0){
				alert('亲，您的留言内容还没填写哦！')
            	return false
			}
            if($.trim($("textarea[name=textMessage]").val()).length >= 100){
				alert('亲，您可以把话精简一下，我们只有100个汉字的位置哟！')
            	return false
			}
             //AjaxURL = $('#liuyan').attr('action')
            //alert('AjaxURL = '+AjaxURL)
            alert($('#contact-form').serialize());
            $.ajax({
                url: '/show/savemessage/',
                type: "POST",
                dataType: "json",
                data:$('#contact-form').serialize(),
                async : false,
                success: function (data) {
                    $.each(data, function (name, value) {
                        alert(value)
                    });
                },
                error: function (data) {
                    alert("error:" + data.responseText);
                }
            });
        }
    );
    // 验证手机号
    function isPhoneNo(phone) {
        var pattern = /^1[34578]\d{9}$/;
        return pattern.test(phone);
    }

})