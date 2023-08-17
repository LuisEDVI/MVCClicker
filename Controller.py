from Model import Model

class Controller:

    model = Model()
    player = model.player

    def __init__(self):
        pass

    def login(self, userName, code):
        return self.model.userLogin(userName, code)
        
    def signup(self, userName, code, confirmCode):
        res = self.model.postNewUser(userName, code)
        if(code == confirmCode) and res == 0:
            return 0
        elif(code != confirmCode):
            return 3
        return res

    def saveGame(self):
        self.model.saveGame()

    def playerClick(self):
        self.player.borglarClick()
    
    def playerFactory(self):
        self.player.borglarFactory()

    def playerBuyUpgrade1(self):
        self.player.upgrade1()
    
    def playerBuyUpgrade2(self):
        self.player.upgrade2()

    def playerBuyUpgrade3(self):
        self.player.upgrade3()