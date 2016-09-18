#search station  http://twtraffic.tra.gov.tw/twrail/SearchResultContent.aspx?searchdate=2016/09/17&traincode=543
# http://twtraffic.tra.gov.tw/twrail/Ticketing.aspx?from_station=108&to_station=175&getin_date=2016/09/19&train_no=543
# get station code http://twtraffic.tra.gov.tw/twrail/Ticketing.aspx?from_station=108&to_station=175&getin_date=2016/09/19&train_no=105
#POST /check_ctno1.jsp HTTP/1.1
#您的身分證字號錯誤, 請重新輸入
#該車次可訂票時間(含當日訂票)已過
#電子資料錯誤
# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.WavFile(r"C:\Users\Rose\Desktop\railway_TW\test.wav1.wav") as source:
#      audio = r.record(source)
#
# try:
#      print("Transcription: " + r.recognize_google(audio_data=audio,language='zh_TW',show_all=True))
# except LookupError:
#      print("Could not understand audio")
# exit()



import railway,time
a=railway.Ticket(r'2016/09/17','543')
a.BookTicket(r'A169351650','108','175',r'2016/09/19-01','505','1')
a.GetCaptcha()
a.GetVoice()
#print(a.GetTicket(input('Captcha:'),r'A169351650',r'2016/09/19-01','111','111','1','111').decode('big5'))
# res=r'''<head>
# 	<title>車次訂票結果</title>
# 	<meta http-equiv="Content-Type" content="text/html; charset=big5">
# 	<meta http-equiv="Pragma" content="no-cache">
# 	<meta http-equiv="Cache-Control" content="no-cache">
# 	<link href="./CssStyle/master.css" rel="stylesheet" type="text/css">
# 	<style type="text/css">
# 		input, select {font-family:Arial;}
# 		span.hd1 {width:100px;}
# 		span.hv1 {width:150px;}
# 	</style>
# </head>
# <body>
# <div><a href="#" accesskey="C" title="中間主要內容區，此區塊呈現網頁的網頁內容">:::</a></div>
# <table border="0" width="750"><tbody><tr><td style="text-align:left" background="./Images/title_bg.jpg"><img src="./Images/title_01.jpg" alt="車次訂單程票"></td></tr></tbody></table><br>
# <p><font class="orange02"><strong>您的車票已訂到</strong></font></p><p class="gray01"><span class="hd1">身分證字號：</span> <span id="spanPid" class="hv1 blue01 bold01">A169351650</span></p><p class="gray01"><span class="hd1">電腦代碼：</span> <span id="spanOrderCode" class="hv1 red02 text_14p bold01">111111</span></p><p class="gray01"><span class="hd1">車次：</span> <span class="hv1 blue01 bold01">111</span><span class="hd1">車種：</span> <span class="hv1 blue01 bold01">自強</span></p><p class="gray01"><span class="hd1">乘車時刻：</span> <span class="hv1 blue01 bold01">2016/09/20 18:56</span></p><p class="gray01"><span class="hd1">起站：</span> <span class="hv1 blue01 bold01">高雄    </span><span class="hd1">到站：</span> <span class="hv1 blue01 bold01">台北    </span><span class="hd1">張數：</span> <span class="hv1 blue01 bold01">01</span></p><p class="gray01">取票或網路付款截止時間：<br>車站、郵局請於	<span class="blue01 bold01">2016/09/19</span> 營業時間內完成取票<br>超商請於		<span class="blue01 bold01">2016/09/19 24:00</span> 前完成付款取票<br>網路付款請於	<span class="blue01 bold01">2016/09/19 24:00</span> 前完成付款<br>郵局及超商須另支付每張8元取票服務費<br><b>若您3個月內逾期未取票累計3次，系統將停止受理訂票6個月</b></p><p>郵輪式列車車票不開放網路付款系統、對號列車自動售票機取票</p><p></p><script language="javascript" src="./pay.js"></script><noscript></noscript><form id="goPayForm" onsubmit="return goPay();" action="https://ticket.chinatrust.com.tw/railway/index.php" method="post" target="_blank" style="float:left;"><input name="howgo" type="hidden"><input name="na" type="hidden"><input name="id1" type="hidden"><input name="go1sn" type="hidden"><input name="id2" type="hidden"><input name="go2sn" type="hidden"><input name="id3" type="hidden"><input name="go3sn" type="hidden"><button type="submit" style="border:0;background:white;width:150px;"><img src="./Images/pay02_a.jpg" alt="網路付款(另開視窗)" onmouseover="this.src='./Images/pay02_b.jpg'" onmouseout="this.src='./Images/pay02_a.jpg'" onfocus="this.src='./Images/pay02_b.jpg'" onblur="this.src='./Images/pay02_a.jpg'"></button></form><form name="form1" method="post" action="ccancel.jsp" style="margin-left:100px;"><input name="personId" value="A169351650" type="hidden"><input name="orderCode" value="951104" type="hidden"><button type="submit" style="border:0;background:white;width:150px;"><img src="./Images/delete02_a.jpg" alt="取消此車次訂票" onmouseover="this.src='./Images/delete02_b.jpg'" onmouseout="this.src='./Images/delete02_a.jpg'" onfocus="this.src='./Images/delete02_b.jpg'" onblur="this.src='./Images/delete02_a.jpg'"></button></form>
#
#
#
# </body>'''
# print(a.JudgeTicket(res))

# 身分證字號       身分證字號：</span> <span id="spanPid" class="hv1 blue01 bold01">A169351650</span>
# 電腦代碼         電腦代碼：</span> <span id="spanOrderCode" class="hv1 red02 text_14p bold01">111111</span>
# 車次             車次：</span> <span class="hv1 blue01 bold01">111</span>
# 車種             車種：</span> <span class="hv1 blue01 bold01">自強</span>
# 乘車時刻         乘車時刻：</span> <span class="hv1 blue01 bold01">2016/09/20 18:56</span>
# 起站             起站：</span> <span class="hv1 blue01 bold01">高雄    </span>
# 到站             到站：</span> <span class="hv1 blue01 bold01">台北    </span>
# 張數             張數：</span> <span class="hv1 blue01 bold01">01</span>
# 取票截止時間     取票或網路付款截止時間：<br>車站、郵局請於	<span class="blue01 bold01">2016/09/19</span>
#
# re.findall(,)