class Menu:
    def __init__(self):
        self.items=[]## aita hocche item er database
    def add_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower()==item_name.lower():
                return item
        return None   
    def remove_item(self,item_name):
        item =self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('item deleted') 
        else:
            print('item not found')
    def show_menu(self):
        print('**menu**')
        print('Name\tprice\tquantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')