from bs4 import BeautifulSoup
import requests, json, time

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



#pulling from espn
source = requests.get('https://www.espn.com/college-sports/football/recruiting/playerrankings/_/view/rn300/sort/rank/class/2018').text
soup = BeautifulSoup(source, 'html5lib')
table = soup.find('div', class_='span-6', id = "my-players-table")
tbody = table.find('tbody')


#iterating over all rows of the ESPN table
list = []
for tr in tbody.find_all('tr'):
    dict = {}
    if(tr.find('div',class_='name') != None):
        #############  ESPN URL  ###############
        url_array = str(tr.find('div',class_='name').a).split('"')
        url = url_array[1]
        dict['url'] = url
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
        dict['offers'] = offer_list

        #############  debug stuff  ###############
        #print(tr.prettify())
        #print()
        list.append(dict)
        #break
        print(dict)
        time.sleep(2)

print(list)
