from Player import Player
import Constants

import pymongo

class Model:
    
    ##set to your connection address
    connection = pymongo.MongoClient('mongodb://localhost:27017')
    db = connection['CAAV']
    collection = db['User']
    player = Player()

    def __init__(self):
        pass

    def postNewUser(self, userName, passCode):
        if self.getUserByName(userName) != None:
            return 1
        self.collection.insert_one({
            "name": userName,
            "passCode": passCode,
            "borglars": 0,
            "up1": 1,
            "up2": 1,
            "up3": 1
        })
        self.playerSetup(userName)
        return 0
    
    def userLogin(self, userName, passCode):
        if self.collection.find_one({
            "name": userName,
            "passCode": passCode
        }) == None:
            return 2
        self.playerSetup(userName)
        return 0

    def getUserByName(self, userName):
        return self.collection.find_one({
            "name":userName
        })
    
    def playerSetup(self, userName):
        player = self.getUserByName(userName)
        self.player.name = player["name"]
        self.player.borglars = player["borglars"]
        self.player.up1 = player["up1"]
        self.player.up2 = player["up2"]
        self.player.up3 = player["up3"]
        self.player.up1Cost = self.player.up1 * Constants.up1CostMultiplier
        self.player.up2Cost = self.player.up2 * Constants.up2CostMultiplier
        self.player.up3Cost = self.player.up3 * Constants.up3CostMultiplier

    def saveGame(self):
        self.collection.update_one({"name":self.player.name}, 
            {"$set":{
                "borglars": int(self.player.borglars),
                "up1": self.player.up1,
                "up2": self.player.up2,
                "up3": self.player.up3
                }
            }
        )