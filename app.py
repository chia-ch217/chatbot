from flask import Flask, request, abort
from linebot.models import *
from linebot import (
    LineBotApi, WebhookHandler)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError)
import requests
from bs4 import BeautifulSoup
from random import choice, random, randint
import re


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import xlrd
import xlwt

app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi(
    'kFpaNP3cTUOV5fHMTwaw74C2uDljFZrBAXRenvZHPMwmp9FeXs1H/OWNdJ6UH2gKnAUvob/Lo2X1S8tn8EJkq1jNvWRHV+o5LITOkPi/+R5JmbPYOvBantBQoSwFyO1uW8qh2eT8S9fat0Q5Oxbq/AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9adc024724fe8cb4d76e9e7bc5f5360e')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


list1 = ""


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global list1


    mtext = event.message.text
    if event.message.text in "[`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）——|{}【】‘；：”“'。，、？]0123456789":
        list1 = event.message.text
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="你是不是輸入特殊符號或數字刁難我!?"))

    # 0606加入
    elif event.message.text == '@彈性配置':
        sendFlex(event)
    elif event.message.text[:3] == '###' and len(event.message.text)> 3:manageForm(event, event.message.text)

    elif event.message.text == '@發票使用說明':
        sendUse(event)

    elif event.message.text == '@顯示本期中獎號碼':
        showCurrent(event)(event)

    elif event.message.text == '@顯示前期中獎號碼':
        showOld(event)

    elif event.message.text == '@輸入發票最後三碼':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入發票最後三碼進行對獎！'))

    elif len(event.message.text) == 3 and event.message.text.isdigit():
        show3digit2(event, event.message.text)

    elif len(event.message.text) == 5 and event.message.text.isdigit():
        show5digit(event, event.message.text)

    # 0606加入

    elif event.message.text != "@給你可愛的動物!" and event.message.text != "@去吃點東西吧!":
        list1 = event.message.text
        Carousel_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://images.chinatimes.com/newsphoto/2017-02-06/900/20170206001603.jpg',
                        title='請選擇',
                        text='工作地區',
                        actions=[
                            PostbackTemplateAction(
                                label='台北',
                                # text='請稍候',
                                data='100100'
                            ),
                            PostbackTemplateAction(
                                label='新北',
                                # text='請稍候',
                                data='100200'
                            ),
                            PostbackTemplateAction(
                                label='桃園',
                                # text='請稍候',
                                data='100500'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://cc.tvbs.com.tw/img/program/upload/2018/05/04/20180504142624-74ece794.jpg',
                        title='請選擇',
                        text='工作地區',
                        actions=[
                            PostbackTemplateAction(
                                label='台中',
                                # text='請稍候',
                                data='100900'
                            ),
                            PostbackTemplateAction(
                                label='台南',
                                # text='請稍候',
                                data='101600'
                            ),
                            PostbackTemplateAction(
                                label='高雄',
                                # text='請稍候',
                                data='101800'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://nba.udn.com/assets/cathay/img/kv.png',
                        title='請選擇',
                        text='行業類別',
                        actions=[
                            PostbackTemplateAction(
                                label='預測:軟體開發及程式設計師',
                                # text='請稍候',
                                data='prediction1'
                            ),
                            PostbackTemplateAction(
                                label='預測:資料庫及網路專業人員',
                                # text='請稍候',
                                data='prediction2'
                            ),
                            PostbackTemplateAction(
                                label='預測:資訊系統分析及設計師',
                                # text='請稍候',
                                data='prediction3'
                            ),
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, Carousel_template)
    #未完成 0606讀xml對話
    else:
        #openAIML(event, mtext)
        pass
    print("輸出1:", list1)


list2 = ""

"{}".format("請稍候")


@handler.add(PostbackEvent)  # 按鈕觸發縣市傳值做爬蟲
def handle_postback(event):
    global list2
    if event.postback.data == "100100":
        list2 = event.postback.data
        a = job()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif event.postback.data == "100200":
        list2 = event.postback.data
        a = job()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif event.postback.data == "100500":
        list2 = event.postback.data
        a = job()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif event.postback.data == "100600":
        list2 = event.postback.data
        a = job()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif event.postback.data == "100900":
        list2 = event.postback.data
        a = job()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif event.postback.data == "101600":
        list2 = event.postback.data
        a = job()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif event.postback.data == "101800":
        list2 = event.postback.data
        a = job()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))

    elif event.postback.data == "aaa":
        x = choice(["https://cdn2.ettoday.net/images/413/d413475.jpg",
                    "https://cdn2.ettoday.net/images/413/d413490.jpg",
                    "https://cdn2.ettoday.net/images/413/d413480.jpg",
                    "https://i1.kknews.cc/SIG=2sv3s13/31pn0000p3pp14rpn466.jpg",
                    "https://cdn2.ettoday.net/images/413/d413465.jpg",
                    "https://i2.kknews.cc/SIG=t3ta0e/qsvp-vzntrunaqyre/55916n42-r56s-4rp9-86p5-5nr2p74577nn.jpg",
                    "https://s.newtalk.tw/album/news/349/5e0c859a2e2e8.jpg",
                    "https://sites.google.com/site/yeyiyingwangyesheji/_/rsrc/1495511251252/ha-shi-qi/14389839027759.jpg?height=320&width=320"])

        message = ImageSendMessage(
            original_content_url=x,
            preview_image_url=x)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.postback.data == "bbb":
        y = choice(["https://www.fe-amart.com.tw/images/amart/photo/gillchou/20160517-5food/119new.jpg",
                    "https://cdn2.ettoday.net/images/1576/d1576399.jpg",
                    "https://compathy-magazine-assets.compathy.net/uploads/2019/08/sushi-4369011_640-640x426.jpg",
                    "https://cdn2.ettoday.net/images/3631/d3631257.jpg",
                    "https://cdn.walkerland.com.tw/images/upload/poi/p49084/m36235/8277f6d86f7f83ee2cd85a8568f855adf96ef5f5.jpg",
                    "https://images.chinatimes.com/newsphoto/2019-05-27/900/20190527003221.jpg",
                    ])

        message = ImageSendMessage(
            original_content_url=y,
            preview_image_url=y)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.postback.data == "prediction1":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(
            text="{}{}".format("點選以下網址唷 ! \n", "https://dash-data.herokuapp.com/")))
    elif event.postback.data == "prediction2":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(
            text="{}{}".format("點選以下網址唷 ! \n", "https://dash-data.herokuapp.com/")))
    elif event.postback.data == "prediction3":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(
            text="{}{}".format("點選以下網址唷 ! \n", "https://dash-data.herokuapp.com/")))
    print("輸出2:", list2)


@handler.add(MessageEvent, message=StickerMessage)  # 傳貼圖
def StickerMessage(event):
    # message = ImageSendMessage(
    # 	original_content_url='https://imgur.dcard.tw/WDWrBTO.jpg',
    #     preview_image_url='https://imgur.dcard.tw/WDWrBTO.jpg')
    # line_bot_api.reply_message(event.reply_token,message)

    Image_Carousel = TemplateSendMessage(
        alt_text='Image Carousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://topwinfix.com.tw/wp-content/uploads/2019/01/15208250579040.jpg',
                    action=PostbackTemplateAction(
                        label='壓力大點我一下',
                        text='@給你可愛的動物!',
                        data='aaa'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2017/12/18/20171218-113611_U9180_M359936_2d67.PNG?itok=CLjper4p',
                    action=PostbackTemplateAction(
                        label='壓力大點我一下',
                        text='@去吃點東西吧!',
                        data='bbb'
                    )
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, Image_Carousel)


def num():
    url = "https://www.1111.com.tw/job-bank/job-index.asp?si=1&ss=s&ks={}&c0={}&page=1".format(list1, list2)
    my_header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
    rs = requests.session()
    resp = rs.get(url, headers=my_header)
    # print("狀態碼", rs.status_code)
    soup = BeautifulSoup(resp.text, "html.parser")
    content = ""

    page_num = soup.select_one('select.custom-select').text.split("/")
    a = page_num[0]
    b = page_num[1].lstrip()
    aaa = randint(1, int(b))
    print("頁數:", aaa)
    return aaa


def job():
    url = "https://www.1111.com.tw/job-bank/job-index.asp?si=1&ss=s&ks={}&c0={}&page={}".format(list1, list2, num())
    my_header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
    rs = requests.session()
    resp = rs.get(url, headers=my_header)
    # print("狀態碼", rs.status_code)
    soup = BeautifulSoup(resp.text, "html.parser")
    content = ""
    title = soup.select("div.position0 > a.text-truncate")
    company = soup.select("div.d-none > a.d-block")
    href = soup.select("div.position0 > a.text-truncate")

    for t, c, h in zip(title, company, href):
        tt = t.get("title")
        cc = c.get("title")
        hh = 'https://www.1111.com.tw/' + h.get("href")
        content += '\n《工作》{}\n{}\n《連結》{}\n-----我是分隔線-----'.format(tt, cc, hh)
        print(content)
    print("資料抓取完畢")

    return content


#0606新加入
####################################
def sendFlex(event):  #彈性配置
    try:
        print("123:::::")
        bubble = BubbleContainer(
            direction='ltr',  #項目由左向右排列
            header=BoxComponent(  #標題
                layout='vertical',
                contents=[
                    TextComponent(text='冰火飲料', weight='bold',
size='xxl'),
                ]
            ),
            hero=ImageComponent(  #主圖片
                url='https://i.imgur.com/3sBRh08.jpg',
                size='full',
                aspect_ratio='792:555',  #長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(  #主要內容
                layout='vertical',
                contents=[
                    TextComponent(text='評價', size='md'),
                    BoxComponent(
                        layout='baseline',  #水平排列
                        margin='md',
                        contents=[
                            IconComponent(size='lg',
url='https://i.imgur.com/GsWCrIx.png'),
                            TextComponent(text='25   ', size='sm',
color='#999999', flex=0),
                            IconComponent(size='lg',
url='https://i.imgur.com/sJPhtB3.png'),
                            TextComponent(text='14', size='sm',
color='#999999', flex=0),
                        ]
                    ),
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業地址:',
color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text='台北市信義路14號', color='#666666', size='sm', flex=5)
                                ],
                            ),
                            SeparatorComponent(color='#0000FF'),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業時間:',
color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text="10:00 -23:00", color='#666666', size='sm', flex=5),
                                ],
                            ),
                        ],
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=URIAction(label='電話聯絡',
uri='tel:0987654321'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=URIAction(label='查看網頁',
uri="http://www.e-happy.com.tw")
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(  #底部版權宣告
                layout='vertical',
                contents=[
                    TextComponent(text='Copyright@ehappy studio2019', color='#888888', size='sm', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="彈性配置範例",
contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage
(text='發生錯誤！'))

def manageForm(event, mtext):
    try:
        flist = mtext[3:].split('/')
        text1 = '姓名：' + flist[0] + '\n'
        text1 += '日期：' + flist[1] + '\n'
        text1 += '包廂：' + flist[2]
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage
(text='發生錯誤！'))


def sendFlex(event):  #彈性配置
    try:
        bubble = BubbleContainer(
            direction='ltr',  #項目由左向右排列
            header=BoxComponent(  #標題
                layout='vertical',
                contents=[
                    TextComponent(text='冰火飲料', weight='bold', size='xxl'),
                ]
            ),
            hero=ImageComponent(  #主圖片
                url='https://i.imgur.com/3sBRh08.jpg',
                size='full',
                aspect_ratio='792:555',  #長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(  #主要內容
                layout='vertical',
                contents=[
                    TextComponent(text='評價', size='md'),
                    BoxComponent(
                        layout='baseline',  #水平排列
                        margin='md',
                        contents=[
                            IconComponent(size='lg', url='https://i.imgur.com/GsWCrIx.png'),
                            TextComponent(text='25   ', size='sm', color='#999999', flex=0),
                            IconComponent(size='lg', url='https://i.imgur.com/sJPhtB3.png'),
                            TextComponent(text='14', size='sm', color='#999999', flex=0),
                        ]
                    ),
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業地址:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text='台北市信義路14號', color='#666666', size='sm', flex=5)
                                ],
                            ),
                            SeparatorComponent(color='#0000FF'),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業時間:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text="10:00 - 23:00", color='#666666', size='sm', flex=5),
                                ],
                            ),
                        ],
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=URIAction(label='電話聯絡', uri='tel:0987654321'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=URIAction(label='查看網頁', uri="http://www.e-happy.com.tw")
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(  #底部版權宣告
                layout='vertical',
                contents=[
                    TextComponent(text='Copyright@ehappy studio 2019', color='#888888', size='sm', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="彈性配置範例", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def manageForm(event, mtext):
    try:
        flist = mtext[3:].split('/')
        text1 = '姓名：' + flist[0] + '\n'
        text1 += '日期：' + flist[1] + '\n'
        text1 += '包廂：' + flist[2]
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#0606新加入發票
####################################

def sendUse(event):  #使用說明
    try:
        text1 ='''
1. 「對獎」功能會提示使用者輸入發票最後三碼，若最後三碼有中獎，就提示使用者輸入發票前五碼。
2. 為方便使用者輸入，也可以直接輸入發票最後三碼直接對獎 (不需按「對獎」項目)。
3. 「前期中獎號碼」功能會顯示前兩期發票中獎號碼。
4. 「本期中獎號碼」功能會顯示最近一期發票中獎號碼。
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def showCurrent(event):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析XML
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        title = items[0][0].text  #期別
        ptext = items[0][2].text  #中獎號碼
        ptext = ptext.replace('<p>','').replace('</p>','\n')
        message = title + '月\n' + ptext[:-1]  #ptext[:-1]為移除最後一個\n
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

def showOld(event):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析XML
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        message = ''
        for i in range(1,3):
            title = items[i][0].text  #期別
            ptext = items[i][2].text  #中獎號碼
            ptext = ptext.replace('<p>','').replace('</p>','\n')
            message = message + title + '月\n' + ptext + '\n'
        message = message[:-2]
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))


def show3digit2(event, mtext):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        ptext = items[0][2].text  #中獎號碼
        ptext = ptext.replace('<p>','').replace('</p>','')
        temlist = ptext.split('：')
        prizelist = []  #特別獎或特獎後三碼
        prizelist.append(temlist[1][5:8])
        prizelist.append(temlist[2][5:8])
        prize6list1 = []  #頭獎後三碼六獎中獎號碼
        for i in range(3):
            t1=temlist[3][9*i+5:9*i+8]
            prize6list1.append(t1)
            print(t1)
        prize6list2 = temlist[4].split('、')  #增開六獎
        #unit = users.objects.get(uid=userid)
        #unit.state = 'no'
        #unit.save()
        if mtext in prizelist:
            message = '符合特別獎或特獎後三碼，請繼續輸入發票前五碼！'
            #unit = users.objects.get(uid=userid)
            #unit.state = 'special'
            #unit.save()
        elif mtext in prize6list1:
            message = '恭喜！至少中六獎，請繼續輸入發票前五碼！'
            #unit = users.objects.get(uid=userid)
            #unit.state = 'head'
            #unit.save()
        elif mtext in prize6list2:
            message = '恭喜！此張發票中了六獎！'
        else:
            message = '很可惜，未中獎。請輸入下一張發票最後三碼。'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))





def show5digit2(event, mtext):
    try:
        #unit = users.objects.get(uid=userid)
        # mode = unit.state
        mode='special'

        if mode == 'no':
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請先輸入發票最後三碼！'))
        else:
            try:
                content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
                tree = ET.fromstring(content.text)  #解析DOM
                items = list(tree.iter(tag='item'))  #取得item標籤內容
                ptext = items[0][2].text  #中獎號碼
                ptext = ptext.replace('<p>','').replace('</p>','')
                temlist = ptext.split('：')
                special1 = temlist[1][0:5]  #特別獎前五碼
                special2 = temlist[2][0:5]  #特獎前五碼
                prizehead = []  #頭獎前五碼
                for i in range(3):
                    prizehead.append(temlist[3][9*i:9*i+5])
                sflag = False  #記錄是否中特別獎或特獎
                print("1")
                if mode=='special' and mtext==special1:
                    message = '恭喜！此張發票中了特別獎！'
                    sflag = True
                elif mode=='special' and mtext==special2:
                    message = '恭喜！此張發票中了特獎！'
                    sflag = True
                if mode=='special' and sflag==False:
                    message = '很可惜，未中獎。請輸入下一張發票最後三碼。'
                elif mode=='head' and sflag==False:
                    if checkhead(mtext, prizehead[0], prizehead[1], prizehead[2]):
                        message = '恭喜！此張發票中了頭獎！'
                    elif checkhead(mtext[1:5], prizehead[0][1:5], prizehead[1][1:5], prizehead[2][1:5]):
                        message = '恭喜！此張發票中了二獎！'
                    elif checkhead(mtext[2:5], prizehead[0][2:5], prizehead[1][2:5], prizehead[2][2:5]):
                        message = '恭喜！此張發票中了三獎！'
                    elif checkhead(mtext[3:5], prizehead[0][3:5], prizehead[1][3:5], prizehead[2][3:5]):
                        message = '恭喜！此張發票中了四獎！'
                    elif checkhead(mtext[4], prizehead[0][4], prizehead[1][4], prizehead[2][4]):
                        message = '恭喜！此張發票中了五獎！'
                    else:
                        message = '恭喜！此張發票中了六獎！'
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
                #unit = users.objects.get(uid=userid)
                #unit.state = 'no'
                #unit.save()
            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

    except:
        #unit = users.objects.get(uid=userid)
        #unit.state = 'no'
        #unit.save()

        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='模式文字檔讀取錯誤！1'))

import aiml

def openAIML(event, mtext):
    try:
        show=""
        # Create the kernel and learn AIML files
        kernel = aiml.Kernel()
        kernel.learn("05-AIML-load.xml")
        kernel.respond("load aiml b")

        try:
                show=kernel.respond(mtext)
                print(show)
        except:
                print("error")

        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=show))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='模式文字檔讀取錯誤！2'))





import os

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8888))  # 固定-ngrok用

# =============================================================================
# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 8888))
#     app.run(host='0.0.0.0', port=port)
# =============================================================================