class episode(object):

    def __init__(self, id, name, siteURL, sourceLink):
        self.id = id
        self.name = name
        self.siteURL = siteURL
        self.sourceLink = sourceLink

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getsiteURL(self):
        return self.siteURL

    def getsourceLink(self):
        return self.sourceLink

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setsiteURL(self, siteURL):
        self.siteURL = siteURL

    def setsourceLink(self, sourceLink):
        self.sourceLink = sourceLink
