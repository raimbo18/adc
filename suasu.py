from GENERATOR import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
#from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib3, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\n\nLOGINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\n")

#cl = RIDEN()
cl = RIDEN(authTokenRFU="EwjA7BGA87lPrc4L0zU9.grzYgOnTdKvSkrQ7FTsKMq.TmsMcUZV6F1pLmV4TxQ5RDSN8NwxUg/x9iFFmCoYF6s=")
#EwjA7BGA87lPrc4L0zU9.grzYgOnTdKvSkrQ7FTsKMq.TmsMcUZV6F1pLmV4TxQ5RDSN8NwxUg/x9iFFmCoYF6s= #PUYZ
#Ewf9dhbOZOVz2Tjmxvh3.Ri4/RX6YPvDWVXddSJv8mW.pXW2aITg+vn3GaZlSkonXf8zqwUbbuCfU6/PPo1VfPE= #PUY
cl.log("YOUR TOKEN : {}".format(str(cl.authToken)))
channel = RIDENChannel(cl,cl.server.CHANNEL_ID['LINE_TIMELINE'])
cl.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

print ("LOGIN SUCCESS")

clProfile = cl.getProfile()
clSettings = cl.getSettings()
RIDEN = RIDENPoll(cl)

Puy = [cl]
mid = cl.profile.mid
PuyBot=[mid]
Owner=["uac8e3eaf1eb2a55770bf10c3b2357c33"]
PuySekawan = PuyBot + Puy + Owner

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

PUYWAIT = {
    "Contact":False,
    "GName":"PUYからコミュニティにシンプル",
    "AutoRespon":False,
    "KickRespon":False,
    "autoAdd":True,
    "PesanAdd":"",
    "ContactAdd":{},
    "autoJoin":True,
    "AutojoinTicket":True,
    "AutoReject":False,
    "autoRead":False,
    "Timeline":False,
    "Welcome":False,
    "WcText": "Selamat Datang",
    "Leave":False,
    "WvText": "Selamat Jalan",
    "Adminadd":False,
    "AdminDel":False,
    "readMember":{},
    "readPoint":{},
    "readTime":{},
    "ROM":{},
    "AddMention":True,
    "Admin": {
        "uac8e3eaf1eb2a55770bf10c3b2357c33":True  #MID ADMIN HERE
    },
}

Mozilla = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

setTime = {}
setTime = PUYWAIT['readTime']
mulai = time.time()
msg_dict = {}

ProfileMe = {
    "displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
ProfileMe["displayName"] = clProfile.displayName
ProfileMe["statusMessage"] = clProfile.statusMessage
ProfileMe["pictureStatus"] = clProfile.pictureStatus

PuyCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Helpz ="""    「 Commands 」
@Fun
Ceksider
Gsteal
Psteal
Mysteal"""

Gsteal ="""    「 GroupSteal 」
Type: Steal Group Information

  1. Foto Grup
  2. Nama Grup
  3. Pembuat Grup
  4. Anggota Grup
  5. Url
  6. ID Grup

Penggunaan: Gsteal 「nomor」
Contoh: Gsteal 1"""

Siderz ="""    「 Lurking 」
Type: Ceksider

  1. Manual Lurking
  2. Auto Lurking

Menjalankan: Ceksider 「nomor」 on/off
Contoh: Ceksider 2 on"""

Profilez ="""    「 ProfileSteal 」
Type: Steal Profile

  1. Picture
  2. Bio
  3. Cover
  4. VidProfile
  5. MID

Penggunaan: Psteal 「nomor」 「Mention」
Contoh: Psteal 1 @"""

Helpadmin ="""    「 Own/Adm Commands 」
Hapus chat
Mulai ulang
Bot keluar
Glist
Tolak Undangan
Broadcastbc:
Contactbc:
All respon / Def respon
Leave on/off
Autoreject on/off
Autojoin on/off
Jointicket on/off
Changeleave: [query]
Welcomsg on/off
Changewelcome: [query]
Status
Refreshprofile
Refresh
Adminadd:on/off
Adminrem:on/off
Devlist
Tokenlist"""

Instaz ="""    「 Fun Commands 」
Type: Instagram Profile Info

  1. Instainfo
  2. Instainfo Full
  3. Instastory
  4. Instapost

Penggunaan: Info 「nomor」
Contoh: Info 2 「Username」"""

Mystealz ="""    「 MySteal 」
Type: Steal Profile

  1. Name
  2. Bio
  3. Profile Picture
  4. Video Profile
  5. Cover

Penggunaan: Mys 「nomor」
Contoh: Mys 1"""

Helpz2 ="""    「 Fun Commands 」
Me
Calendar
Wikipedia: [query」
Write 「text」
1Cak
Instainfo1: 「username」
Instainfo2 「username」
Deviantart 「query」
Artinama1 「nama」
Artinama2 「nama」
Wallhd 「query」
Drakor 「query」
Drakor2 「query」
Cekrobot 「nama」
Cari 「query」
Creepypasta
Carigambar 「query」
Berita hangat
Motivasi
Quotes"""

#------------------------------------------------ SCRIP DEF ----------------------------------------------------------#

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def RIDEN_FAST_USER(fast):
    try:
        if fast.type == 0:
            return
        if fast.type == 5:
            if PUYWAIT["autoAdd"] == True:
                if (PUYWAIT["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    PUYWAIT["ContactAdd"][fast.param2] = True
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} " + str(PUYWAIT["PesanAdd"]).format(usr.displayName))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':mid}, contentType=13)
#--------------------------------------------- PARAM SCRIP AUTO JOIN BOT & AUTO REJECT ------------------------------------------------#
        if fast.type == 13:
            if mid in fast.param3:
              if PUYWAIT['autoJoin'] == True:
                #if fast.param2 in PuySekawan and fast.param2 in PUYWAIT["Admin"]:
                    cl.acceptGroupInvitation(fast.param1)
                    #cl.sendImageWithURL(fast.param1, "https://vignette.wikia.nocookie.net/clubpenguin/images/2/2d/Illuminati.png")
                    ginfo = cl.getGroup(fast.param1)
                    contact = cl.getContact(fast.param2)
                    _session = requests.session()
                    image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                    headers = {
                        "Host": "game.linefriends.com",
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0",
                        "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                    }
                    data = {
                        "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                        "to": fast.param1,
                        "messages": [
                            {
                                "type": "template",
                                "altText": "Puy",
                                "template": {
                                    "type": "carousel",
                                    "actions": [],
                                    "columns": [
                                        {
                                            "thumbnailImageUrl": "https://data.whicdn.com/images/308302664/original.gif",
                                            "title": "Masuk ke grup {}".format(str(ginfo.name)),
                                            "text": "Diundang oleh {}".format(str(contact.displayName)),
                                            "imageAspectRatio": "rectangle",
                                            "imageBackgroundColor": "#FFFFFF",
                                            "imageSize": "contain",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Perintah",
                                                    "uri": "line://msg/text/@cmd"
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Pembuat",
                                                    "uri": "line://msg/text/about"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                    data = json.dumps(data)
                    sendPost = _session.post(url, data=data, headers=headers)
                    print ("Joined Group")

        if fast.type == 13:
            if mid in fast.param3:
              if PUYWAIT['autoJoin'] == True:
                if fast.param2 in Owner and fast.param2 in PUYWAIT["Admin"]:
                    cl.acceptGroupInvitation(fast.param1)
                    print ("JOIN GRUP OLEH OWNER")

        if fast.type == 13:
            if mid in fast.param3:
              if PUYWAIT['AutoReject'] == True:
                if fast.param2 not in PuySekawan and fast.param2 not in PUYWAIT["Admin"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP SIDER & WC LV ------------------------------------------------#

        elif fast.type == 55:
            try:
                if PuyCctv['Point1'][fast.param1]==True:
                    if fast.param1 in PuyCctv['Point2']:
                        Name = cl.getContact(fast.param2).displayName
                        if Name in PuyCctv['Point3'][fast.param1]:
                            pass
                        else:
                            PuyCctv['Point3'][fast.param1] += "「" + Name + "」 \n"
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cl.mentionWithRFU(fast.param1,fast.param2,"and the Reader Comes ","" + " ")
                                else:
                                    cl.mentionWithRFU(fast.param1,fast.param2,"Si, ","" + "Telah Membaca")
                            else:
                                cl.mentionWithRFU(fast.param1,fast.param2,"Si, ","" + "Sudah membaca")
                    else:
                        cl.mentionWithRFU(fast.param1,fast.param2,"Hei, ","" + "How are you today?")
                else:
                    pass
            except:
                pass

        if fast.type == 55:
            try:
                if fast.param1 in PUYWAIT['readPoint']:
                    if fast.param2 in PUYWAIT['readMember'][fast.param1]:
                        pass
                    else:
                        PUYWAIT['readMember'][fast.param1] += fast.param2
                    PUYWAIT['ROM'][fast.param1][fast.param2] = fast.param2
                else:
                   pass
            except:
                pass

        if fast.type == 17:
            if PUYWAIT["Welcome"] == True:
                if fast.param2 not in Puy:
                    #cl.sendText(kirim,"さようなら\n" + str(" "+ginfo.name+" "))
                    ginfo = cl.getGroup(fast.param1)
                    contact = cl.getContact(fast.param1)
                    _session = requests.session()
                    image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                    headers = {
                        "Host": "game.linefriends.com",
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0",
                        "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                    }
                    data = {
                        "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                        "to": fast.param1,
                        "messages": [
                            {
                                "type": "flex",
                                "altText": "Puy",
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "   「 Member Joined 」\n", #% (elapsed_time),
                                                "size": "md",
                                                "weight": "bold",
                                                "align": "center",
                                                "gravity": "top",
                                                "color": "#000000",
                                            },
                                            {
                                                "type": "text",
                                                #"text": "%s" % (elapsed_time),
                                                "text": "Selamat Datang di {}{}".format(str(contact.displayName)),
                                                #.format(str(contact.displayName))
                                                #.format(str(ginfo.name)),
                                                "size": "md",
                                                "align": "center",
                                                "gravity": "top",
                                                "color": "#0000ff",
                                                "wrap": True
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                    data = json.dumps(data)
                    sendPost = _session.post(url, data=data, headers=headers)
                    #cl.mentionWithPuy(fast.param1,fast.param2," Hello","" + "\n " + str(PUYWAIT['WcText']))
                    #cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if fast.type == 15:
            if PUYWAIT["Leave"] == True:
                if fast.param2 not in Puy:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2," Hello","" + "\n " + str(PUYWAIT['LvText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

#--------------------------------------------- PARAM SCRIP ------------------------------------------------#

        if fast.type == 46:
            if fast.param2 in PuyBot:
                cl.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 26:
            msg = fast.message
            text = msg.text
            PuyText = msg.text
            msg_id = msg.id
            kirim = msg.to
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if PUYWAIT["autoRead"] == True:
                        cl.sendChatChecked(kirim, msg_id)
                    if kirim in PUYWAIT["readPoint"]:
                        if user not in PUYWAIT["ROM"][kirim]:
                            PUYWAIT["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(kirim,text)
                    if PUYWAIT["Timeline"] == True:
                       if msg.contentType == 16:
                            ret_ = " ㄔPosting Infoㄔ\n"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(user)
                                auth = "\n Author : {}".format(str(contact.displayName))
                            else:
                                auth = "\n Author : {}".format(str(contact.displayName))
                                ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Object Url : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n Media Url : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Object Url : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n Media Url : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Object Url : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek Url : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                dia = cl.getContact(user)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = 'Pengirim: '
                                xteam = str(dia.displayName)
                                pesan = ''
                                pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                zx2.append(zx)
                                kata = "\n Text : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n Post Url : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += kata
                                zxc += pesan2
                                pesan = xpesan + zxc + ret_ + ""
                                cl.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

#======= AUTO TAG & CHAT BATAS SCRIP ========#
        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in mid and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if PUYWAIT['AutoRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(PUYWAIT['MentionText'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  break

        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in PuySekawan or user not in PUYWAIT["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if PUYWAIT['KickRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "   『 Auto Reply 』\nWhat's Important?","   『 Auto Reply 』\nWas Sleeping"]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithRFU(kirim,user,"","" +str(ret_))
                                  cl.kickoutFromGroup(kirim,[user])
                                  break

#------------------- ( 3 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            text = msg.text
            PuyText = msg.text
            msg_id = msg.id
            kirim = msg.to
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if PUYWAIT["autoRead"] == True:
                        cl.sendChatChecked(0, msg_id)

                    elif PuyText is None:
                        return
                    else:
                        if PuyText.lower() == 'PROSES TRANSISI':
                            cl.sendMessage(0, user)

                        elif PuyText.lower() == "@cmd":
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                 cl.sendMessage(kirim, str(Helpz))

                        elif PuyText.lower() == "insta":
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                 cl.sendMessage(kirim, str(Instaz))

                        elif PuyText.lower() == "ceksider":
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                 cl.sendMessage(kirim, str(Siderz))

                        elif PuyText.lower() == "gsteal":
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                 cl.sendMessage(kirim, str(Gsteal))

                        elif PuyText.lower() == "psteal":
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                 cl.sendMessage(kirim, str(Profilez))

                        elif PuyText.lower() == "mysteal":
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                 cl.sendMessage(kirim, str(Mystealz))

                        elif PuyText.lower() == "@admin":
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                 cl.sendMessage(kirim, str(Helpadmin))

                        elif PuyText.lower() == "@fun":
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                 cl.sendMessage(kirim, str(Helpz2))

                        elif PuyText.lower() == "devlist":
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                Puy = ""
                                sekawan = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    Puy += str(wa) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in PUYWAIT["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    sekawan += str(wi) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendText(kirim,"     「 Devlist 」\nOwner :\n"+Puy+"\nAdmin :\n"+sekawan+" ") #+ str(len(Owner)+len(PUYWAIT["Admin"])))

                        elif PuyText.lower() == "glist":
                            groups = cl.getGroupIdsJoined()
                            ret_ = "      「 Group List 」"
                            no = 0
                            for gid in groups:
                                group = cl.getGroup(gid)
                                no += 1
                                ret_ += "\n{}. {} = {} Members".format(str(no), str(group.name), str(len(group.members)))
                            ret_ += "\n   「 {} Groups 」".format(str(len(groups)))
                            cl.sendText(kirim, str(ret_))

                        elif PuyText.lower() == "@bye": #With INDUK
                                ginfo = cl.getGroup(kirim)
                                _session = requests.session()
                                image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                headers = {
                                    "Host": "game.linefriends.com",
                                    "Content-Type": "application/json",
                                    "User-Agent": "Mozilla/5.0",
                                    "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                                }
                                data = {
                                    "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                    "to": to,
                                    "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "Puy",
                                            "contents": {
                                                "type": "bubble",
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "Keluar Grup", #% (elapsed_time),
                                                            "size": "lg",
                                                            "weight": "bold",
                                                            "align": "start",
                                                            "gravity": "top",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "separator"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "Dadah '{}' Invite kembali jika Perlu.".format(str(ginfo.name)),
                                                            "size": "sm",
                                                            "align": "start",
                                                            "gravity": "top",
                                                            "color": "#0000ff",
                                                            "wrap": True
                                                        }
                                                    ]
                                                }
                                            }
                                        }
                                    ]
                                }
                                data = json.dumps(data)
                                sendPost = _session.post(url, data=data, headers=headers)
                                #cl.sendText(kirim,"さようなら\n" + str(" "+ginfo.name+" "))
                                cl.leaveGroup(kirim)
                                print ("Anda Keluar Grup")

                        elif PuyText.lower() == "leaveall grup":
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Leave All group")

                        elif PuyText.lower() == 'url on':
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)

                        elif PuyText.lower() == "asking ":
                            query = cmd.replace("asking ","")
                            sch = query.replace(" ","+")
                            with requests.session() as web:
                               urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                               r = web.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                               data = r.text
                               data = json.loads(data)
                               url = data["shorturl"]
                               ret_ = "\n"
                               ret_ += " => Link : {}".format(str(url))
                               cl.sendMessage(kirim, "Question is < " + query + " > " + str(ret_))

                        elif PuyText.lower() == 'url off':
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)

                        elif PuyText.lower() == 'gsteal 1':
                                group = cl.getGroup(kirim)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                                cuki = "Below"
                                #cuki += "Group Name : {}".format(str(group.name))
                                #cuki += "\nID Group : {}".format(group.id)
                                #cuki += "\nGroup Creator : {}".format(str(gCreator))
                                #cuki += "\nMembers : {}".format(str(len(group.members)))
                                #cuki += "\nPendings Member : {}".format(gPending)
                                #cuki += "\nGroup Ticket Status : {}".format(gTicket)
                                #cuki += "\nGroup Qr : {}".format(gQr)
                                #cl.sendMessage(kirim, str(cuki))
                                cl.sendImageWithURL(kirim, path)

                        elif PuyText.lower() == 'gsteal 2':
                                group = cl.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                                cuki = ""
                                cuki += "「Grup」\nNama Grup:\n{}".format(str(group.name))
                                #cuki += "\nID Group : {}".format(group.id)
                                #cuki += "\nGroup Creator : {}".format(str(gCreator))
                                #cuki += "\nMembers : {}".format(str(len(group.members)))
                                #cuki += "\nPendings Member : {}".format(gPending)
                                #cuki += "\nGroup Ticket Status : {}".format(gTicket)
                                #cuki += "\nGroup Qr : {}".format(gQr)
                                cl.sendMessage(kirim, str(cuki))

                        elif PuyText.lower() == 'gsteal 3':
                                group = cl.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                                cuki = ""
                                #cuki += "Nama Grup: {}".format(str(group.name))
                                #cuki += "\nID Group : {}".format(group.id)
                                cuki += "「Grup」\nPembuat Grup:\n{}\n  Kontaknya:".format(str(gCreator))
                                #cuki += "\nMembers : {}".format(str(len(group.members)))
                                #cuki += "\nPendings Member : {}".format(gPending)
                                #cuki += "\nGroup Ticket Status : {}".format(gTicket)
                                #cuki += "\nGroup Qr : {}".format(gQr)
                                cl.sendMessage(kirim, str(cuki))
                                cl.sendContact(kirim, group.creator.mid)

                        elif PuyText.lower() == 'gsteal 4':
                                group = cl.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Mati"
                                    gTicket = "Mati"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                                cuki = ""
                                cuki += "「Grup」\nAnggota:\n{}".format(str(len(group.members)))
                                cl.sendMessage(kirim, str(cuki))

                        elif PuyText.lower() == 'gsteal 5':
                          #if user in PuySekawan or user in PUYWAIT["Admin"]:
                            if msg.toType == 2:
                                grup = cl.getGroup(kirim)
                                if grup.preventedJoinByTicket == True:
                                   grup.preventedJoinByTicket == False
                                   cl.updateGroup(grup)
                                set = cl.reissueGroupTicket(kirim)
                                cl.sendMessage(kirim, "「Grup」\nGrup Url:\nhttps://line.me/R/ti/g/{}".format(str(set)))
                            #else:
                            #    cl.sendMessage(kirim, "Tertutup :(")

                        elif PuyText.lower() == 'gsteal 6':
                            gid = cl.getGroup(to)
                            cl.sendMessage(kirim, "「Grup」\nID Group:\n" + gid.id)

### GSTEAL Ended ###
                        elif PuyText.lower().startswith("1cak"):
                            r=requests.get("http://api-1cak.herokuapp.com/random")
                            data=r.text
                            data=json.loads(data)
                            #hasil = "「 1CAK Result 」"
                            hasil = "   Judul : \n" + str(data["title"])
                            hasil += " \n\n  ID : " +str(data["id"])
                            #hasil += "\n  URL : " + str(data["url"])
                            hasil += "\n  Rates : " + str(data["votes"])
                            hasil += "\n  Nsfw : " + str(data["nsfw"])
                            uerel = str(data["url"])
                            #image = str(data["img"])
                            _session = requests.session()
                            imagez = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "lg",
                                                    "weight": "bold",
                                                    "text": "1CAK" #% (elapsed_time),
                                                  },
                                                  {
                                                    "type": "separator",
                                                  }
                                                ]
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "{}".format(hasil),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "md"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Kunjungi",
                                                      "uri": "{}".format(str(uerel))
                                                    },
                                                    "style": "link",
                                                    "height": "md"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif PuyText.lower().startswith("creepypasta"):
                            r=requests.get("http://hipsterjesus.com/api")
                            data=r.text
                            data=json.loads(data)
                            hasil = "     「 Fun 」 \nType: CreepyPasta\n\n"
                            hasil += str(data["text"])
                            cl.sendMessage(kirim, str(hasil))
                            print ("Creepypasta")

                        elif PuyText.lower().startswith("jadwalbola"):
                            r=requests.get("http://rest.farzain.com/api/bola.php?apikey=YAfYs3tyIJJF91Ruc7iw8eW7E")
                            data=r.text
                            data=json.loads(data)
                            hasil = " 「 Jadwal Bola 」 \n\n"
                            hasil += str(data["result"]["tanggal"]["hari"]["event"]["kick"]["match"]["tv"])
                            hasil += str(data["result"]["tanggal"]["hari"]["event"]["kick"]["match"]["tv"])
                            hasil += str(data["result"]["tanggal"]["hari"]["event"]["kick"]["match"]["tv"])
                            cl.sendMessage(kirim, str(hasil))

                        elif PuyText.lower().startswith("randomlose"):
                            group = cl.getGroup(to)
                            try:
                                members = [mem.mid for mem in group.members]
                            except:
                                members = [mem.mid for mem in group.members]
                            message = random.choice(members)
                            cl.mentionWithRFU(kirim, "  「 Fun 」\nType: RandomLose\n• The Loser is : ","") #, [kirim])
                            cl.sendContact(kirim, message)
                            print ("RandomLose")

                        elif PuyText.lower().startswith("alquran:"):
                                try:
                                    sep = PuyText.split(" ")
                                    search = PuyText.lower().replace(sep[0] + " ","")
                                    with requests.session() as web:
                                        r = requests.get("http://api.alquran.cloud/surah/{}/ar.alafasy".format(str(search)))
                                        data = r.text
                                        data = json.loads(data)
                                        no = 0
                                        ret_ = "Quran Surah {}/{}\nSurah Ke-{}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]))
                                        for quran in data["data"]["ayahs"]:
                                            no += 1
                                            ret_ += "\n{}. {}".format(str(no),quran["text"])
                                        cl.sendMessage(kirim, str(ret_))
                                except Exception as error:
                                     pass

                        elif PuyText.lower().startswith("cekrobot "):
                            if msg.toType == 2:
                                url = PuyText.lower().replace("cekrobot ","")
                                urlnya = 'https://robohash.org/'+url+'.png'
                                cl.sendMessage(kirim,"  「 Fun 」\nType: MyRobot\nIni adalah robot kamu,")
                                cl.sendImageWithURL(kirim,urlnya)
                                print ("Robot")
                            else:
                                if wait["lang"] == "JP":
                                    cl.sendMessage(kirim,"Perintah ini hanya bisa di grup")
                                else:
                                    cl.sendMessage(kirim,"Perintah ini hanya bisa di grup")

                        elif PuyText.lower().startswith("friendinfo "):
                            separate = PuyText.split(" ")
                            number = PuyText.lower().replace(separate[0] + " ","")
                            contactlist = cl.getAllContactIds()
                            try:
                                contact = contactlist[int(number)-1]
                                friend = cl.getContact(contact)
                                cu = cl.getProfileCoverURL(contact)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + friend.pictureStatus
                                try:
                                    cl.sendMessage(kirim,"   「 Friend Info 」\n\n" + "Nama : " + friend.displayName + "\nStatus : " + friend.statusMessage + "\nMid : " + friend.mid)
                                    cl.sendImageWithURL(kirim,image)
                                    cl.sendImageWithURL(kirim,path)
                                    cl.sendContact(kirim, friend.mid)
                                except:
                                    pass
                            except Exception as error:
                                cl.sendMessage(kirim, "「 Result Error 」\n" + str(error))

                        elif PuyText.lower().startswith("unfriendall "):
                            try:
                                friend = cl.getContacts(cl.getAllContactIds())
                                cl.sendMessage(kirim,"Menghapus {} Teman".format(len(friend)))
                                for unfriend in friend:
                                    cl.deleteContact(unfriend.mid)
                                cl.sendMessage(kirim,"Berhasil menghapus {} Teman".format(len(friend)))
                            except Exception as error:
                                cl.sendMessage(kirim, "   「 Result Error 」\n" + str(error))

                        elif PuyText in ["Memberlist"]:
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                kontak = cl.getGroup(kirim)
                                group = kontak.members
                                num=1
                                msgs="   「 Daftar Member 」"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\n「Total Member %i」" % len(group)
                                cl.sendText(kirim, msgs)

                        elif PuyText.lower() == 'all respon':
                            contact = cl.getContact(user)
                            txt = ['how are you all?','Hai guys','Puy here','hai semua','selamat beraktivitas']
                            isi = random.choice(txt)
                            #tts = gTTS(text=isi, lang='id', slow=False)
                            #tts.save('temp2.mp3')
                            cl.sendMessage(kirim,"◇ Linda",contentMetadata={"MSG_SENDER_NAME":"Linda","MSG_SENDER_ICON":"http://pbs.twimg.com/profile_images/1001808982615277568/EPVaEr4P_400x400.jpg"})
                            cl.sendMessage(kirim,"◇ Fina",contentMetadata={"MSG_SENDER_NAME":"Fina","MSG_SENDER_ICON":"http://aov.hasagi.gg/wp-content/uploads/2018/06/Sarah-Viloid.jpg"})
                            cl.sendMessage(kirim,"◇ Arin",contentMetadata={"MSG_SENDER_NAME":"Arin","MSG_SENDER_ICON":"https://scontent-lga3-1.cdninstagram.com/vp/4e31f6f9f995df211c10c565507b4830/5BDEFCD3/t51.2885-19/s150x150/26158377_969899119824478_5446520578645164032_n.jpg"})
                            cl.sendMessage(kirim,"◇ Sandra",contentMetadata={"MSG_SENDER_NAME":"Sandra","MSG_SENDER_ICON":"http://asset-a.grid.id/crop/0x0:0x0/700x465/photo/2018/08/08/3351787273.jpg"})
                            cl.sendMessage(kirim,"◇ Risa",contentMetadata={"MSG_SENDER_NAME":"Risa","MSG_SENDER_ICON":"http://cdn2.tstatic.net/pekanbaru/foto/bank/images/sarah-viloid-olivia-gamer_20180806_183745.jpg"})
                            cl.sendMessage(kirim,"◇ Lisa",contentMetadata={"MSG_SENDER_NAME":"Lisa","MSG_SENDER_ICON":"https://i.ytimg.com/vi/kuqy1j6r-Xk/maxresdefault.jpg"})
                            cl.sendMessage(kirim,"◇ Annis",contentMetadata={"MSG_SENDER_NAME":"Annis","MSG_SENDER_ICON":"https://scontent-mrs1-1.cdninstagram.com/vp/bea084c9b99f2c1026af825a8682c881/5C107258/t51.2885-15/e35/36775985_2073120879617880_7681327508842610688_n.jpg"})
                            cl.sendMessage(kirim,"◇ Finkan",contentMetadata={"MSG_SENDER_NAME":"Finkan","MSG_SENDER_ICON":"https://i.pinimg.com/originals/58/e8/d6/58e8d63c8384fbf649ce33196f156904.jpg"})
                            cl.sendMessage(kirim,"◇ Irene",contentMetadata={"MSG_SENDER_NAME":"Irene","MSG_SENDER_ICON":"https://i.ytimg.com/vi/bSQ7yPV-1Ag/mqdefault.jpg"})
                            cl.sendMessage(kirim,"◇ Nadya",contentMetadata={"MSG_SENDER_NAME":"Nadya","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-s7hRHwVUY7c/WcT4qaWOxZI/AAAAAAAADAE/GJa8f584UvcW5fZBGJ12VMRIw1CJ8hX7ACK4BGAYYCw/s400/sarah.jpg"})
                            cl.sendMessage(kirim,"◇ Putri",contentMetadata={"MSG_SENDER_NAME":"Putri","MSG_SENDER_ICON":"https://3.bp.blogspot.com/-lb5rG03TPrg/V47hiQzjmLI/AAAAAAAAAtQ/FxLHG6Sz1jMyz0MXCRvnROTiVN07x8dsgCLcB/s1600/IMG_20160720_091426.jpg"})
                            cl.sendMessage(kirim,"◇ Permata",contentMetadata={"MSG_SENDER_NAME":"Permata","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-Q-xhtNI-bSE/V2ZUo6aQL1I/AAAAAAAAAVk/ENETZiBTIKgP5z9S_iZV1skmiwyF7kPcgCLcB/s1600/Viloid.jpg"})
                            cl.sendMessage(kirim,"◇ Maulida",contentMetadata={"MSG_SENDER_NAME":"Maulida","MSG_SENDER_ICON":"https://scontent-lax3-1.cdninstagram.com/vp/50a708702c5a70e0b48e76685df541fa/5BFEFBD3/t51.2885-15/sh0.08/e35/s640x640/29094007_125595028282088_4752627668053131264_n.jpg"})
                            cl.sendMessage(kirim,"◇ Sabrina",contentMetadata={"MSG_SENDER_NAME":"Sabrina","MSG_SENDER_ICON":"https://s.kaskus.id/images/2017/09/20/6474659_20170920084803.jpg"})
                            cl.sendMessage(kirim,"◇ Syifa",contentMetadata={"MSG_SENDER_NAME":"Syifa","MSG_SENDER_ICON":"https://i.pinimg.com/originals/54/c4/fb/54c4fb5e52a3847eb6959dc3c05d23e4.jpg"})
                            cl.sendMessage(kirim,"◇ Rima",contentMetadata={"MSG_SENDER_NAME":"Rima","MSG_SENDER_ICON":"https://scontent-atl3-1.cdninstagram.com/vp/761c1a85622c69d9f256d56a6de8260b/5BF890CE/t51.2885-15/e35/22280485_1754719227873455_8068433645670498304_n.jpg"})
                            cl.sendMessage(kirim,"◇ Lhefi",contentMetadata={"MSG_SENDER_NAME":"Lhefi","MSG_SENDER_ICON":"https://pbs.twimg.com/profile_images/864425427061792768/EAF1kF5K_400x400.jpg"})
                            cl.sendMessage(kirim,"◇ Indri",contentMetadata={"MSG_SENDER_NAME":"Indri","MSG_SENDER_ICON":"https://scontent-ort2-1.cdninstagram.com/vp/cfbd942f6753cf5a80d0b0ee9d231b1a/5BDCF2EB/t51.2885-15/e35/c0.135.1080.1080/s480x480/36032532_234661703930470_3939402733274005504_n.jpg"})
                            cl.sendMessage(kirim,"◇ Annisa R",contentMetadata={"MSG_SENDER_NAME":"Annisa R","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-c7jQmeoVxh0/WQM8RQ0w2NI/AAAAAAAAA8M/C13jErjBDT00QLQ9eX-wjY1PP-Y8-8eCgCLcB/s640/Sarah%2BViloid.jpg"})
                            cl.sendMessage(kirim,"◇ Mutiara",contentMetadata={"MSG_SENDER_NAME":"Mutiara","MSG_SENDER_ICON":"https://scontent-lga3-1.cdninstagram.com/vp/b0da32ae64d5f1bab8a351e4e4ac069b/5C325DB8/t51.2885-15/sh0.08/e35/c0.135.1080.1080/s640x640/39100754_1839310616147166_1453085189692456960_n.jpg"})
                            #cl.sendMessage(kirim,"◇ {}".format(contact.displayName),contentMetadata={"MSG_SENDER_NAME":"Mutiara","MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/{}"}.format(contact.pictureStatus))
                            #"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            #cl.sendMessage(kirim,"◇ Already Active ◇")
                            #cl.sendMessage(kirim, "◇ {}".format(contact.displayName))
                            #cl.sendMessage(kirim, isi, [user])
                            #cl.sendAudio(kirim, 'temp2.mp3')

                        elif PuyText.lower() == 'def respon':
                            txt = ['how are you all?','Hai guys','Puy here','hai semua','selamat beraktivitas']
                            isi = random.choice(txt)
                            tts = gTTS(text=isi, lang='en', slow=False)
                            tts.save('temp2.mp3')
                            cl.sendMessage(kirim,"◇ Nadya",contentMetadata={"MSG_SENDER_NAME":"Nadya","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-s7hRHwVUY7c/WcT4qaWOxZI/AAAAAAAADAE/GJa8f584UvcW5fZBGJ12VMRIw1CJ8hX7ACK4BGAYYCw/s400/sarah.jpg"})
                            cl.sendMessage(kirim,"◇ Putri",contentMetadata={"MSG_SENDER_NAME":"Putri","MSG_SENDER_ICON":"https://3.bp.blogspot.com/-lb5rG03TPrg/V47hiQzjmLI/AAAAAAAAAtQ/FxLHG6Sz1jMyz0MXCRvnROTiVN07x8dsgCLcB/s1600/IMG_20160720_091426.jpg"})
                            cl.sendMessage(kirim,"◇ PermataE",contentMetadata={"MSG_SENDER_NAME":"Permata","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-Q-xhtNI-bSE/V2ZUo6aQL1I/AAAAAAAAAVk/ENETZiBTIKgP5z9S_iZV1skmiwyF7kPcgCLcB/s1600/Viloid.jpg"})
                            cl.sendMessage(kirim,"◇ Maulida",contentMetadata={"MSG_SENDER_NAME":"Maulida","MSG_SENDER_ICON":"https://scontent-lax3-1.cdninstagram.com/vp/50a708702c5a70e0b48e76685df541fa/5BFEFBD3/t51.2885-15/sh0.08/e35/s640x640/29094007_125595028282088_4752627668053131264_n.jpg"})
                            cl.sendMessage(kirim,"◇ Sabrina",contentMetadata={"MSG_SENDER_NAME":"Sabrina","MSG_SENDER_ICON":"https://s.kaskus.id/images/2017/09/20/6474659_20170920084803.jpg"})
                            cl.sendMessage(kirim,"◇ Syifa",contentMetadata={"MSG_SENDER_NAME":"Syifa","MSG_SENDER_ICON":"https://i.pinimg.com/originals/54/c4/fb/54c4fb5e52a3847eb6959dc3c05d23e4.jpg"})
                            cl.sendMessage(kirim,"◇ Rima",contentMetadata={"MSG_SENDER_NAME":"Rima","MSG_SENDER_ICON":"https://scontent-atl3-1.cdninstagram.com/vp/761c1a85622c69d9f256d56a6de8260b/5BF890CE/t51.2885-15/e35/22280485_1754719227873455_8068433645670498304_n.jpg"})
                            cl.sendMessage(kirim,"◇ Lhefi",contentMetadata={"MSG_SENDER_NAME":"Lhefi","MSG_SENDER_ICON":"https://pbs.twimg.com/profile_images/864425427061792768/EAF1kF5K_400x400.jpg"})
                            #cl.sendMessage(kirim,"◇ DEF Already Active ◇")
                            #cl.sendMessage(kirim, isi)
                            cl.sendAudio(kirim, 'temp2.mp3')

                        elif PuyText.lower() == 'ceksider 1 on':
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = " " + timeNow.strftime('%H:%M:%S') + " "
                                if kirim in PUYWAIT['readPoint']:
                                        try:
                                            del PUYWAIT['readPoint'][kirim]
                                            del PUYWAIT['readMember'][kirim]
                                            del PUYWAIT['readTime'][kirim]
                                        except:
                                            pass
                                        PUYWAIT['readPoint'][kirim] = msg.id
                                        PUYWAIT['readMember'][kirim] = ""
                                        PUYWAIT['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                        PUYWAIT['ROM'][kirim] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(PUYWAIT, fp, sort_keys=True, indent=4)
                                            cl.sendMessage(kirim,"  「 Group 」\nType: Ceksider1\nSekarang diaktifkan.\nKetik /csider untuk melihat titik pembaca.")
                                else:
                                    try:
                                        del read['readPoint'][kirim]
                                        del read['readMember'][kirim]
                                        del read['readTime'][kirim]
                                    except:
                                        pass
                                    PUYWAIT['readPoint'][kirim] = msg.id
                                    PUYWAIT['readMember'][kirim] = ""
                                    PUYWAIT['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                    PUYWAIT['ROM'][kirim] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(PUYWAIT, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(kirim, "  「 Group 」\nType: Ceksider1\n\nKetik /csider untuk melihat Pembaca\nKetik CekUlang untuk mengulang titik Pembaca.") #+ readTime)

                        elif PuyText.lower() == 'ceksider 1 off':
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = " " + timeNow.strftime('%H:%M:%S') + " "
                                if kirim not in PUYWAIT['readPoint']:
                                    cl.sendMessage(kirim,"  「 Group 」\nType: Ceksider1\nSekarang dinonaktifkan.")
                                else:
                                    try:
                                            del PUYWAIT['readPoint'][kirim]
                                            del PUYWAIT['readMember'][kirim]
                                            del PUYWAIT['readTime'][kirim]
                                    except:
                                          pass
                                    cl.sendMessage(kirim, "  「 Group 」\nType: Ceksider1\nMenghapus titik pembaca.") #+ readTime)

                        elif PuyText.lower() == 'cekulang':
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = " " + timeNow.strftime('%H:%M:%S') + " "
                                if kirim in PUYWAIT["readPoint"]:
                                    try:
                                        PUYWAIT["readPoint"][kirim] = True
                                        PUYWAIT["readMember"][kirim] = {}
                                        PUYWAIT["readTime"][kirim] = readTime
                                        PUYWAIT["ROM"][kirim] = {}
                                    except:
                                        pass
                                    cl.sendMessage(kirim, "  「 Group 」\nType: Ceksider1\nMengulang titik pembaca.")# + readTime)
                                else:
                                    cl.sendMessage(kirim, "  「 Group 」\nType: Ceksider1\nBelum diaktifkan\n  'Ceksider 1 on' dahulu.")

                        elif PuyText.lower() == '/csider':
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = " " + timeNow.strftime('%H:%M:%S') + " "
                                if kirim in PUYWAIT['readPoint']:
                                    if PUYWAIT["ROM"][kirim].items() == []:
                                        cl.sendMessage(kirim,"  「 Reader 」:\nNone")
                                    else:
                                        chiya = []
                                        for rom in PUYWAIT["ROM"][kirim].items():
                                            chiya.append(rom[1])
                                        cmem = cl.getContacts(chiya)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '   「 Pembaca 」\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@ARDIAN_GANTENG\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan + zxc #+ "  At: " + readTime
                                    try:
                                        cl.sendMessage(kirim, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cl.sendMessage(kirim,"  「 Group 」\nType: Ceksider1\nBelum diaktifkan\n  'Ceksider 1 on' dahulu.")
                                    print ("Ceksider1 on")

                        elif PuyText.lower() == 'ceksider 2 on':
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                try:
                                    del PuyCctv['Point2'][kirim]
                                    del PuyCctv['Point3'][kirim]
                                    del PuyCctv['Point1'][kirim]
                                except:
                                    pass
                                PuyCctv['Point2'][kirim] = msg.id
                                PuyCctv['Point3'][kirim] = ""
                                PuyCctv['Point1'][kirim]=True
                                cl.sendText(kirim,"  「 Group 」\nType: Ceksider2\n\nMemulai cek pembaca.")
                                print ("Ceksider2 on")

                        elif PuyText.lower() == 'ceksider 2 off':
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                if kirim in PuyCctv['Point2']:
                                    PuyCctv['Point1'][kirim]=False
                                    cl.sendText(kirim, PuyCctv['Point3'][kirim])
                                else:
                                    cl.sendText(kirim, "  「 Group 」\nType: Ceksider2\n\nSekarang dinonaktifkan.")

                        elif PuyText.lower() == 'mentionall':
                            if user in Owner:
                                group = cl.getGroup(kirim)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    cl.mentionWithRFU(kirim, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mentionWithRFU(kirim, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    cl.mentionWithRFU(kirim, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mentionWithRFU(kirim, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mentionWithRFU(kirim, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mentionWithRFU(kirim, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mentionWithRFU(kirim, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mentionWithRFU(kirim, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mentionWithRFU(kirim, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    cl.mentionWithRFU(kirim, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mentionWithRFU(kirim, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mentionWithRFU(kirim, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mentionWithRFU(kirim, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    cl.mentionWithRFU(kirim, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    cl.mentionWithRFU(kirim, nm5)
                                cl.sendText(kirim, "「Mention berhasil」\n  Jumlah Anggota: "+str(jml))
                                print ("mentionall")

                        elif PuyText in ["Welcomsg on"]:
                          if user in PuySekawan or user in PUYWAIT["Admin"]:
                            if user in PuySekawan:
                                PUYWAIT['Welcome'] = True
                                cl.sendText(kirim,"Cek Welcome Already ON")
                        elif PuyText in ["Welcomsg off"]:
                          if user in PuySekawan or user in PUYWAIT["Admin"]:
                            if user in PuySekawan:
                                PUYWAIT['Welcome'] = False
                                cl.sendText(kirim,"Cek Welcome Already Off")

                        elif PuyText.lower().startswith("changewelcome: "):
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                teks = PuyText.split(": ")
                                data = PuyText.replace(teks[0] + ": ","")
                                try:
                                    PUYWAIT["WcText"] = data
                                    cl.sendText(kirim,"Welcome Message Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Error")

                        elif PuyText.lower().startswith("hack "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention['M'] not in lists:
                                        lists.append(mention['M'])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                xz = PuyText.replace(names.split(":")[0]+" ","")
                                #print(xz)
                                cl.sendMessage(kirim,xz, "◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 1","MSG_SENDER_ICON":"http://pbs.twimg.com/profile_images/1001808982615277568/EPVaEr4P_400x400.jpg"})

                        elif PuyText.lower().startswith("say "):
                          if user in Owner:
                            if "MENTION" in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention['M'] not in lists:
                                        lists.append(mention['M'])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                puy = PuyText.split(" ")
                                puy = PuyText.replace(puy[0]+" "," ")
                                puy = puy.split('*')
                                txt = str(puy[0])
                                xz = PuyText.replace(PuyText.split(":")[0]+" "," ")
                                #print(xz)
                                cl.sendMessage(kirim, (txt),contentMetadata={"MSG_SENDER_NAME":"{}".format(contact.displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)})

                        elif PuyText in ["Leave on"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT['Leave'] = True
                                cl.sendText(kirim,"Cek Leave Already ON")
                        elif PuyText in ["Leave off"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT['Leave'] = False
                                cl.sendText(kirim,"Cek Leave Already Off")

                        elif PuyText.lower().startswith("changeleave: "):
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                teks = PuyText.split(": ")
                                data = PuyText.replace(teks[0] + ": ","")
                                try:
                                    PUYWAIT["LvText"] = data
                                    cl.sendText(kirim,"Leave Message Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Error")

                        elif PuyText.lower() == "runtimez":
                            if user in Owner:
                                eltime = time.time() - mulai
                                opn = " "+waktu(eltime)
                                cl.sendText(kirim,"Active in :" + opn)

                        elif PuyText.lower().startswith("broadcast: "):
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                bc = msg.text.replace("Teks: ","")
                                gid = cl.getGroupIdsJoined()
                                owner = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," By","\n" + str(" "+bc+" "))

                        elif PuyText.lower().startswith("contactbc: "):
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                bc = msg.text.replace("Teks: ","")
                                gid = cl.getAllContactIds()
                                owner = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," By","\n" + str(" ("+bc+")"))

                        elif PuyText.lower() == "hapus chat":
                            if user in Owner:
                                try:
                                    cl.removeAllMessages(fast.param2)
                                    ginfo = cl.getGroup(kirim)
                                    #cl.mentionWithPuy(kirim,owner,"Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    cl.sendText(kirim, 'Berhasil menghapus obrolan di').format(str(ginfo.name))
                                except:
                                    pass

                        elif PuyText.lower() == 'mulai ulang bot':
                            if user in PuySekawan:
                                cl.sendText(kirim, 'Memulai ulang...')
                                print ("Restarting............")
                                restart_program()

                        elif PuyText.lower() == 'bot keluar':
                            if user in PuySekawan:
                                #cl.mentionWithRFU(kirim,user,"!Exit","")
                                cl.sendMessage(kirim, 'Bot sudah dinonaktifkan!')
                                print ("BOT OFF")
                                exit(1)

                        elif PuyText.lower().startswith("tolak undangan"):
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    cl.sendMessage(kirim, "Berhasil menolak {} Undangan Grup".format(str(len(ginvited))))
                                else:
                                    cl.sendMessage(kirim, "Tidak ada undangan")

                        elif PuyText.lower().startswith("status"):
                            if user in Owner:
                                try:
                                    hasil = "Status Bot\n"
                                    if PUYWAIT["autoAdd"] == True: hasil += "\nAuto Add ( on )"
                                    else: hasil += "\nAuto Add ( off )"
                                    if PUYWAIT["autoJoin"] == True: hasil += "\nAuto Join ( on )"
                                    else: hasil += "\nAuto Join ( off )"
                                    if PUYWAIT["AutoReject"] == True: hasil += "\nAuto Reject Room ( on )"
                                    else: hasil += "\nAuto Reject Room ( off )"
                                    if PUYWAIT["AutojoinTicket"] == True: hasil += "\nAuto Join Ticket ( on )"
                                    else: hasil += "\nAuto Join Ticket ( off )"
                                    if PUYWAIT["autoRead"] == True: hasil += "\nAuto Read ( on )"
                                    else: hasil += "\nAuto Read ( off )"
                                    if PUYWAIT["AutoRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Mention ( off )"
                                    if PUYWAIT["KickRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Kick Mention ( off )"
                                    if PUYWAIT["Timeline"] == True: hasil += "\nCheck Post Timeline ( on )"
                                    else: hasil += "\nCheck Post ( off )"
                                    hasil += "\n"
                                    cl.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif PuyText in ["Autojoin on"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT['autoJoin'] = True
                                cl.sendText(kirim,"Join Set To On..")
                        elif PuyText in ["Autojoin off"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT['autoJoin'] = False
                                cl.sendText(kirim,"Join Set To Off..")

                        elif PuyText in ["Autoreject on"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT['AutoReject'] = True
                                cl.sendText(msg.to,"Reject Set To On..")
                        elif PuyText in ["Autoreject off"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT['AutoReject'] = False
                                cl.sendText(msg.to,"Reject Set To Off..")

                        elif PuyText in ["Adminadd:on"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT["Adminadd"] = True
                                cl.sendText(kirim,"   「 Admin Notify 」\nSent Contact to Add!")
                        elif PuyText in ["Adminadd:off"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT["Adminadd"] = False
                                cl.sendText(kirim,"   「 Admin Notify 」\nAdding admin is now Off!")

                        elif PuyText in ["Adminrem:on"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT["AdminDel"] = True
                                cl.sendText(kirim,"   「 Admin Notify 」\nSent Contact to Remove!")
                        elif PuyText in ["Adminrem:off"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT["AdminDel"] = False
                                cl.sendText(kirim,"   「 Admin Notify 」\nRemoving admin is now Off!")

                        elif PuyText in ["jointicket on"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT["AutojoinTicket"] = True
                                cl.sendText(kirim,"Join Ticket Set To On")
                        elif PuyText in ["jointicket off"]:
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                PUYWAIT["AutojoinTicket"] = False
                                cl.sendText(kirim,"Join Ticket Set To Off")
                        elif '/ti/g/' in PuyText.lower():
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if PUYWAIT["AutojoinTicket"] == True:
                                        group=cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        cl.sendText(kirim,"Masuk ke %s" % str(group.name))

                        elif PuyText.lower() == 'refreshprofile':
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                try:
                                    cl.sendMessage(kirim, "   「 Refresh Profile 」\nWaiting for 5s!")
                                    time.sleep(5.0)
                                    clProfile.displayName = str(ProfileMe["displayName"])
                                    clProfile.statusMessage = str(ProfileMe["statusMessage"])
                                    clProfile.pictureStatus = str(ProfileMe["pictureStatus"])
                                    cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                    cl.updateProfile(clProfile)
                                    cl.sendMessage(kirim, "   「 Refresh Profile 」\nSuccessfully!")
                                except:
                                    cl.sendMessage(kirim, "Error")

                        elif PuyText.lower().startswith("refresh"):
                            if user in PuySekawan or user in PUYWAIT["Admin"]:
                                try:
                                    cl.sendText(kirim,"   「 Refresh 」\nWaiting for 5s!")
                                    time.sleep(5.0)
                                    PUYWAIT['autoJoin'] = False
                                    PUYWAIT['autoAdd'] = False
                                    PUYWAIT['AutojoinTicket'] = False
                                    PUYWAIT['AutoReject'] = False
                                    PUYWAIT['Upfoto'] = False
                                    PUYWAIT['UpfotoBot'] = False
                                    PUYWAIT['UpfotoGrup'] = False
                                    PUYWAIT['Adminadd'] = False
                                    PUYWAIT['AdminDel'] = False
                                    PUYWAIT['Welcome'] = False
                                    PUYWAIT['Leave'] = False
                                    cl.sendText(kirim,"   「 Refresh 」\nDone Refresh!")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif PuyText.lower().startswith("searchid: "):
                            msgg = PuyText.replace('searchid: ','')
                            conn = cl.findContactsByUserid(msgg)
                            if True:
                                cl.sendText(kirim,"https://line.me/ti/p/~" + msgg)
                                cl.sendMessage(kirim, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                contact = cl.getContact(conn.mid)
                                cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                cover = cl.getProfileCoverURL(conn.mid)
                                cl.sendImageWithURL(kirim, cover)
                                cl.mentionWithRFU(kirim,conn.mid,"Tag User\n","")
#### STEAL PROFILE ####
                        elif PuyText.lower().startswith("psteal 1 "):
                            #if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                                        cl.sendImageWithURL(kirim, str(path))

                        elif PuyText.lower().startswith("psteal 2 "):
                            try:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = cl.getContact(ls)
                                      cl.sendMessage(kirim, "   「 ProfileSteal 」\nStatus Message:\n" + contact.statusMessage)
                            except:
                                 cl.sendMessage(kirim, "Status kosong")

                        elif PuyText.lower().startswith("psteal 3 "):
                            #if msg._from in admin:
                                #if line != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = cl.getProfileCoverURL(ls)
                                            cl.sendImageWithURL(kirim, str(path))
                        elif PuyText.lower().startswith("psteal 4 "):
                            #if msg._from in admin:
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            contact = cl.getContact(target)
                                            path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                                            cl.sendVideoWithURL(kirim, path)
                                        except Exception as e:
                                            pass

                        elif PuyText.lower().startswith("psteal 5 "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = "   「 ProfileSteal 」"
                                for ls in lists:
                                    ret_ += "\nMid:\n{}".format(str(ls))
                                cl.sendMessage(kirim, str(ret_))

                        elif PuyText.lower().startswith("mys 1"):
                            contact = cl.getContact(user)
                            cl.sendMessage(kirim, "  「Mysteal」\nName:{}".format(contact.displayName))

                        elif PuyText.lower().startswith("mys 2"):
                            contact = cl.getContact(user)
                            cl.sendMessage(kirim, "  「Mysteal」\nBio:{}".format(contact.statusMessage))

                        elif PuyText.lower().startswith("mys 3"):
                            contact = cl.getContact(user)
                            cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                        elif PuyText.lower().startswith("mys 4"):
                            contact = cl.getContact(user)
                            cl.sendVideoWithURL(kirim,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                        elif PuyText.lower().startswith("mys 5"):
                            channel = cl.getProfileCoverURL(user)          
                            path = str(channel)
                            cl.sendImageWithURL(kirim, path)
#------------ TEMPLATE ------------#
### Token ###
                        elif PuyText.lower().startswith("tokenlist"):
                          if user in Owner:
                            r = requests.get("https://Puytoken.herokuapp.com/iosipad/Puy")
                            data = r.text
                            data = json.loads(data)
                            contact = cl.getContact(user)
                            h = cl.getContact(user)
                            name = "{}".format(h.displayName)
                            _session = requests.session()
                            to = msg.to
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "template",
                                        "altText": "Puy",
                                        "template": {
                                            "type": "buttons",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "LOGIN",
                                                    "uri": "{}".format(str(data["qr"]))
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "CREATOR",
                                                    "uri": "line://ti/p/~yapuy"
                                                }
                                            ],
                                            "thumbnailImageUrl": "https://media1.tenor.com/images/22dab68a24735564a964e68194d23ffb/tenor.gif",
                                            "title": "Iosipad",
                                            "text": "Link will burn in 2 minutes"
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif PuyText.lower().startswith("tokenlistz"):
                            r = requests.get("https://Puytoken.herokuapp.com/iosipad/chromeos")
                            data = r.text
                            data = json.loads(data)
                            contact = cl.getContact(user)
                            h = cl.getContact(user)
                            name = "{}".format(h.displayName)
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "lg",
                                                    "weight": "bold",
                                                    "text": "TOKENLIST"
                                                  }
                                                ]
                                              },
                                              "hero": {
                                                "type": "image",
                                                "url": "https://herencia.net/wp-content/uploads/2017/05/Que_estudiar.jpg",
                                                "size": "full",
                                                "aspectRatio": "20:13"
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    #"weight": "bold",
                                                    "text": "Link will burn in 2 minutes",
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "CHROME",
                                                      "uri": "{}".format(str(data["qr"])),#"{}".format(str(data["qr"]))
                                                    },
                                                    "style": "link",
                                                    "height": "sm"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

### Token Ended ###
### Speed ###
                        elif PuyText.lower().startswith("speed"):
                            no = time.time()
                            cl.sendText("uac8e3eaf1eb2a55770bf10c3b2357c33", ' ')
                            elapsed_time = time.time() - no
                            cl.sendMessage(kirim, "%s" % (elapsed_time))
### Speed Ended ###
                        elif PuyText.lower().startswith("lolz"):
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "text", # ①
                                        "text": "Select your favorite food category or send me your location!",
                                        "quickReply": { # ②
                                          "items": [
                                            {
                                              "type": "action", # ③
                                              "imageUrl": "https://example.com/sushi.png",
                                              "action": {
                                                "type": "message",
                                                "label": "Sushi",
                                                "text": "Sushi"
                                              }
                                            },
                                            {
                                              "type": "action",
                                              "imageUrl": "https://example.com/tempura.png",
                                              "action": {
                                               "type": "message",
                                               "label": "Tempura",
                                               "text": "Tempura"
                                              }
                                            },
                                            {
                                              "type": "action", # ④
                                              "action": {
                                                "type": "location",
                                                "label": "Send location"
                                              }
                                            }
                                          ]
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Wikipedia ###
                        elif PuyText.lower().startswith("wikipedia: "):
                            wiki = PuyText.lower().replace("wikipedia: ","")
                            wikipedia.set_lang("id")
                            pesan=" 『 "
                            pesan+=wikipedia.page(wiki).title
                            pesan+=" 』\n"
                            pesan+=wikipedia.summary(wiki, sentences=1)
                            pesan+="\n"
                            pesanz="Tap tombol dibawah untuk mengunjungi situs tersebut."
                            pesanz+=" "
                            pesann=""
                            pesann+=wikipedia.page(wiki).url
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "text": "WIKIPEDIA" #% (elapsed_time),
                                                  },
                                                  {
                                                    "type": "separator",
                                                  }
                                                ]
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "{}".format(str(pesan)),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                 },
                                                 {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "{}".format(str(pesanz)),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Visit here",
                                                      "uri": "{}".format(str(pesann)),
                                                    },
                                                    "style": "link",
                                                    "height": "sm"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Wikipedia Ended ###
                        elif PuyText.lower().startswith("imagehdz "):
                            query = PuyText.replace("imagehdz ","")
                            cond = PuyText.split("|")
                            search = str(cond[0])
                            result = requests.get("https://api.eater.tech/wallp/{}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            _session = requests.session()
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            if data["result"] != []:
                                ret_ = []
                                for fn in data["result"]:
                                    if 'http://' in fn["link"]:
                                        pass
                                    else:
                                        if len(ret_) >= 20:
                                            pass
                                        else:
                                            ret_.append({
                                                "imageUrl": "{}".format(str(fn["link"])),
                                                "action": {
                                                    "type": "uri",
                                                    "label": "View detail",
                                                    "uri": "{}".format(str(fn["link"]))
                                                    }
                                                }
                                            )
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                        "to": to,
                                        "messages": [{
                                            "type": "template",
                                            "altText": " Puy",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }]
                                    }
                                    data = json.dumps(data)
                                    sendPost = _session.post(url, data=data, headers=headers)
### SC ###
                        elif PuyText.lower().startswith('instainfo2'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://syadnysyz2.herokuapp.com/api/instagram/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Search User Instagram\n"
                                a+="\nName : "+str(data["graphql"]["user"]["full_name"])
                                a+="\nUsername : "+str(data["graphql"]["user"]["username"])
                                a+="\nBio : "+str(data["graphql"]["user"]["biography"])
                                a+="\nUser Blocked : "+str(data["graphql"]["user"]["blocked_by_viewer"])
                                a+="\nURL : "+str(data["graphql"]["user"]["external_url"])
                                a+="\nURL link : "+str(data["graphql"]["user"]["external_url_linkshimmed"])
                                a+="\nFollowers : "+str(data["graphql"]["user"]["edge_followed_by"]["count"])
                                a+="\nFollowing View : "+str(data["graphql"]["user"]["followed_by_viewer"])
                                a+="\nFollowed : "+str(data["graphql"]["user"]["edge_follow"]["count"])
                                a+="\nFollower View : "+str(data["graphql"]["user"]["follows_viewer"])
                                a+="\nChannel  : "+str(data["graphql"]["user"]["has_channel"])
                                a+="\nBlocked Viewer : "+str(data["graphql"]["user"]["has_blocked_viewer"])
                                a+="\nReal Account : "+str(data["graphql"]["user"]["highlight_reel_count"])
                                a+="\nRequest Viewer : "+str(data["graphql"]["user"]["has_requested_viewer"])
                                a+="\nId : "+str(data["graphql"]["user"]["id"])
                                a+="\nBussines Account : "+str(data["graphql"]["user"]["is_business_account"])
                                a+="\nPrivate Account : "+str(data["graphql"]["user"]["is_private"])
                                a+="\nVerified : "+str(data["graphql"]["user"]["is_verified"])
                                a+="\nFollow Real Account : "+str(data["graphql"]["user"]["edge_mutual_followed_by"]["count"])
                                a+="\nPicture url : "+str(data["graphql"]["user"]["profile_pic_url"])
                                a+="\nPicture url HD : "+str(data["graphql"]["user"]["profile_pic_url_hd"])
                                a+="\nConnected Facebook : "+str(data["graphql"]["user"]["connected_fb_page"])
                                a+="\nRequested View : "+str(data["graphql"]["user"]["requested_by_viewer"])                                
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('artinama1'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://syadnysyz2.herokuapp.com/api/ramalan-nama?nama=/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Ramalan Nama\n"
                                a+="\nRomantis : "+str(data["result"]["romantis"])
                                a+="\nMesum : "+str(data["result"]["mesum"])
                                a+="\nMiris : "+str(data["result"]["miris"])
                                a+="\nTulus : "+str(data["result"]["tulus"])
                                a+="\nLoyal : "+str(data["result"]["loyal"])
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('artinama2'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://syadnysyz2.herokuapp.com/api/ramalan-primbon/artinama?nama=/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Arti Nama\n"
                                a+="\nRomantis : "+str(data["arti"])
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith("quotes"):
                            r=requests.get("https://talaikis.com/api/quotes/random")
                            data=r.text
                            data=json.loads(data)
                            hasil = " 「 Fun 」\nType: Random Quotes\n\n"
                            hasil += "Jenis : " +str(data["cat"])
                            hasil += "\n\n" +str(data["quote"])
                            hasil += "\n\nDari : " +str(data["author"])+ " "
                            cl.sendMessage(kirim, str(hasil))

                        elif PuyText.lower().startswith('wallhd'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://api.eater.pw/wallp/{}".format(search))
                                data = r.json()
                                #data = r.text
                                hasil = " 「 Fun 」\nType: Wallpaper HD\n"
                                #hasil += data["result"]
                                hasil += "Judul : " +str(data["result"]["judul"])
                                hasil += "Link : " +str(data["result"]["link"])
                                cl.sendMessage(kirim,hasil)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('kbbi'):
                            try:
                                sep = PuyText.split(" ")
                                kata = PuyText.replace(sep[0] + " ","")
                                r = requests.get("https://farzain.com/api/kbbi.php?id={}&apikey=YAfYs3tyIJJF91Ruc7iw8eW7E".format(urllib.parse.quote(kata)))
                                data = r.text
                                ret_ = "Kata : " + str(kata) + "\nDefinisi : "
                                ret_ += "\n" + str(data)
                                cl.sendMessage(kirim, str(ret_))
                            except Exception as e:
                                cl.sendMessage(kirim, "error\n" + str(e))

                        elif PuyText.lower().startswith('linesticker'):
                            try:
                                sep = PuyText.split(" ")
                                kata = PuyText.replace(sep[0] + " ","")
                                r = requests.get("https://rest.farzain.com/api/stickerline.php?q={}&apikey=YAfYs3tyIJJF91Ruc7iw8eW7E".format(kata))
                                data = r.text
                                b = data["result"]
                                c += str(b["result"]["id"])
                                d += str(b["result"]["title"])
                                e += str(b["result"]["url"])
                                f += str(b["result"]["description"])
                                g += str(b["result"]["type"])
                                h += str(b["result"]["authorName"])
                                hasil = "Informasi Sticker\n "
                                hasil = "Nama: "+str(d)
                                hasil = "StID: "+str(c)
                                hasil = "Tipe: "+str(g)
                                hasil = "Deskripsi: "+str(f)
                                hasil = "Pembuat: "+str(h)
                                hasil = "Url: "+str(e)
                                cl.sendMessage(kirim, hasil)
                            except Exception as error:
                                cl.sendMessage(kirim, "error\n" + str(error))

                        elif PuyText.lower().startswith("animstream"):
                            try:
                                proses = PuyText.split(" ")
                                urutan = PuyText.replace(proses[0] + " ","")
                                count = urutan.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.farzain.com/animestream.php?apikey=YAfYs3tyIJJF91Ruc7iw8eW7E&type=search&q={}".format(search))
                                data = r.text
                                data = json.loads(data)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "Anime Streaming From www.riie.net\n"
                                    for aa in data["result"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". " + str(aa["title"])
                                        ret_ = "\n\nAnimstream {} | number\nUntuk Melihat Link Dan Episodenya".format(str(search))
                                    cl.sendMessage(kirim,hasil+ret_)
                                elif len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        b = data["result"][num - 1]
                                        c = str(b["title"])
                                        d = str(b["url"])
                                        e = str(b["img"])
                                        f = str(b["genre"])
                                        g = str(b["desc"])
                                        hasil = "Informasi Streaming\n "
                                        hasil = "Judul: "+str(c)
                                        hasil += "\nLink Anime : "+str(d)
                                        hasil += "\nLink Gambar : "+str(e)
                                        hasil += "\nGenre : "+str(f)
                                        hasil += "\nDeskripsi : "+str(g)
                                        cl.sendMessage(kirim,hasil)
                                    except Exception as e:
                                        cl.sendMessage(kirim," "+str(e))
                            except Exception as error:
                                cl.sendMessage(kirim, "error\n" + str(error))

                        elif PuyText.lower().startswith("cari"):
                            sep = PuyText.split(" ")
                            search = PuyText.replace(sep[0] + " ","")
                            url = "http://lmgtfy.com/?q={}".format(urllib.parse.quote(search))
                            try:
                                r = requests.get("http://tinyurl.com/api-create.php?url={}".format(url))
                                hasil = r.text
                                cl.sendMessage(kirim, " 「 Fun 」\nType: Search\n\n" + hasil)
                            except Exception as error:
                                cl.sendMessage(kirim, "error\n" + str(error))

                        elif PuyText.lower().startswith("drakor2"):
                            try:
                                proses = PuyText.split(" ")
                                urutan = PuyText.replace(proses[0] + " ","")
                                count = urutan.split("|")
                                search = str(count[0])
                                r = requests.get("https://api.eater.pw/drakor/{}".format(search))
                                data = r.text
                                data = json.loads(data)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "  「 Fun 」\nType: Drama Korea\n"
                                    for aa in data["result"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". " + str(aa["judul"])
                                        ret_ = "\n\nketik Drakor2 {} | nomor\nUntuk Lanjut".format(str(search))
                                    cl.sendMessage(kirim,hasil+ret_)
                                elif len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        b = data["result"][num - 1]
                                        c = str(b["judul"])
                                        d = str(b["link"])
                                        hasil = "Informasi Drama Korea\n "
                                        hasil = "Judul: "+str(c)
                                        hasil += "\nLink : "+str(d)
                                        cl.sendMessage(kirim,hasil)
                                    except Exception as e:
                                        cl.sendMessage(kirim," "+str(e))
                            except Exception as error:
                                cl.sendMessage(kirim, "error\n" + str(error))
                                #logError(error)

                        elif PuyText.lower().startswith("lockscreen "):
                            #if msg._from in Owner:
                            query = PuyText.replace("lockscreen ","")
                            cond = PuyText.split("*")
                            search = str(cond[0])
                            result = requests.get("http://api.eater.pw/wallp/{}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = "[ Lockscreen Search ]\n"
                                for sam in data["result"]:
                                    num += 1
                                    ret_ += "\n{}. {}".format(str(num),str(sam["judul"]))
                                ret_ += "\n\nUntuk Lanjut ketik lockscreen {}*(nomor)".format(str(search))
                                cl.sendMessage(kirim, str(ret_))
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["result"]):
                                    sam = data["result"][num - 1]
                                    result = requests.get("http://api.eater.pw/wallp/{}".format(str(search)))
                                    data = result.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        cl.sendImageWithURL(kirim, str(sam["link"]))

                        elif PuyText.lower().startswith('drakor'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://api.eater.pw/drakor/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Drama Korea\n"
                                a+="\n "+str(data["result"])
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('cooltext'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                #r = requests.get("http://api.eater.pw/drakor/{}".format(search))
                                #data = r.json()
                                #a=" 「 Fun 」\nType: Drama Korea\n"
                                #a+="\n "+str(data["result"])
                                cl.sendImageWithURL(to, "http://rest.farzain.com/api/cooltext.php?text={}&apikey=YAfYs3tyIJJF91Ruc7iw8eW7E".format(search))
                                #cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('animequote'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("https://rest.farzain.com/api/animequotes.php?apikey=YAfYs3tyIJJF91Ruc7iw8eW7E/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Drama Korea\n"
                                a+="\n "+str(data["result"]["quote"]["anime"]["author"])
                                #cl.sendImageWithURL(kirim,a)
                                cl.sendMessage(kirim,a)
                                #cl.sendImageWithURL(kirim, "https://rest.farzain.com/api/cooltext.php?text={}&apikey=YAfYs3tyIJJF91Ruc7iw8eW7E".format(search))
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('redtube'):
                            try:
                                #sep = PuyText.split(" ")
                                #search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://api.eater.pw/redtube/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: RedTube\n"
                                a+="\n "+str(data["result"])
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('mangalist'):
                            try:
                                #sep = PuyText.split(" ")
                                #search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://api.eater.pw/manga/list/") #.format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Manga List\n"
                                a+="\n "+str(data["result"])
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('danbooru'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://api.eater.pw/danbooru/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Danbooru\n"
                                a+="\n "+str(data["result"]["img"]["info"])
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('genz'):
                            try:
                                #sep = PuyText.split(" ")
                                #search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("https://v1.mazterin.com/auto_generate_link.php")#.format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Xvideos\n"
                                a+="\n "+str(data["url"]["reason"])
                                cl.sendMessage(kirim,a)
                                #cl.sendImageWithURL(kirim, "http://api.eater.pw/cctv/") #.format(search))
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith("motivasi"):
                            puy1 = requests.get("https://talaikis.com/api/quotes/random")
                            data=puy1.text
                            data=json.loads(data)
                            cl.sendMessage(kirim, " 「 Fun 」\nType: Motivasi\n\n" + str(data["quote"]))

                        elif PuyText.lower().startswith("berita hangat"):
                            mpui = requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                            data = mpui.text
                            data = json.loads(data)
                            hasil = "  「 Fun 」\nType: Berita Hangat\n\n"
                            hasil += "1). \n「" + str(data["articles"][0]["title"] + "」")
                            hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                            hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                            hasil += "\n     Link : " + str(data["articles"][0]["url"])
                            hasil += "\n\n2). \n「" + str(data["articles"][0]["title"] + "」")
                            hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                            hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                            hasil += "\n     Link : " + str(data["articles"][1]["url"])
                            hasil += "\n\n3). \n「" + str(data["articles"][0]["title"] + "」")
                            hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                            hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                            hasil += "\n     Link : " + str(data["articles"][2]["url"])
                            path = data["articles"][3]["urlToImage"]
                            cl.sendMessage(kirim, str(hasil))
                            cl.sendImageWithURL(kirim, str(path))

                        elif PuyText.lower().startswith("getimage "):
                            try:
                                query = PuyText.replace("getimage ","")
                                #search = cmd.replace("client image ","")
                                r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(query))
                                data = r.text
                                data = json.loads(data)
                                if data["content"] != []:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    #cl.sendMessage(kirim, " Search Image 「 " + query + " 」  ")
                                    cl.sendImageWithURL(kirim, str(path))
                            except Exception as e:
                                 #logError(error)
                                 #var= traceback.print_tb(error.__traceback__)
                                 cl.sendMessage(kirim,str(e))

                        elif PuyText.lower().startswith("carigambar"):
                            try:
                                separate = PuyText.split(" ")
                                search = PuyText.replace(separate[0] + " ","")
                                r = requests.get("http://api.eater.pw/googleimg/{}".format(search))
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    items = data["result"]["img"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendImageWithURL(kirim, str(path))
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('animelist'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://api.eater.pw/anime/list/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Anime List\n"
                                a+="\n "+str(data["result"]["judul"]["sinop"]["link"])
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

                        elif PuyText.lower().startswith('jodohin'):
                            try:
                                sep = PuyText.split(" ")
                                search = PuyText.replace(sep[0] + " ","")
                                r = requests.get("http://syadnysyz2.herokuapp.com/api/love-calculator?nama1=&nama2=/{}".format(search))
                                data = r.json()
                                a=" 「 Fun 」\nType: Love percentage\n"
                                a+="\nSi : "+str(data["fname"])
                                a+="\nTersangka : "+str(data["sname"])
                                a+="\nPersen : "+str(data["percentage"])
                                a+="\nKeterangan : "+str(data["result"])
                                cl.sendMessage(kirim,a)
                            except Exception as e:
                                cl.sendMessage(kirim, str(e))

### SC ###

                        elif PuyText.lower().startswith("instainfo1: "):
                            sep = PuyText.split(" ")
                            instagram = PuyText.replace(sep[0] + " ","")
                            html = requests.get('https://www.instagram.com/' + instagram + '/')
                            soup = BeautifulSoup(html.text, 'html.parser')
                            data = soup.find_all('meta', attrs={'property':'og:description'})
                            text = data[0].get('content').split()
                            data1 = soup.find_all('meta', attrs={'property':'og:image'})
                            text1 = data1[0].get('content').split()
                            #tj = text1[0].replace("s150x150/","")
                            user = "Name: " + text[-2] + "\n"
                            user1 = "Username: " + text[-1] + "\n"
                            followers = "Followers: " + text[0] + "\n"
                            following = "Following: " + text[2] + "\n"
                            post = "Post: " + text[4] + "\n"
                            #link = "https://www.instagram.com/" + instagram
                            detail = " 「 Account Info 」\n\n"
                            details = "\n</>"
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "text": "INSTAGRAM INFO", #% (elapsed_time),
                                                  },
                                                  {
                                                    "type": "separator",
                                                  }
                                                ]
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "{}".format(str(detail + user + user1 + followers + following + post + details)),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Add",
                                                      "uri": "https://line.me/ti/p/~yapuy", #.format(str(link)),
                                                    },
                                                    "style": "link",
                                                    "height": "sm"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### INSTAGRAM Ended ###
                        elif PuyText.lower().startswith("write "):
                            bcd = PuyText.lower().replace("write ","")
                            #bcd = PuyText.upper().replace("write ","")
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "{}".format(str(bcd)),
                                                        "size": "sm",
                                                        "weight": "regular",
                                                        "align": "start",
                                                        "gravity": "top",
                                                        "color": "#E261FF",
                                                        "wrap": True,
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Runtime ###
                        elif PuyText.lower().startswith("runtime"):
                          if user in Owner:
                            eltime = time.time() - mulai
                            opn = " "+waktu(eltime)
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "   「 Runtime 」\n", #% (elapsed_time),
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#000000",
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "{}".format(str(opn)),
                                                        "size": "md",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#0000ff",
                                                        "wrap": True
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Runtime Ended ###
### About ###
                        elif PuyText.lower() == "about":
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "lg",
                                                    "weight": "bold",
                                                    "text": "ABOUT"
                                                  },
                                                  {
                                                    "type": "separator",
                                                  }
                                                ]
                                              },
                                              #"hero": {
                                              #  "type": "image",
                                              #  "url": "https://media1.tenor.com/images/4648a40f88dd6c80e1304ba200f210dc/tenor.gif",
                                              #  "size": "full",
                                              #  "aspectMode": "cover",
                                              #  "aspectRatio": "20:13" #20:13
                                              #},
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "text": "PUY'Z",
                                                    "color": "#186A3B",
                                                    "wrap": True
                                                  },
                                                  {
                                                    "type": "separator"
                                                  },
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "weight": "regular",
                                                    "color": "#000000",
                                                    "text": "Dipersembahkan oleh :",
                                                    "wrap": True
                                                  },
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "color": "#aaaaaa",
                                                    "size": "sm",
                                                    "text": "- Icad\n- Agee\n- Ical\n- Iyan\n- Ryn\n- Zubair\n- Ree\n- Nazri\n- Fian",
                                                    "wrap": True
                                                  },
                                                  {
                                                    "type": "separator",
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Support Us",
                                                      "uri": "http://line.me/ti/p/%40wiz0278g"
                                                    },
                                                    "style": "link",
                                                    "height": "sm"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif PuyText.lower().startswith("deviantart "):
                            query = PuyText.lower().replace("deviantart ","")
                            try:
                                search = PuyText.lower().replace("deviantart ","")
                                r = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                data = r.text
                                data = json.loads(data)
                                if data["content"] != []:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    #cl.sendMessage(kirim, "Mencari gambar " + query + " ")
                                _session = requests.session()
                                image = "https://cdn.icon-icons.com/icons2/1294/PNG/512/2362135-instagram-photo-round-social_85523.png"
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                headers = {
                                    "Host": "game.linefriends.com",
                                    "Content-Type": "application/json",
                                    "User-Agent": "Mozilla/5.0",
                                    "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                                }
                                data = {
                                    "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                    "to": to,
                                    "messages": [
                                        {
                                                "type": "template",
                                                "altText": "Imagez",
                                                "template": {
                                                    "type": "image_carousel",
                                                    "columns": [
                                                        {
                                                            "imageUrl": "{}".format(path),
                                                            "action": {
                                                                "type": "uri",
                                                                "label": "Sentuh",
                                                                "uri": "line://shop/detail/2000006" #.format(path)
                                                            }
                                                        },
                                                        {
                                                            "imageUrl": image,
                                                            "action": {
                                                                "type": "uri", #"uri",
                                                                "label": "Kunjungi",
                                                                "uri": "https://instagram.com/muh.khadaffy"
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                    ]
                                }
                                data = json.dumps(data)
                                sendPost = _session.post(url, data=data, headers=headers)
                            except Exception as error:
                                cl.sendMessage(kirim, str(error))

                        elif PuyText.lower().startswith("help"):
                            _session = requests.session()
                            image = "https://cdn.icon-icons.com/icons2/1294/PNG/512/2362135-instagram-photo-round-social_85523.png"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                            "type": "template",
                                            "altText": "Puy",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": [
                                                    {
                                                        "imageUrl": "https://cdn.pixabay.com/photo/2017/03/30/20/22/black-2189644_960_720.png",
                                                        "action": {
                                                            "type": "uri", #"uri",
                                                            "label": "Commands",
                                                            "uri": "line://msg/text/@cmd"
                                                        }
                                                    },
                                                    {
                                                        "imageUrl": "https://cdn.pixabay.com/photo/2017/03/30/20/22/black-2189644_960_720.png",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Fun",
                                                            "uri": "line://msg/text/@fun" #.format(path)
                                                        }
                                                    },
                                                    {
                                                        "imageUrl": "https://i.pinimg.com/originals/cc/43/df/cc43df045deaf2170a8a8d884d16b62c.png",
                                                        "action": {
                                                            "type": "uri", #"uri",
                                                            "label": "Tentang",
                                                            "uri": "line://msg/text/about"
                                                        }
                                                    },
                                                    {
                                                        "imageUrl": "https://cdn0.iconfinder.com/data/icons/emotions-line/2048/1656_-_Bye-512.png",
                                                        "action": {
                                                            "type": "uri", #"uri",
                                                            "label": "Keluarkan",
                                                            "uri": "line://msg/text/@bye"
                                                        }
                                                    }
                                                ]
                                            }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
                            #except Exception as error:
                            #    cl.sendMessage(kirim, str(error))

                        elif PuyText.lower().startswith("imageart "):
                            try:                                   
                                search = PuyText.lower().replace("imageart ","")
                                puy1 = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                data = puy1.text
                                data = json.loads(data)
                                if data["content"] != []:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(kirim,"Image in #%s From #%s." %(str(a),str(b)))
                                    cl.sendImageWithURL(kirim, str(path))
                                    log.info("Art #%s from #%s." %(str(a),str(b)))
                            except Exception as error:
                                cl.sendMessage(kirim, str(error))
### About Ended ###
### IMAGETEST ###
                        elif PuyText.lower().startswith("@tokenlist"):
                          if user in Owner:
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                "contents": [
                                                  {
                                                    "type": "image",
                                                    "url": "https://media1.tenor.com/images/8a5b50b68118f35027da5dd8dbc0840d/tenor.gif",
                                                    "size": "md",
                                                    "aspectMode": "cover",
                                                    "align": "start"
                                                    #"aspectRatio": "4:3" #20:13
                                                  },
                                                  {
                                                    "type": "image",
                                                    "url": "https://media.tenor.com/images/d4a0ef6f496d3a1547218fb858d8896e/tenor.gif",
                                                    "size": "lg",
                                                    "aspectMode": "cover",
                                                    "align": "center"
                                                    #"aspectRatio": "4:3" #20:13
                                                  },
                                                  {
                                                    "type": "image",
                                                    "url": "https://media.tenor.com/images/267e955f9e03519022ca28ec2010be6b/tenor.gif",
                                                    "size": "md",
                                                    "aspectMode": "cover",
                                                    "align": "start"
                                                    #"aspectRatio": "4:3" #20:13
                                                  }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Calendar ###
                        elif PuyText.lower().startswith("calendar"):
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                            bulan = ["January", "February", "March", "April", "May", "June", "Juli", "August", "September", "October", "November", "December"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + "." + bln + "." + timeNow.strftime('%Y') + "\nWib : " + timeNow.strftime('%H:%M:%S') + " "
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "lg",
                                                    "weight": "bold",
                                                    "text": "CALENDAR", #% (elapsed_time),
                                                  },
                                                  {
                                                      "type": "separator"
                                                  },
                                                ]
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "text": "{}".format(readTime),
                                                    #"margin": "sm",
                                                    "wrap": True
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "md"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Creator",
                                                      "uri": "http://line.me/ti/p/~yapuy"
                                                    },
                                                    "style": "primary",
                                                    "height": "md"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Calendar Ended ###
### Myinfo ###
                        elif PuyText.lower() == "me":
                            contact = cl.getContact(user)
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "start",
                                                    "color": "#000000",
                                                    "size": "lg",
                                                    #"spacing": "sm",
                                                    "weight": "bold",
                                                    "text": "PROFILE"
                                                  },
                                                  {
                                                      "type": "separator"
                                                  }
                                                ]
                                              },
                                              "hero": {
                                                "type": "image",
                                                "url": "https://syadnysyz2.herokuapp.com/storage/img?url=http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus),
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "4:3" #20:13
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "color": "#186A3B",
                                                    "text": "{}".format(contact.displayName)
                                                    #"flex": 3
                                                  },
                                                  {
                                                    "type": "text",
                                                    "weight": "regular",
                                                    "color": "#aaaaaa",
                                                    "align": "center",
                                                    "text": "{}".format(contact.statusMessage),
                                                    "wrap": True
                                                    #"flex": 5
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                #"separator": True,
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "sm"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Set Profile",
                                                      "uri": "line://nv/profile"
                                                    },
                                                    "style": "link",
                                                    "height": "sm"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
                            
                        elif PuyText.lower().startswith("@deviantart "):
                            query = PuyText.lower().replace("@deviantart ","")
                            try:
                                search = PuyText.lower().replace("@deviantart ","")
                                r = requests.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(search))
                                data = r.text
                                data = json.loads(data)
                                if data["content"] != []:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(kirim, "Mencari gambar " + query + " ")
                                _session = requests.session()
                                image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                headers = {
                                    "Host": "game.linefriends.com",
                                    "Content-Type": "application/json",
                                    "User-Agent": "Mozilla/5.0",
                                    "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                                }
                                data = {
                                    "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                    "to": to,
                                    "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "Puy",
                                            "contents": {
                                                "type": "bubble",
                                                "header": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                      {
                                                        "type": "text",
                                                        "align": "start",
                                                        "color": "#000000",
                                                        "size": "md",
                                                        #"spacing": "sm",
                                                        "weight": "bold",
                                                        "text": "PROFILE"
                                                      }
                                                    ]
                                                  },
                                                  "hero": {
                                                    "type": "image",
                                                    "url": "{}".format(path),
                                                    "size": "full",
                                                    "aspectMode": "cover",
                                                    "aspectRatio": "4:3" #20:13
                                                  },
                                                  "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "contents": [
                                                      {
                                                        "type": "text",
                                                        "align": "center",
                                                        "weight": "regular",
                                                        "color": "#186A3B",
                                                        "text": "T" #.format(contact.displayName)
                                                        #"flex": 3
                                                      },
                                                      {
                                                        "type": "text",
                                                        "weight": "regular",
                                                        "color": "#aaaaaa",
                                                        "align": "center",
                                                        "text": "T", #.format(contact.statusMessage),
                                                        "wrap": True
                                                        #"flex": 5
                                                      }
                                                    ]
                                                  },
                                                  "footer": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    #"separator": True,
                                                    "contents": [
                                                      {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                      },
                                                      {
                                                        "type": "button",
                                                        "action": {
                                                          "type": "uri",
                                                          "label": "Set Profile",
                                                          "uri": "line://nv/profile"
                                                        },
                                                        "style": "link",
                                                        "height": "sm"
                                                        #"color": "#000000"
                                                      }
                                                    ]
                                                  }
                                            }
                                        }
                                    ]
                                }
                                data = json.dumps(data)
                                sendPost = _session.post(url, data=data, headers=headers)
                            except Exception as error:
                                cl.sendMessage(kirim, str(error))
### Myinfo Ended ###
### Getname ###
                        elif PuyText.lower().startswith("myname"):
                            contact = cl.getContact(user)
                            _session = requests.session()
                            image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
                            url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                            headers = {
                                "Host": "game.linefriends.com",
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0",
                                "Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
                            }
                            data = {
                                "cc": "UXfpO//D+K6TlqsIBX4AhlamXjhsCUtI1/lWa0zxvp3YA3BlQFwCS8cEKWXBtSJO2cwDtNmbXRA6QPIDBiHbvDOODNoaDQgv6Vno900RzrJ+orAi+vCx9BymUUoebOT3RRtTaJHTYL3AiHLB1MlUdOJvGf7QqPih3p1WUxvWG1v+Tol4W/zAEFdXld5bYneQI3YAZjUn8Ejekfh3qwEHu30f9IayoJs1IwU5C45QMS8Qfu73cln4qH90pgOiQ2Yq15ZJ68/0/Amwy46C5ugyoqookxI4/Oh+Iu+tjT0VtP2Fv5/YoNCKOwbrsw2jHAvL8ACR1qVJj2NesAHkB7fDzC6Ncb0mbxQ5/r1P8oQ1Gbk",
                                "to": to,
                                "messages": [
                                    {
                                        "type": "flex",
                                        "altText": "Puy",
                                        "contents": {
                                            "type": "bubble",
                                            "header": {
                                                "type": "box",
                                                #"align": "center",
                                                #"color": "#0000ff",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "text": "   「 Getname 」\n", #% (elapsed_time),
                                                    "flex": 1
                                                  }
                                                ]
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    #"align": "center",
                                                    "color": "#aaaaaa",
                                                    "size": "sm",
                                                    "weight": "regular",
                                                    "text": "HH", #.format(contact.displayName),
                                                    "flex": 1
                                                  },
                                                  {
                                                    "type": "text",
                                                    "text": "Monday 25, 9:00PM",
                                                    "wrap": True,
                                                    "size": "md",
                                                    "color": "#666666",
                                                    "flex": 4
                                                  }
                                                ]
                                              },
                                              "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "spacer",
                                                    "size": "xl"
                                                  },
                                                  {
                                                    "type": "button",
                                                    "action": {
                                                      "type": "uri",
                                                      "label": "Creator",
                                                      "uri": "http://line.me/ti/p/~yapuy"
                                                    },
                                                    "style": "primary"
                                                    #"color": "#000000"
                                                  }
                                                ]
                                              }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Getname Ended ###
#------------ TEMPLATE ENDED ------------#
#------------ SCRIPT PUY -----------#
                        elif 'Tokenlist' in msg.text:
                           if user in Owner:
                              cl.sendText(kirim,"1\n"+cl.authToken)
                              #cl.sendText(kirim,"2\n"+RIDEN1.authToken)
                              #cl.sendText(kirim,"3\n"+RIDEN2.authToken)
                              #cl.sendText(kirim,"4\n"+RIDEN3.authToken)
                              #cl.sendText(kirim,"5\n"+RIDEN4.authToken)
                              #cl.sendText(kirim,"6\n"+RIDEN5.authToken)
                              #cl.sendText(kirim,"7\n"+RIDEN6.authToken)
#------------ SCRIPT PUY ENDED -----------#

                        elif PuyText.lower().startswith("apakah: "):
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif PuyText.lower().startswith("kapan: "):
                            #if user in PuySekawan or user in PUYWAIT["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

    except Exception as error:
        print (error)

#-------------------------------------------- FINNISHING SCRIP ------------------------------------------------#

while True:
    try:
        Operation = RIDEN.singleTrace(count=50)
        if Operation is not None:
            for fast in Operation:
                RIDEN.setRevision(fast.revision)
                thread1 = threading.Thread(target=RIDEN_FAST_USER, args=(fast,))#self.OpInterrupt[fast.type], args=(fast,)
                thread1.start()
                thread1.join()
    except Exception as error:
        print (error)
