import sys


class Order:
    def __init__(self):
        self.sandwiches = []
        self.drinks = []
        self.chips = []
        self.totalPrice = 0.00

    def addSandwich(self, sandwich):
        self.sandwiches.append(sandwich)

    def addDrink(self, drink):
        self.drinks.append(drink)

    def addChip(self, chip):
        self.chips.append(chip)

    def setSandwichPrices(self):
        self.total = sum(sandwich.getTotalPrice() for sandwich in self.sandwiches)
        print(f"{"this is the total",self.total}")

    def setDrinkorChipTotal(self, price):
        self.totalPrice += price

    def getTotal(self):
        return self.totalPrice

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






class OrderMenu:
    def __init__(self):
        self.customerOrder = Order()

    def run(self):
        print("What'll be your order?:")

        while True:
            choice = input(
                "1. Add sandwich.\n2. Add drink.\n3. Add chips.\n4. Checkout.\n0. Cancel\nEnter your choice: "
            )
            if choice == "1":
                self.addSandwich()
            elif choice == "2":
                self.addDrink()
            elif choice == "3":
                self.addChips()
            elif choice == "4":
                self.checkout()
            elif choice == "0":
                print(
                    "Returning to main. You couldn't even handle our sandwiches anyways."
                )
                break
            else:
                print("WRONG! STOP IT!")

    def addSandwich(self):
        size = input(
            "What size sandwich would you like? (4 inch, 8 Inch, or 12 Inch): "
        ).strip()
        size_str = size.lower().replace("inch", "").strip()
        try:
            newSize = int(size_str)
        except ValueError:
            print("Invalid input")
            
            
        bread = (
            input("Which bread would you like? (White, Wheat, Rye, Wraps): ")
            .strip()
            .lower()
        )
        is_toasted = (
            input("Would you like that toasted? (Yes/No): ").strip().lower() == "yes"
        )

        userChoice: int = 0
        print("Would you like meat on your sandwich?")
        print("1: Yes")
        print("2: No")
        userChoice = input("")
        
        meatToppings = [
            "Steak",
            "Ham",
            "Salami",
            "Roast Beef",
            "Chicken",
            "Herring",
            "Bacon",
            "Continue to cheese",
        ]
        cheeseToppings = [
            "American",
            "Provolone",
            "Cheddar",
            "Swiss",
            "PepperJack",
            "Continue to vegetables",
        ]
        vegToppings = [
            "Lettuce",
            "Peppers",
            "Onions",
            "Tomatoes",
            "Jalapenos",
            "Cucumbers",
            "Pickles",
            "Guacamole",
            "Mushrooms",
            "Continue to sauces",
        ]
        sauceToppings = [
            "Mayo",
            "Mustard",
            "Ketchup",
            "Ranch",
            "Thousand Islands",
            "Vinaigrette",
            "Continue to sides",
        ]
        sideToppings = ["Au Jus", "A1", "DELICIOUS RED 40", "No more sides"]

        sandwich = Sandwich(newSize, bread, is_toasted)
        userMeat(userChoice,meatToppings,sandwich)
        userCheese(cheeseToppings, sandwich)
        userToppings(vegToppings, sandwich)
        userSide(sideToppings, sandwich)
        userSauces(sauceToppings, sandwich)

        self.customerOrder.addSandwich(sandwich)
        
        self.customerOrder.setSandwichPrices()
        
        print("This is your total")
        
        print(self.customerOrder.getTotal())


def addDrink(self):
    pass


def addChips(self):
    pass


def checkout(self):
    pass


def userMeat(userChoice, meatToppings, sandwich):
    if userChoice == 1:
        moreMeatToppings = 1

        while moreMeatToppings != 8:
            if moreMeatToppings <= 7:
                print("These are our meat toppings")
                for i in range(1, len(meatToppings) + 1):
                    print(f"{i}: {meatToppings[i - 1]}")

                moreMeatToppings = int(input())

                if len(sandwich.meatToppings) > 1:
                    sandwich.extraMeat()

                sandwich.meatToppings.append(meatToppings[moreMeatToppings - 1])

            if "Continue to cheese" in sandwich.meatToppings:
                sandwich.meatToppings.pop()

            if not sandwich.meatToppings:
                sandwich.meatToppings.append("No meat")
            else:
                print(sandwich.meatToppings)


def userCheese(cheeseToppings, sandwich):
    userChoice2 = 0
    print("Would you like cheese on your sandwich?")
    print("1: Yes")
    print("2: No")
    userChoice2 = int(input())

    if userChoice2 == 1:
        moreCheeseToppings = 1

        while moreCheeseToppings != 6:
            if moreCheeseToppings <= 5:
                print("These are the cheese toppings:")
                for i in range(1, len(cheeseToppings) + 1):
                    print(f"{i}: {cheeseToppings[i - 1]}")

                moreCheeseToppings = int(input())

                if len(sandwich.cheeseToppings) > 1:
                    sandwich.extraCheese()

                sandwich.cheeseToppings.append(cheeseToppings[moreCheeseToppings - 1])

            if "Continue to vegetables" in sandwich.cheeseToppings:
                sandwich.cheeseToppings.pop()

            if not sandwich.cheeseToppings:
                sandwich.cheeseToppings.append("No cheese")
            else:
                print(sandwich.cheeseToppings)


def userSauces(sauceToppings, sandwich):
    userChoice4 = 0
    print("Would you like any sauces on your sandwich?")
    print("1: Yes")
    print("2: No")
    userChoice4 = int(input())

    if userChoice4 == 1:
        moreSauceToppings = 1

        while moreSauceToppings != 7:
            if moreSauceToppings <= 6:
                print("These are our sauces:")
                for i in range(1, len(sauceToppings) + 1):
                    print(f"{i}: {sauceToppings[i - 1]}")

                moreSauceToppings = int(input())
                sandwich.sauceToppings.append(sauceToppings[moreSauceToppings - 1])

            if "Continue to sides" in sandwich.sauceToppings:
                sandwich.sauceToppings.pop()

            if len(sandwich.sauceToppings) < 1:
                sandwich.sauceToppings.append("No sauces")
            else:
                print(sandwich.sauceToppings)


def userSide(sideToppings, sandwich):
    userChoice5 = 0
    print("Would you like any sides with your sandwich?")
    print("1: Yes")
    print("2: No")
    userChoice5 = int(input())

    if userChoice5 == 1:
        moreSideToppings = 1

        while moreSideToppings != 4:
            if moreSideToppings <= 3:
                print("These are our sides:")
                for i in range(1, len(sideToppings) + 1):
                    print(f"{i}: {sideToppings[i - 1]}")

                moreSideToppings = int(input())
                sandwich.sideToppings.append(sideToppings[moreSideToppings - 1])

            if len(sandwich.sideToppings) < 1:
                sandwich.sideToppings.append("No sides")
            else:
                print(sandwich.sideToppings)


def userToppings(vegToppings, sandwich):
    userChoice3 = 0
    print("Would you like vegetables on your sandwich?")
    print("1: Yes")
    print("2: No")
    userChoice3 = int(input())

    if userChoice3 == 1:
        moreVegetableToppings = 1

        while moreVegetableToppings != 10:
            if moreVegetableToppings <= 9:
                print("These are our vegetables:")
                for i in range(1, len(vegToppings) + 1):
                    print(f"{i}: {vegToppings[i - 1]}")

                moreVegetableToppings = int(input())
                sandwich.vegetableToppings.append(
                    vegToppings[moreVegetableToppings - 1]
                )

            if len(sandwich.vegetableToppings) < 1:
                sandwich.vegetableToppings.append("No veggies")
            else:
                print(sandwich.vegetableToppings)


if __name__ == "__main__":
    orderMenu = OrderMenu()
    orderMenu.run()
