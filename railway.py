import urllib.request, re, http.cookiejar, urllib.parse,datetime,os,subprocess,time,random,speech_recognition
class Ticket:
    StationList = []
    Error = (False, None)
    UrlOpener = None
    StationCode = {}
    UserAgent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chr' \
                 r'ome/52.0.2743.116 Safari/537.36'

    def __init__(self, searchdate, traincode):
        self.StationCode = self.GetStationCode()
        self.StationList = self.GetStationList(searchdate, traincode)
        if self.StationList == []:
            self.Error = (True, 'Not exist Train 404')
            return
        return

    def GetStationList(self, searchdate, traincode):
        cj = http.cookiejar.CookieJar()
        self.UrlOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        header = {
            'Host': 'twtraffic.tra.gov.tw',
            'User-Agent': self.UserAgent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en,en-US;q=0.7,zh-TW;q=0.3',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }
        url = r"http://twtraffic.tra.gov.tw/twrail/SearchResultContent.aspx?searchdate=" + searchdate \
              + r"&traincode=" + traincode
        req = urllib.request.Request(url=url, headers=header)
        response = self.UrlOpener.open(req).read().decode('utf-8')
        response = re.findall(r'''style="width:100px;">(.*?)</td>''', response)
        return response

    def GetStationCode(self):
        response = urllib.request.urlopen('http://railway.hinet.net/station_code.htm').read().decode('big5')
        name = re.findall(r'''<td class="cName">(.*?)</td>''',response)
        code = re.findall(r'''<td>(\w*?)</td>''',response)
        StationCode = dict(zip(name,code))
        return StationCode

    def BookTicket(self,SID,from_station,to_station,getin_date,train_no,order_qty_str):

        value={
        'person_id' : SID,
        'from_station' : from_station,
        'to_station' : to_station,
        'getin_date' : getin_date,
        'train_no' : train_no,
        'order_qty_str' : order_qty_str,
        't_order_qty_str' : '0',
        'n_order_qty_str' : '0',
        'd_order_qty_str' : '0',
        'b_order_qty_str' : '0',
        'z_order_qty_str' : '0',
        'returnTicket' : '0'
        }
        header={
            'Host': 'railway.hinet.net',
            'User-Agent': self.UserAgent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en,en-US;q=0.7,zh-TW;q=0.3',
            'Referer': 'http://railway.hinet.net/ctno1.htm',
            'Connection': 'keep-alive'
        }
        data = urllib.parse.urlencode(value).encode('utf-8')
        req = urllib.request.Request(url=r'''http://railway.hinet.net/check_ctno1.jsp''', headers=header,data=data)
        response=self.UrlOpener.open(req).read().decode('big5')
        return

    def GetCaptcha(self): #nedd change file name and return it
        value = {
            'pageRandom':'0.5010025438144057'
        }
        header = {
            'Host': 'railway.hinet.net',
            'User-Agent': self.UserAgent,
            'Accept': '*/*',
            'Accept-Language': 'en,en-US;q=0.7,zh-TW;q=0.3',
            'Referer': 'http://railway.hinet.net/check_ctno1.jsp',
            'Connection': 'keep-alive'
        }
        data = urllib.parse.urlencode(value).encode('utf-8')
        req = urllib.request.Request(url=r'''http://railway.hinet.net/ImageOut.jsp?pageRandom=0.5010025438144057''', headers=header, data=data)
        response = self.UrlOpener.open(req).read()
        f=open('./test.jpg','wb')
        f.write(response)
        return response

    def GetVoice(self): #nedd change file name and return it
        value = {
            'pageRandom': '0.39312307475596486'
        }
        header = {
            'Host': 'railway.hinet.net',
            'User-Agent': self.UserAgent,
            'Accept': 'audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5',
            'Accept-Language': 'en,en-US;q=0.7,zh-TW;q=0.3',
            'Referer': 'http://railway.hinet.net/check_ctno1.jsp',
            'Connection': 'keep-alive'
        }
        data = urllib.parse.urlencode(value).encode('utf-8')
        req = urllib.request.Request(url=r'''http://railway.hinet.net/PronounceRandonNumber.do?pageRandom=0.39312307475596486''',
                                     headers=header, data=data)
        response = self.UrlOpener.open(req).read()
        f = open('./test.wav', 'wb')
        f.write(response)
        return response

    def GetTicket(self,Captcha,SID,getin_date,from_station,to_station,order_qty_str,train_no):
        header={
        'Host': 'railway.hinet.net',
        'User-Agent': self.UserAgent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en,en-US;q=0.7,zh-TW;q=0.3',
        'Referer': 'http://railway.hinet.net/check_ctno1.jsp',
        'Connection': 'keep-alive'
        }
        url=r'''http://railway.hinet.net/order_no1.jsp?randInput=''' + Captcha + '''&person_id=''' + SID +\
            '''&getin_date=''' + getin_date + '''&from_station=''' + from_station +\
            '''&to_station=''' + to_station + '''&order_qty_str=''' + order_qty_str + '''&train_no=''' + train_no +\
            '''&returnTicket=0'''
        req=urllib.request.Request(url=url,headers=header)
        response = self.UrlOpener.open(req).read()
        return response

    def JudgeTicket(self,response):
        if '您的車票已訂到' in response:
            regex = r'''身分證字號：</span> <span id="spanPid" class="hv1 blue01 bold01">(.+?)</span>.+?電腦代碼：</span> <span id="spanOrderCode" class="hv1 red02 text_14p bold01">(\d+?)</span>.+?車次：</span> <span class="hv1 blue01 bold01">(\d+?)</span>.+?車種：</span> <span class="hv1 blue01 bold01">(.*?)</span>.+?乘車時刻：</span> <span class="hv1 blue01 bold01">(.+?)</span>.+?起站：</span> <span class="hv1 blue01 bold01">(.+?)</span>.+?到站：</span> <span class="hv1 blue01 bold01">(.+?)</span>.+?張數：</span> <span class="hv1 blue01 bold01">(\d+?)</span>.+?取票或網路付款截止時間：<br>車站、郵局請於	<span class="blue01 bold01">(.+?)</span>'''
            ticket = re.findall(regex,response)[0]
            key=['身分證字號','電腦代碼','車次','車種','乘車時刻','起站','到站','張數','取票截止時間']
            ticket=dict(zip(key,ticket))
            return (True,ticket)
        elif '您的身分證字號錯誤, 請重新輸入' in response:
            return (False,'Error SID 400')
        elif '起到站錯誤起到站錯誤' in response:
            return (False,'Error Station 400')
        elif '該區間無剩餘座位' in response:
            return (False,'Error Occupy 403.9')
        elif '該車次可訂票時間(含當日訂票)已過' in response:
            return (False,'Error too late 301')
        elif '電子資料錯誤' in response:
            return (False,'Error EData 400')
        return (False,'Error Unknown 0')

    def StoC(self,Station):
        if Station in self.StationCode.keys():
            return self.StationCode[Station]
        self.Error=(True,'Error StoC 404')
        return False

    def GetServerTime(self):
        req=urllib.request.urlopen('http://railway.hinet.net/').info()['Date']
        stime=datetime.datetime.strptime(req,'%a, %d %b %Y %H:%M:%S GMT')
        stime=stime+datetime.timedelta(hours=8)
        return stime

    def GetLocalTime(self):
        ltime=datetime.datetime.now()
        return ltime

    def alaw2pcm_s16le(self): #need fix
        os.chdir(r'ffmpeg\bin')
        subprocess.call(['ffmpeg', '-i', '../../65179.wav', '-c:a', 'pcm_s16le', '1.wav'])

    def voice2text(AudioFile):
        r = speech_recognition.Recognizer()
        with speech_recognition.WavFile(AudioFile) as source:
            audio = r.record(source)
        try:
            return r.recognize_google(audio_data=audio, language='zh_TW')
        except LookupError:
            return False

         #   sample SID A169351650