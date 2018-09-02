from GENERATOR import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
#from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\n\n============= HI =============\n")

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

Rfu = [cl]
mid = cl.profile.mid
RfuBot=[mid]
Owner=["uac8e3eaf1eb2a55770bf10c3b2357c33"]
RfuSekawan = RfuBot + Rfu + Owner

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

Squad = {
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
        "uac8e3eaf1eb2a55770bf10c3b2357c33":True,  #MID ADMIN HERE
        "uac8e3eaf1eb2a55770bf10c3b2357c33":True
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
setTime = Squad['readTime']
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

RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Helpz ="""    「 Group Commands 」
Tagall / Mentionall
Ceksider on/off
 'Ceksider' :
  Melihat Pembaca.
 'Recheck' :
  Mengulang titik Pembaca.
Getsider on/off
Groupinfo
Url on/off
Geturl

  「 Token - OFFLINE 」
Tokenlist / offline

'''Once Again, An JUST FOR FUN!'''"""

Helpz2 ="""    「 Fun Commands 」
@Me
Calendar
Wikipedia: [query]
Write [text]
1Cak
Instainfo: [username]
Deviantart [query]

  「 Token - OFFLINE 」
Tokenlist / offline

'''Once Again, An JUST FOR FUN!'''"""

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
            if Squad["autoAdd"] == True:
                if (Squad["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Squad["ContactAdd"][fast.param2] = True
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} " + str(Squad["PesanAdd"]).format(usr.displayName))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':mid}, contentType=13)
#--------------------------------------------- PARAM SCRIP AUTO JOIN BOT & AUTO REJECT ------------------------------------------------#
        if fast.type == 13:
            if mid in fast.param3:
              if Squad['autoJoin'] == True:
                if fast.param2 in RfuSekawan and fast.param2 in Squad["Admin"]:
                    cl.acceptGroupInvitation(fast.param1)
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
                                                "text": "JOINED GROUP", #% (elapsed_time),
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
                                                #"text": "%s" % (elapsed_time),
                                                "text": "Hei '{}'".format(str(contact.displayName)),
                                                #str(" "+ginfo.name+" ")
                                                "size": "md",
                                                "align": "start",
                                                "gravity": "top",
                                                "color": "#0000ff",
                                                "wrap": True
                                            },
                                            {
                                                "type": "text",
                                                #"text": "%s" % (elapsed_time),
                                                "text": "Terimakasih sudah mengundang saya ke group '{}' ketik Help untuk Bantuan!".format(str(ginfo.name)),
                                                #str(" "+ginfo.name+" ")
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
                    print ("ANDA JOIN DI GRUP")

        if fast.type == 13:
            if mid in fast.param3:
              if Squad['AutoReject'] == True:
                if fast.param2 not in RfuSekawan and fast.param2 not in Squad["Admin"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP SIDER & WC LV ------------------------------------------------#

        elif fast.type == 55:
            try:
                if RfuCctv['Point1'][fast.param1]==True:
                    if fast.param1 in RfuCctv['Point2']:
                        Name = cl.getContact(fast.param2).displayName
                        if Name in RfuCctv['Point3'][fast.param1]:
                            pass
                        else:
                            RfuCctv['Point3'][fast.param1] += "「" + Name + "」 \n"
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cl.mentionWithRFU(fast.param1,fast.param2,"and the Reader Comes ","" + " ")
                                else:
                                    cl.mentionWithRFU(fast.param1,fast.param2,"Hei, ","" + "What are You doing There")
                            else:
                                cl.mentionWithRFU(fast.param1,fast.param2,"Hellooo, ","" + "Comeon Join the Conversation")
                    else:
                        cl.mentionWithRFU(fast.param1,fast.param2,"Hei, ","" + "How are you today?")
                else:
                    pass
            except:
                pass

        if fast.type == 55:
            try:
                if fast.param1 in Squad['readPoint']:
                    if fast.param2 in Squad['readMember'][fast.param1]:
                        pass
                    else:
                        Squad['readMember'][fast.param1] += fast.param2
                    Squad['ROM'][fast.param1][fast.param2] = fast.param2
                else:
                   pass
            except:
                pass

        if fast.type == 17:
            if Squad["Welcome"] == True:
                if fast.param2 not in Rfu:
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
                    #cl.mentionWithRFU(fast.param1,fast.param2," Hello","" + "\n " + str(Squad['WcText']))
                    #cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if fast.type == 15:
            if Squad["Leave"] == True:
                if fast.param2 not in Rfu:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithRFU(fast.param1,fast.param2," Hello","" + "\n " + str(Squad['LvText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

#--------------------------------------------- PARAM SCRIP ------------------------------------------------#

        if fast.type == 46:
            if fast.param2 in RfuBot:
                cl.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 26:
            msg = fast.message
            text = msg.text
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["autoRead"] == True:
                        cl.sendChatChecked(kirim, msg_id)
                    if kirim in Squad["readPoint"]:
                        if user not in Squad["ROM"][kirim]:
                            Squad["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(kirim,text)
                    if Squad["Timeline"] == True:
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
                    if Squad['AutoRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Squad['MentionText'])]
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
            if msg.contentType == 0 and user not in RfuSekawan or user not in Squad["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Squad['KickRespon'] == True:
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
            rfuText = msg.text
            msg_id = msg.id
            kirim = msg.to
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Squad["autoRead"] == True:
                        cl.sendChatChecked(0, msg_id)

                    elif rfuText is None:
                        return
                    else:
                        if rfuText.lower() == 'PROSES TRANSISI':
                            cl.sendMessage(0, user)

                        elif rfuText.lower() == "@group":
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                 cl.sendMessage(kirim, str(Helpz))

                        elif rfuText.lower() == "@fun":
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                 cl.sendMessage(kirim, str(Helpz2))

                        elif rfuText.lower() == "devlist":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                rfu = ""
                                sekawan = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    rfu += str(wa) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in Squad["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    sekawan += str(wi) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendText(kirim,"     「 Devlist 」\nOwner :\n"+rfu+"\nAdmin :\n"+sekawan+" ") #+ str(len(Owner)+len(Squad["Admin"])))

                        elif rfuText.lower() == "grouplist":
                            groups = cl.getGroupIdsJoined()
                            ret_ = "      「 Group List 」"
                            no = 0
                            for gid in groups:
                                group = cl.getGroup(gid)
                                no += 1
                                ret_ += "\n{}. {} = {} Members".format(str(no), str(group.name), str(len(group.members)))
                            ret_ += "\n   「 {} Groups 」".format(str(len(groups)))
                            cl.sendText(kirim, str(ret_))

                        elif rfuText.lower() == "@bye": #With INDUK
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
                                                            "text": "OUT GROUP", #% (elapsed_time),
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
                                print ("OUT GROUP")

                        elif rfuText.lower() == "leaveall grup":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Leave All group")

                        elif rfuText.lower() == 'url on':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)

                        elif rfuText.lower() == "asking ":
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

                        elif rfuText.lower() == 'url off':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)

                        elif rfuText.lower() == 'geturl':
                          #if user in RfuSekawan or user in Squad["Admin"]:
                            if msg.toType == 2:
                                grup = cl.getGroup(kirim)
                                if grup.preventedJoinByTicket == True:
                                   grup.preventedJoinByTicket == False
                                   cl.updateGroup(grup)
                                set = cl.reissueGroupTicket(kirim)
                                cl.sendMessage(kirim, "  Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                #else:
                                    #cl.sendMessage(kirim, "Ketik Link on Dulu kaka")

                        elif rfuText.lower() == 'groupinfo':
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
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                                cuki = " "
                                cuki += "Group Name : {}".format(str(group.name))
                                #cuki += "\nID Group : {}".format(group.id)
                                cuki += "\nGroup Creator : {}".format(str(gCreator))
                                cuki += "\nMembers : {}".format(str(len(group.members)))
                                cuki += "\nPendings Member : {}".format(gPending)
                                cuki += "\nGroup Ticket Status : {}".format(gTicket)
                                cuki += "\nGroup Qr : {}".format(gQr)
                                #cl.sendMessage(kirim, str(cuki))
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
                                                            "text": "   「 Info Group 」\n", #% (elapsed_time),
                                                            "size": "md",
                                                            "weight": "bold",
                                                            "align": "center",
                                                            "gravity": "top",
                                                            "color": "#000000",
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "{}".format(str(cuki)),
                                                            "size": "sm",
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

                        elif rfuText.lower().startswith("1cak"):
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

                        elif rfuText in ["creepypasta"]:
                            r=requests.get("http://hipsterjesus.com/api")
                            data=r.text
                            data=json.loads(data)
                            hasil = " 「 Creepypasta 」 \n\n" 
                            hasil += str(data["text"])
                            cl.sendMessage(kirim, str(hasil))

                        elif rfuText in ["randomlose"]:
                            group = cl.getGroup(to)
                            try:
                                members = [mem.mid for mem in group.members]
                            except:
                                members = [mem.mid for mem in group.members]
                            message = random.choice(members)
                            cl.mentionWithRFU(kirim, "< RandomLoseMem >\n\n• The Loser is :", [sender])
                            cl.sendContact(kirim, message)

                        elif rfuText in ["alquran:"]:
                                try:
                                    sep = rfuText.split(" ")
                                    search = rfuText.lower().replace(sep[0] + " ","")
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

                        elif rfuText in ["/myrobot "]:
                            if msg.toType == 2:
                                url = rfuText.lower().replace("/myrobot ","")
                                urlnya = 'https://robohash.org/'+url+'.png'
                                cl.sendMessage(kirim,"Ini adalah karakter robotmu !!")
                                cl.sendImageWithURL(msg.to,urlnya)
                                print ("@MyRobot")
                            else:
                                if wait["lang"] == "JP":
                                    cl.sendMessage(kirim,"Perintah ini hanya bisa di grup")
                                else:
                                    cl.sendMessage(kirim,"Perintah ini hanya bisa di grup")

                        elif rfuText in ["friendinfo "]:
                            separate = rfuText.split(" ")
                            number = rfuText.lower().replace(separate[0] + " ","")
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

                        elif rfuText in ["unfriendall"]:
                            try:
                                friend = cl.getContacts(cl.getAllContactIds())
                                cl.sendMessage(kirim,"Menghapus {} Teman".format(len(friend)))
                                for unfriend in friend:
                                    cl.deleteContact(unfriend.mid)
                                cl.sendMessage(kirim,"Berhasil menghapus {} Teman".format(len(friend)))
                            except Exception as error:
                                cl.sendMessage(kirim, "   「 Result Error 」\n" + str(error))

                        elif rfuText in ["Memberlist"]:
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                kontak = cl.getGroup(kirim)
                                group = kontak.members
                                num=1
                                msgs="   「 Daftar Member 」"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\n「Total Member %i」" % len(group)
                                cl.sendText(kirim, msgs)

                        elif rfuText.lower() == 'all respon':
                            #txt = ['how are you all?','Hai guys','Puy here','hai semua','selamat beraktivitas']
                            #isi = random.choice(txt)
                            #tts = gTTS(text=isi, lang='id', slow=False)
                            #tts.save('temp2.mp3')
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 1","MSG_SENDER_ICON":"http://pbs.twimg.com/profile_images/1001808982615277568/EPVaEr4P_400x400.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 2","MSG_SENDER_ICON":"http://aov.hasagi.gg/wp-content/uploads/2018/06/Sarah-Viloid.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 3","MSG_SENDER_ICON":"https://scontent-lga3-1.cdninstagram.com/vp/4e31f6f9f995df211c10c565507b4830/5BDEFCD3/t51.2885-19/s150x150/26158377_969899119824478_5446520578645164032_n.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 4","MSG_SENDER_ICON":"http://asset-a.grid.id/crop/0x0:0x0/700x465/photo/2018/08/08/3351787273.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 5","MSG_SENDER_ICON":"http://cdn2.tstatic.net/pekanbaru/foto/bank/images/sarah-viloid-olivia-gamer_20180806_183745.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 6","MSG_SENDER_ICON":"https://i.ytimg.com/vi/kuqy1j6r-Xk/maxresdefault.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 7","MSG_SENDER_ICON":"https://scontent-mrs1-1.cdninstagram.com/vp/bea084c9b99f2c1026af825a8682c881/5C107258/t51.2885-15/e35/36775985_2073120879617880_7681327508842610688_n.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 8","MSG_SENDER_ICON":"https://i.pinimg.com/originals/58/e8/d6/58e8d63c8384fbf649ce33196f156904.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 9","MSG_SENDER_ICON":"https://i.ytimg.com/vi/bSQ7yPV-1Ag/mqdefault.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 10","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-s7hRHwVUY7c/WcT4qaWOxZI/AAAAAAAADAE/GJa8f584UvcW5fZBGJ12VMRIw1CJ8hX7ACK4BGAYYCw/s400/sarah.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 11","MSG_SENDER_ICON":"https://3.bp.blogspot.com/-lb5rG03TPrg/V47hiQzjmLI/AAAAAAAAAtQ/FxLHG6Sz1jMyz0MXCRvnROTiVN07x8dsgCLcB/s1600/IMG_20160720_091426.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 12","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-Q-xhtNI-bSE/V2ZUo6aQL1I/AAAAAAAAAVk/ENETZiBTIKgP5z9S_iZV1skmiwyF7kPcgCLcB/s1600/Viloid.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 13","MSG_SENDER_ICON":"https://scontent-lax3-1.cdninstagram.com/vp/50a708702c5a70e0b48e76685df541fa/5BFEFBD3/t51.2885-15/sh0.08/e35/s640x640/29094007_125595028282088_4752627668053131264_n.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 14","MSG_SENDER_ICON":"https://s.kaskus.id/images/2017/09/20/6474659_20170920084803.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 15","MSG_SENDER_ICON":"https://i.pinimg.com/originals/54/c4/fb/54c4fb5e52a3847eb6959dc3c05d23e4.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 16","MSG_SENDER_ICON":"https://scontent-atl3-1.cdninstagram.com/vp/761c1a85622c69d9f256d56a6de8260b/5BF890CE/t51.2885-15/e35/22280485_1754719227873455_8068433645670498304_n.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 17","MSG_SENDER_ICON":"https://pbs.twimg.com/profile_images/864425427061792768/EAF1kF5K_400x400.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 18","MSG_SENDER_ICON":"https://scontent-ort2-1.cdninstagram.com/vp/cfbd942f6753cf5a80d0b0ee9d231b1a/5BDCF2EB/t51.2885-15/e35/c0.135.1080.1080/s480x480/36032532_234661703930470_3939402733274005504_n.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 19","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-c7jQmeoVxh0/WQM8RQ0w2NI/AAAAAAAAA8M/C13jErjBDT00QLQ9eX-wjY1PP-Y8-8eCgCLcB/s640/Sarah%2BViloid.jpg"})
                            cl.sendMessage(kirim,"◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 20","MSG_SENDER_ICON":"https://scontent-lga3-1.cdninstagram.com/vp/b0da32ae64d5f1bab8a351e4e4ac069b/5C325DB8/t51.2885-15/sh0.08/e35/c0.135.1080.1080/s640x640/39100754_1839310616147166_1453085189692456960_n.jpg"})
                            cl.sendMessage(kirim,"◇ Already Active ◇")
                            #cl.sendMessage(kirim, isi)
                            #cl.sendAudio(kirim, 'temp2.mp3')

                        elif rfuText.lower() == 'def respon':
                            txt = ['how are you all?','Hai guys','Puy here','hai semua','selamat beraktivitas']
                            isi = random.choice(txt)
                            tts = gTTS(text=isi, lang='en', slow=False)
                            tts.save('temp2.mp3')
                            cl.sendMessage(kirim,"◇ DEF HERE",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 10","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-s7hRHwVUY7c/WcT4qaWOxZI/AAAAAAAADAE/GJa8f584UvcW5fZBGJ12VMRIw1CJ8hX7ACK4BGAYYCw/s400/sarah.jpg"})
                            cl.sendMessage(kirim,"◇ DEF HERE",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 11","MSG_SENDER_ICON":"https://3.bp.blogspot.com/-lb5rG03TPrg/V47hiQzjmLI/AAAAAAAAAtQ/FxLHG6Sz1jMyz0MXCRvnROTiVN07x8dsgCLcB/s1600/IMG_20160720_091426.jpg"})
                            cl.sendMessage(kirim,"◇ DEF HERE",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 12","MSG_SENDER_ICON":"https://2.bp.blogspot.com/-Q-xhtNI-bSE/V2ZUo6aQL1I/AAAAAAAAAVk/ENETZiBTIKgP5z9S_iZV1skmiwyF7kPcgCLcB/s1600/Viloid.jpg"})
                            cl.sendMessage(kirim,"◇ DEF HERE",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 13","MSG_SENDER_ICON":"https://scontent-lax3-1.cdninstagram.com/vp/50a708702c5a70e0b48e76685df541fa/5BFEFBD3/t51.2885-15/sh0.08/e35/s640x640/29094007_125595028282088_4752627668053131264_n.jpg"})
                            cl.sendMessage(kirim,"◇ DEF HERE",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 14","MSG_SENDER_ICON":"https://s.kaskus.id/images/2017/09/20/6474659_20170920084803.jpg"})
                            cl.sendMessage(kirim,"◇ DEF HERE",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 15","MSG_SENDER_ICON":"https://i.pinimg.com/originals/54/c4/fb/54c4fb5e52a3847eb6959dc3c05d23e4.jpg"})
                            cl.sendMessage(kirim,"◇ DEF HERE",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 16","MSG_SENDER_ICON":"https://scontent-atl3-1.cdninstagram.com/vp/761c1a85622c69d9f256d56a6de8260b/5BF890CE/t51.2885-15/e35/22280485_1754719227873455_8068433645670498304_n.jpg"})
                            cl.sendMessage(kirim,"◇ DEF HERE",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 17","MSG_SENDER_ICON":"https://pbs.twimg.com/profile_images/864425427061792768/EAF1kF5K_400x400.jpg"})
                            cl.sendMessage(kirim,"◇ DEF Already Active ◇")
                            #cl.sendMessage(kirim, isi)
                            cl.sendAudio(kirim, 'temp2.mp3')

                        elif rfuText.lower() == 'ceksider on':
                            #if user in RfuSekawan or user in Squad["Admin"]:
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
                                if kirim in Squad['readPoint']:
                                        try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                        except:
                                            pass
                                        Squad['readPoint'][kirim] = msg.id
                                        Squad['readMember'][kirim] = ""
                                        Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                        Squad['ROM'][kirim] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(Squad, fp, sort_keys=True, indent=4)
                                            cl.sendMessage(kirim,"  「 Reader Notify 」\nIs now Active!")
                                else:
                                    try:
                                        del read['readPoint'][kirim]
                                        del read['readMember'][kirim]
                                        del read['readTime'][kirim]
                                    except:
                                        pass
                                    Squad['readPoint'][kirim] = msg.id
                                    Squad['readMember'][kirim] = ""
                                    Squad['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                    Squad['ROM'][kirim] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(Squad, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(kirim, "  「 Reader Notify 」\nSetting Reader Point!\n  At: " + readTime)

                        elif rfuText.lower() == 'ceksider off':
                            #if user in RfuSekawan or user in Squad["Admin"]:
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
                                if kirim not in Squad['readPoint']:
                                    cl.sendMessage(kirim,"  「 Reader Notify 」\nIs now Unactive!")
                                else:
                                    try:
                                            del Squad['readPoint'][kirim]
                                            del Squad['readMember'][kirim]
                                            del Squad['readTime'][kirim]
                                    except:
                                          pass
                                    cl.sendMessage(kirim, "  「 Reader Notify 」\nDeleting Reader Point!\n  At: " + readTime)

                        elif rfuText.lower() == 'recheck':
                            #if user in RfuSekawan or user in Squad["Admin"]:
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
                                if kirim in Squad["readPoint"]:
                                    try:
                                        Squad["readPoint"][kirim] = True
                                        Squad["readMember"][kirim] = {}
                                        Squad["readTime"][kirim] = readTime
                                        Squad["ROM"][kirim] = {}
                                    except:
                                        pass
                                    cl.sendMessage(kirim, "  「 Reader Notify 」\nResetting Readerchecker!\n  At: " + readTime)
                                else:
                                    cl.sendMessage(kirim, "  「 Reader Notify 」\nGot Invalid,\n  '''Checkread on''' first!")

                        elif rfuText.lower() == 'ceksider':
                            #if user in RfuSekawan or user in Squad["Admin"]:
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
                                if kirim in Squad['readPoint']:
                                    if Squad["ROM"][kirim].items() == []:
                                        cl.sendMessage(kirim,"  「 Reader 」:\nNone")
                                    else:
                                        chiya = []
                                        for rom in Squad["ROM"][kirim].items():
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
                                    text = xpesan+ zxc + "  At: " + readTime
                                    try:
                                        cl.sendMessage(kirim, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cl.sendMessage(kirim,"  「 Reader Notify 」\nGot Invalid,\n  '''Checkread on''' first!")

                        elif rfuText.lower() == 'getsider on':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    del RfuCctv['Point2'][kirim]
                                    del RfuCctv['Point3'][kirim]
                                    del RfuCctv['Point1'][kirim]
                                except:
                                    pass
                                RfuCctv['Point2'][kirim] = msg.id
                                RfuCctv['Point3'][kirim] = ""
                                RfuCctv['Point1'][kirim]=True
                                cl.sendText(kirim,"  「 Reader Notify 」\nStarting get reader!")

                        elif rfuText.lower() == 'getsider off':
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                if kirim in RfuCctv['Point2']:
                                    RfuCctv['Point1'][kirim]=False
                                    cl.sendText(kirim, RfuCctv['Point3'][kirim])
                                else:
                                    cl.sendText(kirim, "  「 Reader Notify 」\nIs now Unactive hee!")

                        elif rfuText.lower().startswith("tagall"):
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                gname = cl.getGroup(kirim)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n In {} '.format(str(gname.name))
                                            atas += '\n Has {} Members'.format(str(len(local)))
                                        cl.sendMessage(kirim, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText.lower().startswith("mentionall"):
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                gname = cl.getGroup(kirim)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n In {} '.format(str(gname.name))
                                            atas += '\n Has {} Members'.format(str(len(local)))
                                        cl.sendMessage(kirim, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText in ["Welcomsg on"]:
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = True
                                cl.sendText(kirim,"Cek Welcome Already ON")
                        elif rfuText in ["Welcomsg off"]:
                          if user in RfuSekawan or user in Squad["Admin"]:
                            if user in RfuSekawan:
                                Squad['Welcome'] = False
                                cl.sendText(kirim,"Cek Welcome Already Off")

                        elif rfuText.lower().startswith("changewelcome: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["WcText"] = data
                                    cl.sendText(kirim,"Welcome Message Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Error")

                        elif rfuText.lower().startswith("hack "):
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
                                xz = rfuText.replace(names.split(":")[0]+" ","")
                                #print(xz)
                                cl.sendMessage(kirim,xz, "◇ Hei",contentMetadata={"MSG_SENDER_NAME":"PUY'Z 1","MSG_SENDER_ICON":"http://pbs.twimg.com/profile_images/1001808982615277568/EPVaEr4P_400x400.jpg"})

                        elif rfuText.lower().startswith("say "):
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
                                puy = rfuText.split(" ")
                                puy = rfuText.replace(puy[0]+" "," ")
                                puy = puy.split('')
                                txt = str(puy[0])
                                #xz = rfuText.replace(names.split(":")[0]+" ","")
                                #print(xz)
                                cl.sendMessage(kirim, (txt),contentMetadata={"MSG_SENDER_NAME":"{}".format(contact.displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)})

                        elif rfuText in ["Leave on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = True
                                cl.sendText(kirim,"Cek Leave Already ON")
                        elif rfuText in ["Leave off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['Leave'] = False
                                cl.sendText(kirim,"Cek Leave Already Off")

                        elif rfuText.lower().startswith("changeleave: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                teks = rfuText.split(": ")
                                data = rfuText.replace(teks[0] + ": ","")
                                try:
                                    Squad["LvText"] = data
                                    cl.sendText(kirim,"Leave Message Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Error")

                        elif rfuText.lower() == "runtimez":
                            if user in Owner:
                                eltime = time.time() - mulai
                                opn = " "+waktu(eltime)
                                cl.sendText(kirim,"Active in :" + opn)

                        elif rfuText.lower().startswith("broadcast: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("Teks: ","")
                                gid = cl.getGroupIdsJoined()
                                owner = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," By","\n" + str(" "+bc+" "))

                        elif rfuText.lower().startswith("contactbc: "):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                bc = msg.text.replace("Teks: ","")
                                gid = cl.getAllContactIds()
                                owner = "uac8e3eaf1eb2a55770bf10c3b2357c33"
                                for i in gid:
                                    cl.mentionWithRFU(i,owner," By","\n" + str(" ("+bc+")"))

                        elif rfuText.lower().startswith("adminadd"):
                            if user in RfuSekawan:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Squad["Admin"]:
                                        cl.sendText(kirim, "User added to Admin")
                                    else:
                                        try:
                                            Squad["Admin"][target] = True
                                            cl.sendText(kirim, "User in Admin ")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower().startswith("admindel"):
                            if user in Owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Squad["Admin"]:
                                        cl.sendText(kirim, "User not Registered as Admin")
                                    else:
                                        try:
                                            del Squad["Admin"][target]
                                            cl.sendText(kirim, "Success Deleted User as Admin")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif rfuText.lower() == "remove chat":
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    cl.removeAllMessages(fast.param2)
                                    ginfo = cl.getGroup(kirim)
                                    #cl.mentionWithRFU(kirim,owner,"Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    cl.sendText(kirim, 'Remove Message Success in this Group!')
                                except:
                                    pass

                        elif rfuText.lower() == 'restart':
                            if user in RfuSekawan:
                                cl.sendText(kirim, 'Restarting...')
                                print ("Restarting Server")
                                restart_program()

                        elif rfuText.lower() == 'bot logout':
                            if user in RfuSekawan:
                                cl.mentionWithRFU(kirim,user,"!Exit","")
                                print ("Selfbot Off")
                                exit(1)

                        elif rfuText.lower() == 'my grup':
                            if user in RfuSekawan or user in Squad["Admin"]:
                                groups = cl.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cl.sendText(kirim, str(ret_))

                        elif rfuText.lower().startswith("rejectall grup"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    cl.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    cl.sendMessage(kirim, "Nothing Invited")

                        elif rfuText.lower().startswith("status"):
                            if user in Owner:
                                try:
                                    hasil = "Status Bot\n"
                                    if Squad["autoAdd"] == True: hasil += "\nAuto Add ( on )"
                                    else: hasil += "\nAuto Add ( off )"
                                    if Squad["autoJoin"] == True: hasil += "\nAuto Join ( on )"
                                    else: hasil += "\nAuto Join ( off )"
                                    if Squad["AutoReject"] == True: hasil += "\nAuto Reject Room ( on )"
                                    else: hasil += "\nAuto Reject Room ( off )"
                                    if Squad["AutojoinTicket"] == True: hasil += "\nAuto Join Ticket ( on )"
                                    else: hasil += "\nAuto Join Ticket ( off )"
                                    if Squad["autoRead"] == True: hasil += "\nAuto Read ( on )"
                                    else: hasil += "\nAuto Read ( off )"
                                    if Squad["AutoRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Mention ( off )"
                                    if Squad["KickRespon"] == True: hasil += "\nDetect Mention ( on )"
                                    else: hasil += "\nDetect Kick Mention ( off )"
                                    if Squad["Timeline"] == True: hasil += "\nCheck Post Timeline ( on )"
                                    else: hasil += "\nCheck Post ( off )"
                                    hasil += "\n"
                                    cl.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif rfuText in ["Autojoin on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = True
                                cl.sendText(kirim,"Join Set To On..")
                        elif rfuText in ["Autojoin off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['autoJoin'] = False
                                cl.sendText(kirim,"Join Set To Off..")

                        elif rfuText in ["Autoreject on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = True
                                cl.sendText(msg.to,"Reject Set To On..")
                        elif rfuText in ["Autoreject off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad['AutoReject'] = False
                                cl.sendText(msg.to,"Reject Set To Off..")

                        elif rfuText in ["Adminadd:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = True
                                cl.sendText(kirim,"   「 Admin Notify 」\nSent Contact to Add!")
                        elif rfuText in ["Adminadd:off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["Adminadd"] = False
                                cl.sendText(kirim,"   「 Admin Notify 」\nAdding admin is now Off!")

                        elif rfuText in ["Adminrem:on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = True
                                cl.sendText(kirim,"   「 Admin Notify 」\nSent Contact to Remove!")
                        elif rfuText in ["Adminrem:off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AdminDel"] = False
                                cl.sendText(kirim,"   「 Admin Notify 」\nRemoving admin is now Off!")

                        elif rfuText in ["jointicket on"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = True
                                cl.sendText(kirim,"Join Ticket Set To On")
                        elif rfuText in ["jointicket off"]:
                            if user in RfuSekawan or user in Squad["Admin"]:
                                Squad["AutojoinTicket"] = False
                                cl.sendText(kirim,"Join Ticket Set To Off")
                        elif '/ti/g/' in rfuText.lower():
                            if user in RfuSekawan or user in Squad["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Squad["AutojoinTicket"] == True:
                                        group=cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        cl.sendText(kirim,"Success Masuk %s" % str(group.name))

                        elif rfuText.lower() == 'refreshprofile':
                            if user in RfuSekawan or user in Squad["Admin"]:
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

                        elif rfuText.lower().startswith("refresh"):
                            if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    cl.sendText(kirim,"   「 Refresh 」\nWaiting for 5s!")
                                    time.sleep(5.0)
                                    Squad['autoJoin'] = False
                                    Squad['autoAdd'] = False
                                    Squad['AutojoinTicket'] = False
                                    Squad['AutoReject'] = False
                                    Squad['Upfoto'] = False
                                    Squad['UpfotoBot'] = False
                                    Squad['UpfotoGrup'] = False
                                    Squad['Adminadd'] = False
                                    Squad['AdminDel'] = False
                                    Squad['Welcome'] = False
                                    Squad['Leave'] = False
                                    cl.sendText(kirim,"   「 Refresh 」\nDone Refresh!")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))
#------------ TEMPLATE ------------#
### Help ###
                        elif rfuText.lower().startswith("helpz"):
                            #Help = Help
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
                                                        "text": "「 MENU 」\n\n", #% (elapsed_time),
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#000000",
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": " " + str(Helpz),
                                                        "size": "sm",
                                                        "align": "start",
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
### Help Ended ###
### Token ###
                        elif rfuText.lower().startswith("tokenlist"):
                            r = requests.get("https://rfutoken.herokuapp.com/iosipad/rfu")
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

                        elif rfuText.lower().startswith("tokenlistz"):
                            r = requests.get("https://rfutoken.herokuapp.com/iosipad/chromeos")
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
                        elif rfuText.lower().startswith("speed"):
                            no = time.time()
                            cl.sendText("uac8e3eaf1eb2a55770bf10c3b2357c33", ' ')
                            elapsed_time = time.time() - no
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
                                                        "text": "   「 Speed Sender Messages 」\n", #% (elapsed_time),
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#000000",
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "%s" % (elapsed_time),
                                                        #"text": "%s".format(str(elapsed_time)),
                                                        "size": "md",
                                                        "align": "center",
                                                        "gravity": "top",
                                                        "color": "#0000ff"
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
### Speed Ended ###
                        elif rfuText.lower().startswith("lolz"):
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
                        elif rfuText.lower().startswith("wikipedia: "):
                            wiki = rfuText.lower().replace("wikipedia: ","")
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
### INSTAGRAM ###
                        elif rfuText.lower().startswith("instainfo: "):
                            sep = rfuText.split(" ")
                            instagram = rfuText.replace(sep[0] + " ","")
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
                        elif rfuText.lower().startswith("write "):
                            bcd = rfuText.lower().replace("write ","")
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
                        elif rfuText.lower().startswith("runtime"):
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
                        elif rfuText.lower().startswith("@about"):
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
                                              "hero": {
                                                "type": "image",
                                                "url": "https://media1.tenor.com/images/4648a40f88dd6c80e1304ba200f210dc/tenor.gif",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "20:13" #20:13
                                              },
                                              "body": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "text": "Dibuat oleh Puy",
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
                                                    "text": "Terimakasih kepada :",
                                                    "wrap": True
                                                  },
                                                  {
                                                    "type": "text",
                                                    "align": "center",
                                                    "weight": "regular",
                                                    "color": "#aaaaaa",
                                                    "size": "sm",
                                                    "text": "- Tuhan YME\n- Icad\n- Ical\n- Iyan\n- Zubair\n- Ree\n- Nazri\n- (F)",
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
                                                      "label": "Add Creator",
                                                      "uri": "http://line.me/ti/p/~yapuy"
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
                            
                        elif rfuText.lower().startswith("help"):
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
                                                "spacing": "sm",
                                                "contents": [
                                                  {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "spacing": "sm",
                                                    "contents": [
                                                      {
                                                        "type": "text",
                                                        "align": "center",
                                                        "text": "@Group"
                                                      },
                                                      {
                                                        "type": "separator",
                                                        "color": "#FA0B0B"
                                                      },
                                                      {
                                                        "type": "text",
                                                        "align": "center",
                                                        "text": "@Fun"
                                                      }
                                                    ]
                                                  },
                                                  {
                                                    "type": "separator",
                                                    "color": "#FA0B0B"
                                                  },
                                                  {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "spacing": "sm",
                                                    "contents": [
                                                      {
                                                        "type": "text",
                                                        "align": "center",
                                                        "text": "@Bye"
                                                      },
                                                      {
                                                        "type": "separator",
                                                        "color": "#FA0B0B"
                                                      },
                                                      {
                                                        "type": "text",
                                                        "align": "center",
                                                        #"color": "#FFDDDD",
                                                        "text": "@About"
                                                      }
                                                    ]
                                                  }
                                                ]
                                            }
                                        }
                                    }
                                ]
                            }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)

                        elif rfuText.lower().startswith("deviantart "):
                            query = rfuText.lower().replace("deviantart ","")
                            try:
                                search = rfuText.lower().replace("deviantart ","")
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

                        elif rfuText.lower().startswith("imageart "):
                            try:                                   
                                search = rfuText.lower().replace("imageart ","")
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
                        elif rfuText.lower().startswith("@tokenlist"):
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
                        elif rfuText.lower().startswith("calendar"):
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
                        elif rfuText.lower().startswith("@me"):
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
                                                    "size": "md",
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
                            
                        elif rfuText.lower().startswith("@deviantart "):
                            query = rfuText.lower().replace("@deviantart ","")
                            try:
                                search = rfuText.lower().replace("@deviantart ","")
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
                        elif rfuText.lower().startswith("myname"):
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
                              #cl.sendText(kirim,"2\n"+riden1.authToken)
                              #cl.sendText(kirim,"3\n"+riden2.authToken)
                              #cl.sendText(kirim,"4\n"+riden3.authToken)
                              #cl.sendText(kirim,"5\n"+riden4.authToken)
                              #cl.sendText(kirim,"6\n"+riden5.authToken)
                              #cl.sendText(kirim,"7\n"+riden6.authToken)
#------------ SCRIPT PUY ENDED -----------#

                        elif rfuText.lower().startswith("apakah: "):
                            #if user in RfuSekawan or user in Squad["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif rfuText.lower().startswith("kapan: "):
                            #if user in RfuSekawan or user in Squad["Admin"]:
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
