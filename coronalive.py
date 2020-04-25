#scraping HTML
import requests
from bs4 import BeautifulSoup
import urllib.request 

def getCoronaVirusData():
    r = requests.get('https://www.worldometers.info/coronavirus/#countries')
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('a',attrs = {'class':'mt_a'})       #class is the type of the identifer and mt_a is the name of the class im tag <a>
    return results

# results = getCoronaVirusData()
# length = len(results)  

#Take the value of position of the infected country and return the name of it 
def country_corona(pos):
    country = results[pos-1:pos]
    country = country[-1].text
    return country


def list_of_Countries_Asending(num):
    # loop for countries pos in corona virus
    i=1
    while(i <= num):
        # print(i)
        count = country_corona(i)
        print(count)
        i=i+1



# print(results)

# print (list_of_Countries_Asending(5))
# print (country_corona(1))
# print (length)