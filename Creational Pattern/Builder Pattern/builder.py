# Abstract Classes

class Packing:

    def pack(self) -> str:
        pass


class Item:

    def name(self) -> str:
        return ""

    def packing(self) -> Packing:
        return None

    def price(self) -> float:
        return 0.0


# Concrete Classes
class Wrapper(Packing):

    def pack(self) -> str:
        return "Wrapper"


class Bottle(Packing):

    def pack(self) -> str:
        return "Bottle"


class Burger(Item):

    def packing(self) -> Packing:
        return Wrapper()


class ColdDrink(Item):

    def packing(self) -> Packing:
        return Bottle()


class VegBurger(Burger):

    def name(self) -> str:
        return "Veg Burger"

    def price(self) -> float:
        return 25.0


class ChickenBurger(Burger):

    def name(self) -> str:
        return "Chicken Burger"

    def price(self) -> float:
        return 50.0


class Pepsi(ColdDrink):

    def name(self) -> str:
        return "Pepsi"

    def price(self) -> float:
        return 35.0


class Coke(ColdDrink):

    def name(self) -> str:
        return "Coke"

    def price(self) -> float:
        return 30.0


class Meal:

    def __init__(self) -> None:
        self._item_list = []

    def addItem(self, item: Item):
        self._item_list.append(item)

    def getCost(self):
        cost = 0
        for item in self._item_list:
            cost += item.price()
        return cost

    def showItems(self):
        for item in self._item_list:
            print(item.name(), end=", ")
            print(item.packing().pack(), end=", ")
            print(item.price())


class MealBuilder:

    def prepareVegMeal(self) -> Meal:
        meal = Meal()
        meal.addItem(VegBurger())
        meal.addItem(Coke())

        return meal

    def prepareNonVegMeal(self) -> Meal:
        meal = Meal()
        meal.addItem(ChickenBurger())
        meal.addItem(Pepsi())

        return meal


if __name__ == "__main__":
    builder = MealBuilder()
    vmeal = builder.prepareVegMeal()
    nmeal = builder.prepareNonVegMeal()

    print("Veg Meal")
    vmeal.showItems()
    print(vmeal.getCost())

    print("Non Veg Meal")
    nmeal.showItems()
    print(nmeal.getCost())
