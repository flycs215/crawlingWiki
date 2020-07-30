class fileMaker:

    def makeFile(self, dir, keyword, wikiContent):
        with open(dir +'/'+ keyword+".txt", "w") as f:
                f.write(wikiContent)


