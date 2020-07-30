import requests
import urllib3
from bs4 import BeautifulSoup
import requests
import re

class PeopleNameGetter:

    
    def PeopleNameGet(self):
        webpage = requests.get("https://www.biographyonline.net/people/famous-100.html")
        soup = BeautifulSoup(webpage.content, "html.parser")

        i = 1
        j = 0
        count = 0
        peopleList = []
        peopleListForUrl = []
        while i <= 110 or count < 110:
            strSelect = "#p6641 > section > ol:nth-child(2) > li:nth-child(" + str(i) + ")" + " > a"
            
            try:
                strSoup = str(soup.select_one(strSelect).string)
            except AttributeError:
                i = i + 1
                strSelect = "#p6641 > section > ol:nth-child(2) > li:nth-child(" + str(i) + ")" + " > a"
                try:
                    strSoup = str(soup.select_one(strSelect).string)
                except AttributeError:
                    j = j + 1
                    strSelect = "#p6641 > section > ol:nth-child(5) > li:nth-child(" + str(j) + ")" + " > a"
                    strSoup = str(soup.select_one(strSelect).string)    
            peopleList = strSoup.split(" ")
            

            if len(peopleList) < 2:
                peopleForUrl = peopleList[0]
            elif len(peopleList) == 2:
                peopleForUrl = peopleList[0] + "_" + peopleList[1]
            else:
                peopleForUrl = peopleList[0] + "_" + peopleList[1] + "_" + peopleList[2]
            
            peopleListForUrl.append(peopleForUrl)
            i += 1
            count += 1
            print(count)
        
        print("110 people names Crawling Completed")    
        return peopleListForUrl




