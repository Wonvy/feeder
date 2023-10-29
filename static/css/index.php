<!DOCTYPE html>

<html>

<head>
	<meta charset="utf-8">
	<title></title>
	<meta name=“renderer” content=“webkit”>
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="Keywords" content="" />
	<meta name="Description" content="。。" />
	<link rel="shortcut icon" href="/favicon.ico" />
	<link rel="bookmark" href="/favicon.ico" />
	<script>
		window.onload = function () {
			if (top != self) {
				var f = document.createElement("form");
				f.action = location;
				f.target = "_parent";
				document.body.appendChild(f);
				f.submit();
			}
		};
	</script>

</head>

<body>
<img src="http://c.hiphotos.baidu.com/image/w%3D210/sign=ed30880babec8a13141a50e1c7029157/d52a2834349b033be1a9503e17ce36d3d539bd35.jpg" >
<img src="http://zcimg.zcool.com.cn/zcimg/c_m_989e552f83420000012a7c2b9b1e.jpg">
	



<?php 
		//初始化一个 cURL 对象
		$curl = curl_init("http://www.zcool.com.cn/article/ZMTUxNzk2.html");
		//设置你需要抓取的URL
//		curl_setopt($curl, CURLOPT_URL, "http://www.zcool.com.cn/article/ZMTUxNzk2.html");
		//伪造来路
		curl_setopt ($curl, CURLOPT_REFERER, "http://zcimg.zcool.com.cn/");
	
		//设置cURL 参数，要求结果保存到字符串中还是输出到屏幕上。
		curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);



  
		curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);  
		curl_setopt($curl, CURLOPT_BINARYTRANSFER, 1);

		//运行cURL，请求网页
		$data = curl_exec($curl);
		//关闭URL请求
		curl_close($curl);
//header("Content-type: image/jpeg");  


//	$dataStr = '/[x80-xff]+/';
//	preg_match_all($dataStr, $data, $list);

//    print_r($data)


	function getwebcontent($url){
		$ch = curl_init();
		$timeout = 10;
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
		curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);
		$contents = trim(curl_exec($ch));
		curl_close($ch);
		return  $contents;
	}
		
?>
		

	
	
	
	

 


	
</body>

</html>