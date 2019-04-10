#Made by Kevin Topper
from bs4 import BeautifulSoup
import requests, json, time, login

headers={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"en-US,en;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"s_vi=[CS]v1|2E30E37D8507FAC1-6000010B80003247[CE]; UNID=161b0119-eeeb-43c4-a5bd-18bf65c6a31b; ESPN-ONESITE.WEB-PROD.auth=disneyid; ESPN-ONESITE.WEB-PROD-ac=XUS; SWID={609FD710-E667-4B1A-AFDF-3F012F476107}; espnAuth={\"swid\":\"{609FD710-E667-4B1A-AFDF-3F012F476107}\"}; AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg=1; dtcAuth=ESPN_PLUS; s_c6=1552324902648-New; s_sq=%5B%5BB%5D%5D; s_omni_lid=%5B%5BB%5D%5D; edition=espn-en-us; connectionspeed=full; edition-view=espn-en-us; country=us; broadbandAccess=espn3-true%2Cnetworks-false; DE2=\"dXNhO255O2J1ZmZhbG87YnJvYWRiYW5kOzU7NDs0OzUxNDs0Mi45NDE2OTstNzguODM3NDY7ODQwOzMzOzE0Njs2O3VzOw==\"; DS=\"dmVyaXpvbi5uZXQ7NzM3NDE1O21jaSBjb21tdW5pY2F0aW9ucyBzZXJ2aWNlcyBpbmMuIGRiYSB2ZXJpem9uIGJ1c2luZXNzOw==\"; _omnicwtest=1552952782951; _cb_ls=1; _cb=INLPmCbG6-5PVWap; _chartbeat2=.1546716755264.1552952784673.0000000000000001.Ded9SsDvN-TdDMwVqUBOi91hBXClzh.1; _cb_svref=null; UNID=161b0119-eeeb-43c4-a5bd-18bf65c6a31b; userZip=14221; AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg=-330454231%7CMCAID%7C2E30E37D8507FAC1-6000010B80003247%7CMCIDTS%7C17974%7CMCMID%7C90446614011983908062998598862853325162%7CMCAAMLH-1553557654%7C7%7CMCAAMB-1553557654%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1552960054s%7CNONE%7CvVersion%7C3.1.2; _omnicwtest=works; check=true; mbox=session#6957a3795a86445d9330af92625503bb#1552954715|PC#6957a3795a86445d9330af92625503bb.17_111#1616197655; block.check=false%7Cfalse; tveMVPDAuth=; tveAuth=; espn_s2=AECbUT4MJFMcl6uRccl3xkPIpkxK%2FvcelIMg6%2Brxxej2WBwlfPrk%2BUYUG0SpVLaO11AUqrEW47Z2SeAnwHS69KbOBrOlST8Dv6X9cx17JtMmh0PjmpewDH589eX3ipMlNVA2LSo13UYNpbeDrnrZjj8HKArFyMtTEQkXTNPHbrEo0CVfHFLnWmIcEND1Sbti2gko%2Bg05ExvXJHABhLPkRUK9IoOKoZrQvPmJtRZu2d5W008ctGcC6wFnAnx7COsw%2B9iDJeuVrM4J8N4UoU9yEcxR; SWID_NT=0; userZip=14221; visionBrowserSession=1552952855545; visionLocalSession={%22session_id_local%22:%221552952855536-2003121647567%22}; visionLocalVisitor={}; visionSession={%22timestamp%22:1552952855549}; visionVisitor={}; optimizelyEndUserId=oeu1552952855553r0.06638249259827878; __qca=P0-508644946-1552952856845; s_pers=%20s_c24%3D1552952864147%7C1647560864147%3B%20s_c24_s%3DFirst%2520Visit%7C1552954664147%3B%20s_gpv_pn%3Despndevcenter%253Adocumentation%253Aindex%7C1552954664161%3B; s_sess=%20s_cc%3Dtrue%3B%20s_omni_lid%3D%3B%20s_sq%3D%3B%20s_ppv%3D92%3B",
"DNT":"1",
"Host":"insider.espn.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}



def get_scouting_report_pre_2014(url):
    report=""
    z = requests.get(url, headers=headers)
    soup = BeautifulSoup(z.text, features="lxml")
    div = soup.find("div",{"class":"mod-content article"}).find_all("p")
    for p in div:
        if(len(p.text)>30):
            report += p.text + '\n\n'
    print(report)
    return report

get_scouting_report_pre_2014('http://insider.espn.com/college-sports/football/recruiting/player/evaluation/_/id/132850/anthony-jennings')
