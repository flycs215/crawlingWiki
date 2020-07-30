import wikipediaapi

class wikiSearcher:

    def getWikiContents(self, dir, keyword):
        wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
            )
        
        pageTotal = wiki.page(keyword)

        # pageSplit = pageStr.split('\\s+')
        # pageSplitPhr = pageStr.split('\\n')

        title = pageTotal.title
        content = pageTotal.text
        contentSplit= content.split('\n')
        contentTotal = title + '\n' + '\n' + contentSplit[0]
        
        return contentTotal

    
