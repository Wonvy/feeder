/*jslint browser: true*/
/*global $, jQuery, alert*/


//键盘操作
$(document).keydown(function (event) {
	'use strict';
	if (event.ctrlKey && event.keyCode === 13) {
		alert('Ctrl+Enter');
	}
	switch (event.keyCode) {
		case 27:
			//            alert('ESC键');
			$("#open").removeClass("on");
			$("#open iframe").attr("src", "");
			break;
		case 37:
			alert('方向键-左');
			break;
		case 39:
			alert('方向键-右');
			break;
	}
	//	return false;
});


$(document).ready(function () {
	'use strict';

	var host = "http://127.0.0.1:8000";
	//	$("#wrapper").load("html/zcool.html");
	// $("nav > div > ul").addClass("on");

	// 防止链接打开 URL：
	//    $("#flex-wrap a").attr("href", "dd");
	$("#flex-wrap").on("click", "a", function (ev) {
		event.preventDefault();
	});

	$("nav h2").click(function () {
		var ul = $(this).next();

		if (ul.hasClass("on")) {
			ul.removeClass("on");
			$("nav ul").removeClass("on");
		} else {
			$("nav ul").removeClass("on");
			ul.addClass("on");
		}
		if ($(this).hasClass("on")) {
			$(this).removeClass("on");
		} else {
			$("nav h2").removeClass("on");
			$(this).addClass("on");
		}
	});

	// $("#wrapper").load("uisdc.html");

	$("nav ul li").click(function () {
		var html, ahref;
		html = $(this).find("a").attr("data-href");
		$("nav ul li").removeClass("on");
		$(this).addClass("on");
		ahref = host + "/list/" + encodeURIComponent(html);
		$.get(ahref, function (result) {
			$("#wrapper").html(result);
			window.history.pushState({}, 0, 'http://' + window.location.host + '/' + html);
		});
		//		var patten = new RegExp("z");
		//		var url = patten.match(html);
		//
		//		alert(url[0]);
		//		alert(url[1]);
		//		console.log(url);
		//        $("#wrapper").load("html/" + html + ".html");

	});

	$("nav ul li").dblclick(function () {

		alert("444");
	});


	// 上一项
	$(".prex").click(function () {
		var on_id, html, ahref;
		on_id = $('nav li.on').index();
		alert(on_id);
		on_id = parseInt(on_id, 10) - 1;
		html = $("nav li:eq(" + on_id + ")").find("a").attr("data-href");


		// 返回数据
		//		ahref = host + "/list/" + encodeURIComponent(html);
		//		$.get(ahref, function (result) {
		//			$("#wrapper").html(result);
		//		});

		//        $("#wrapper").load("html/" + html + ".html");

		$("nav li").removeClass("on");
		$("nav li:eq(" + on_id + ")").addClass("on");
		//		$("#flex-wrap a").click(function (event) {
		//			event.preventDefault();
		//		});
	});



	// 下一项
	$(".next").click(function () {

		//获取ID
		var on_id, html, ahref;
		on_id = $('nav li.on').index();
		on_id = parseInt(on_id, 10) + 1;
		html = $("nav li:eq(" + on_id + ")").find("a").attr("data-href");

		// 返回数据
		//		ahref = host + "/list/" + encodeURIComponent(html);
		//		$.get(ahref, function (result) {
		//			$("#wrapper").html(result);
		//			//            alert(result);
		//		});

		//        $("#wrapper").load("html/" + html + ".html");

		$("nav li").removeClass("on");
		$("nav li:eq(" + on_id + ")").addClass("on");

		//		$("#flex-wrap a").click(function (event) {
		//			event.preventDefault();
		//		});

		// ID+1，如果大于总ID,则为1
	});



	$(".show_text").click(function () {
		if ($(this).text() === "A") {
			$(this).text("-");
			$("#wrapper ul li a").removeClass("on");
		} else {
			$(this).text("A");
			$("#wrapper ul li a").addClass("on");
		}

	});



	// 提交表单
	$('#submit').click(function () {
		var s, sinput;
		sinput = $('#user_url').val();
		sinput = encodeURIComponent(sinput);
		s = $('#province').val();

		$.get(host + "/feed?url=" + sinput + "&fenlei=" + s, function (result) {
			$("#wrapper").html(result);
			//            alert(result);
		});
	});


	// 提交表单
	$('#bottom .bottom').click(function () {
		var s, sinput;
		s = $(this).attr("data-url");
		$.get(host + "/feed?fenlei=" + s, function (result) {
			$("#wrapper").html(result);
			//            alert(result);
		});
	});

	$(".settingall").click(function () {
		$("#setting").addClass("on");
    });

	$(".closeall").click(function () {
		$("#setting").removeClass("on");
    });



	// 弹出框
	$("#flex-content").delegate("ul li", "click", function (ev) {
		var whref, ahref, openid;
		//		openid = $("#flex-preview");
		openid = $("#page");
		openid.html("");
		openid.scrollTop(0);
		whref = $(this).children("a").attr("href");
		ahref = host + "/content/" + encodeURIComponent(whref); // 已经阅读过
		$.get(ahref, function (result) {
			openid.html(result);
		});
		$(this).addClass("reed");
		$("#open").addClass("on");
		//        $("#open iframe").attr("src", whref);
		//        $("#open").load("zcool.html");

	});


	// 弹出框
	$("#flex-content ul li a").hover(function () {
		//        var whref, ahref;
		//        whref = $(this).html();
		//        alert(ahref);
	});


	// 弹出框 - 字号
	$(".zoomin").click(function () {
		var size = parseInt($(".pagestyle p").css("font-size"), 10);
		size += 2;
		$(".pagestyle p").css("font-size", size + 'px');
	});
	$(".w1280").click(function () {
		$("#open .pagestyle").css("width","1280px");
	});

	$(".w800").click(function () {
		$("#open .pagestyle").css("width","800px");
	});

	$(".zoomout").click(function () {
		var size = parseInt($(".pagestyle p").css("font-size"), 10);
		size -= 2;
		$(".pagestyle p").css("font-size", size + 'px');
	});

	$("#open .areaclose").click(function () {
		$("#open").removeClass("on");
	});
	$(".close").click(function () {
		$("#open").removeClass("on");
	});

	//更换主题
	$('#flex-content .page-controls i').click(function (event) {
		var Theme = $(this).attr("data-theme");
		$('#theme').attr('href', host + Theme);

		$(".page-controls i").removeClass("on");
		$(this).addClass("on");
	});
	//		$(".link > li > li:it(3)")

});
