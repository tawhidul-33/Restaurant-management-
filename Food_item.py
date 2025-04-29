class FoodItem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    #copy item er jonno
    def copy_item(self):
        return FoodItem(self.name, self.price, self.quantity)
