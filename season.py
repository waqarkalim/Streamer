class season(object):

    def __init__(self, id, siteURL, episodeList):
        self.id = id
        self.siteURL = siteURL
        self.episodeList = episodeList

    def getId(self):
        return self.id

    def getsiteURL(self):
        return self.siteURL

    def getEpisodeList(self):
        return self.episodeList

    def setId(self, id):
        self.id = id

    def setsiteURL(self, siteURL):
        self.siteURL = siteURL

    def setEpisodeList(self, episodeList):
        self.episodeList = episodeList
