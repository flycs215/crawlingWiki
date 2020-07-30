
import wiki
from dirMaker import dirMaker
from PeopleNameGetter import PeopleNameGetter
from fileMaker import fileMaker
import time
import datetime
import wikipediaapi
import progressbar
from time import sleep
from tqdm import tqdm

# Call Class Objects
wiki = wiki.wikiSearcher()
dirMaker = dirMaker()
peopleNameGetter = PeopleNameGetter()
fileMaker = fileMaker()


# Make new Directory in Actual Directory with your input keyword 
dir = dirMaker.dirMake()

# Crawl 100 Peoples names
peopleListForUrl = peopleNameGetter.PeopleNameGet()

# Check Start Time
start = datetime.datetime.now() 
print('-- Start crawling %s'%start) 

# Start wikipedia Crawling
countCrawling = 0
for element in peopleListForUrl:
    wikiContent = wiki.getWikiContents(dir,element)
    wikiContentSplit = wikiContent.splitlines()

    if wikiContent == "" or len(wikiContentSplit)<=2:
        continue
    fileMaker.makeFile(dir, element, wikiContent)

    countCrawling += 1
    if countCrawling % 10 == 0:
        print('Processing ... ' + str((countCrawling/100)*100) + '%')
    if countCrawling == 100:
        break
print(countCrawling)
print('-- End crawling %s'%datetime.datetime.now())
print('- # of cralwed documents: %s'%countCrawling) 
elapsedTime = datetime.datetime.now()-start
seconds = int(round(elapsedTime.total_seconds())) 
print('- elapsed time: %i ' %seconds + 'second')


