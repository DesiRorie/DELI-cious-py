class Sandwich:
    def __init__(self, size, bread, isToasted):
        self.size = size
        self.bread = bread
        self.isToasted = isToasted
        self.isExtraMeat = False
        self.isExtraCheese = False
        self.meatToppings = []
        self.cheeseToppings = []
        self.vegetableToppings = []
        self.sideToppings = []
        self.sauceToppings = []

        self.breadPrice = 0.0
        self.meatPrice = 0.0
        self.cheesePrice = 0.0
        self.totalPrice = 0.0

        self.setBreadPrice()
        self.setCheesePrice()
        self.setMeatPrice()

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getBread(self):
        return self.bread

    def setBread(self, bread):
        self.bread = bread

    def isToasted(self):
        return self.isToasted

    def setToasted(self, toasted):
        self.isToasted = toasted

    def setBreadPrice(self):
        if self.size == 4:
            self.breadPrice = 5.50
        elif self.size == 8:
            self.breadPrice = 7.0
        else:
            self.breadPrice = 8.50
            print(self.breadPrice)

    def setMeatPrice(self):
        if self.size == 4:
            self.meatPrice = 1.0
        elif self.size == 8:
            self.meatPrice = 2.0
        else:
            self.meatPrice = 3.0
        print(self.meatPrice)

    def addMeatPrice(self):
        self.totalPrice += self.meatPrice

    def extraMeat(self):
        self.isExtraMeat = True
        if self.size == 4 and self.isExtraMeat:
            self.meatPrice += 0.50
        elif self.size == 8 and self.isExtraMeat:
            self.meatPrice += 1.0
        elif self.size == 12 and self.isExtraMeat:
            self.meatPrice += 1.50

    def extraCheese(self):
        self.isExtraCheese = True
        if self.size == 4 and self.isExtraCheese:
            self.cheesePrice += 0.30
        elif self.size == 8 and self.isExtraCheese:
            self.cheesePrice += 0.60
        elif self.size == 12 and self.isExtraCheese:
            self.cheesePrice += 0.90

    def setCheesePrice(self):
        if self.size == 4:
            self.cheesePrice = 0.75
        elif self.size == 8:
            self.cheesePrice = 1.5
        else:
            self.cheesePrice = 2.25

    def addCheesePrice(self):
        self.totalPrice += self.cheesePrice

    def getTotalPrice(self):
        return self.breadPrice + self.meatPrice + self.cheesePrice

    def displayMeat(self):
        if not self.meatToppings:
            return "NO MEAT"
        return " ".join(self.meatToppings)

    def displayCheese(self):
        if not self.cheeseToppings:
            return "NO CHEESE"
        return " ".join(self.cheeseToppings)

    def displayVeg(self):
        if not self.vegetableToppings:
            return "NO VEGGIES"
        return " ".join(self.vegetableToppings)

    def displaySauce(self):
        if not self.sauceToppings:
            return "NO SAUCES"
        return " ".join(self.sauceToppings)

    def displaySides(self):
        if not self.sideToppings:
            return "NO SIDES"
        return " ".join(self.sideToppings)

    def setSandwichPrice(self, price):
        self.totalPrice = price

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description
