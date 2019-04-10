#Made by Kevin Topper
from bs4 import BeautifulSoup
import requests, json, time, login, csv

############# returns list of schools that gave an offer ###############
def offers(link):
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html5lib')
    tbody = soup.find('div',class_='span-4').find('tbody')
    retVal = []
    for tr in tbody.find_all('tr'):
        a = tr.find_all('a')
        if len(a) != 0:
            school_arr = str(a[1]).split('>')
            school_arr = school_arr[1].split('<')
            offer = school_arr[0]
            retVal.append(offer)
    return retVal

def picture(url):
    z = requests.get(url)
    soup = BeautifulSoup(z.text, features="lxml")
    div = soup.find("div",{"class":"player-photo"})
    ret = str(div).split('"')
    return ret[3]

#returns a string of a player's scouting report
def scouting_report_post_2014(link):
    return login.get_scouting_report_post_2014(link)
def scouting_report_pre_2014(link):
    return login.get_scouting_report_pre_2014(link)




#pulling from espn
year = 2006
list = []

#iterating over all rows of the ESPN table
def script(year):
    print("beginning year " + str(year))
    ###########ESPN REQUEST##############
    source = requests.get('https://www.espn.com/college-sports/football/recruiting/playerrankings/_/view/rn300/sort/rank/class/'+str(year)).text
    soup = BeautifulSoup(source, 'html5lib')
    table = soup.find('div', class_='span-6', id = "my-players-table")
    tbody = table.find('tbody')
    ##########################
    progress = 1
    for tr in tbody.find_all('tr'):
        dict = {}
        if(tr.find('div',class_='name') != None):
            #############  ESPN URL  ###############
            url_array = str(tr.find('div',class_='name').a).split('"')
            url = url_array[1]
            #dict['url'] = url
            #############  PLAYER NAME  ###############
            name = tr.find('div',class_='name').strong.text
            dict['name'] = name

            #############  HOMETOWN  ###############
            td_array = tr.find_all('td')
            hometown = str(td_array[3]).partition('<br/>')
            hometown = hometown[0].split('>')
            hometown = hometown[1]
            dict['hometown'] = hometown

            #############  HEIGHT  ###############
            height = td_array[4].text
            dict['height'] = height

            #############  WEIGHT  ###############
            weight = td_array[5].text
            dict['weight'] = weight

            #############  OFFERS  ###############
            offer_list = offers(url)
            dict['committed_to'] = offer_list[0]
            dict['offers'] = offer_list

            ########### PHOTO URL ###########
            try:
                dict['photo'] = picture(url)
            except:
                dict['photo'] = 'No Photo'

            ######### SCOUTING REPORT ###########
            insider_link = url.replace('www','insider')
            temp = insider_link.split('/player')
            new = temp[0] + '/player/evaluation' + temp[1]
            #print(insider_link)
            report = ""
            try:
                if(int(year) > 2013):
                    report = scouting_report_post_2014(new)
                else:
                    report = scouting_report_pre_2014(new)
            except:
                report = ""
            dict['report'] = report
            ###############YEAR##############
            dict['year'] = year

            #############  debug stuff  ###############
            #print(tr.prettify())
            #print()
            list.append(dict)
            print(progress, end = ' ', flush = True)
            progress+=1
            time.sleep(.3)

    #print(list)

    '''
    Now we must write our list to csv
    '''

while(year < 2019):
    try:
        script(year)
    except:
        print('year exception, restarting year ' + str(year))
        script(year)
    year+=1

toCSV = list
keys = toCSV[0].keys()
with open('players.csv', 'w', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)
print('csv is complete')
