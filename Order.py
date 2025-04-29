class Order:
    def __init__(self):
        self.items={}  #dictionary

    def add_to_item(self,item):
        if item in self.items:
            self.items[item] += item.quantity #jodi cart a item thake  
        else:
            self.items[item] = item.quantity #jodi cart a item na thake 
    def remove_item(self,item):
        if item in self.items:
            del self.items[item]
    def total_price(self):
        return sum(item.price*quantity for item,quantity in self.items.items())#items dictionary theke piar akare key and valo ber kore ai fun..items()
    def clear(self):
        self.items={}
