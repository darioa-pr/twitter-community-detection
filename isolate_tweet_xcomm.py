import fileinput
import os
import itertools
import string


class Community:
    def __init__(self, id):
        self.id = id
        self.userList = []
        self.twits = []
        pass

    def addUser(self, id):
        self.userList.append(id)
        pass


class Communities:
    def __init__(self):
        self.commList = []
        pass

    def getCommunityByID(self, id):
        for community in self.commList:
            if community.id == id: return community
        community = Community(id)
        self.commList.append(community)
        return community

    def getCommunityIDByUser(self, userID):
        for community in self.commList:
            if userID in community.userList:
                return community
        return None


fp = open("Brexit_Reduced [Nodes]_res1.csv", "r")

communities = Communities();
i = 0
max = 49728.0

print 'Lettura file'

for line in fp:
    line = line.strip('\n')
    userID, commID = line.split(',')
    community = communities.getCommunityByID(commID)
    community.addUser(userID)
    i = i + 1
    print 'Progresso ', (100.0 / max) * i
    pass

print 'Lettura Twits'

fp.close()

md = open("brexit_tweet_ridotti.txt", "r")

i = 0
max = 93820.0

for line in md:
    i = i + 1
    print 'Progresso ', (100.0 / max) * i
    userID = line.split('\t', 1)[0]
    twit = line.split('\t', 20)[7]
    community = communities.getCommunityIDByUser(userID)
    if community:
        community.twits.append(twit)

md.close()

print 'Scrittura file'


jk = open("test.csv", "a")

for community in communities.commList:
    jk.write(community.id + '\t' + " ".join(community.twits) + '\n')


jk.close()

print 'Fine'
