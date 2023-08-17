import Constants

class Player:

    name = ""
    borglars = 0
    up1 = 1
    up2 = 1
    up3 = 1
    up1Cost = 1
    up2Cost = 1
    up3Cost = 1

    def __init__(self, ):
        pass

    def borglarClick(self):
        self.borglars += self.up1
        if self.up3 > 1:
            self.borglars *= 1 + self.up3 * Constants.up3Multiplier

    def borglarFactory(self):
        if self.up2 > 1:
            self.borglars += self.up2 * Constants.up2Multiplier
            if self.up3 > 1:
                self.borglars *= 1 + self.up3 * Constants.up3Multiplier

    def upgrade1(self):
        if self.canBuy(self.up1Cost):
            self.borglars -= self.up1Cost
            self.up1 += 1
            self.up1Cost = self.up1 * Constants.up1CostMultiplier

    def upgrade2(self):
        if self.canBuy(self.up2Cost):
            self.borglars -= self.up2Cost
            self.up2 += 1
            self.up2Cost = self.up2 * Constants.up2CostMultiplier

    def upgrade3(self):
        if self.canBuy(self.up3Cost):
            self.borglars -= self.up3Cost
            self.up3 += 1
            self.up3Cost = self.up3 * Constants.up3CostMultiplier

    def canBuy(self, price):
        return self.borglars >= price

