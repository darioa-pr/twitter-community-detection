import fileinput
import os
import itertools
import string


class Community:
    def __init__(self, id):
        self.id = id
        self.users = []
        pass

    def addUser(self, user):
        self.users.append(user)
        pass


class User:
    def __init__(self, id):
        self.id = id
        pass

    def setLatLng(self, latLng):
        self.latLng = latLng
        pass


class LatLng:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
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


## ______________________________________________________
## CREAZIONE COMUNITA'
## ______________________________________________________

communities = Communities();

i = 0  #
max = 49728.0  #

fp = open("Brexit_Reduced [Nodes]_res1.csv", "r")

for line in fp:
    line = line.strip('\n')
    userID, commID = line.split(',')
    user = User(userID)
    community = communities.getCommunityByID(commID)  # Cerca una comunità con l'id specificato, se non esiste la crea
    community.addUser(user)  # Aggiunge l'id
    i = i + 1  #
    print 'Lettura file => ', (100.0 / max) * i  #
    pass

fp.close()

## ______________________________________________________
## CALCOLO PUNTO MEDIO
## ______________________________________________________

md = open("brexit_pulita.txt", "r")

i = 0
max = 93820.0

for line in md:

    userID = line.split('\t', 1)[0]
    lat = line.split('\t', 20)[8]
    lng = line.split('\t', 20)[9]

    

    community = communities.getCommunityIDByUser(userID)
    if community:
        community.twits.append(twit)

    i = i + 1
    print 'Progresso ', (100.0 / max) * i

    pass

md.close()

print 'Scrittura file'

jk = open("test.csv", "a")

for community in communities.commList:
    jk.write(community.id + '\t' + " ".join(community.twits) + '\n')

jk.close()

print 'Fine'
