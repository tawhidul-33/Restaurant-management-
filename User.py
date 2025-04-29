from abc import ABC 
from Order import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
        self.cart=Order()#order er object banaylam

    def view_menu(self,restaurant):
        print(f'Welcome to our {restaurant.name}')
        restaurant.menu.show_menu()

    def add_to_cart(self,restaurant,item_name,quantity):
        item=restaurant.menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print('Item quantity exceeded!!')
            else:
                copy_item=item.copy_item() #aikhane jokhon FoodItem theke item er boisistu deiy tokhon copy_item method thake oi copy item niye kaj kortechi 
                copy_item.quantity=quantity # ar ai copy kore niyar karone mul menur quantity kno change hoilona
                self.cart.add_to_item(copy_item)
                print('Item_added')
        else:
            print('Item not found')
    def view_cart(self):
        print('**Vew_cart**')
        print('Name\tPrice\tquantity')
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total price:{self.cart.total_price()}')

    def paybil(self,restaurant,amount):
        self.amount=amount

        if self.amount<self.cart.total_price():
            print(f'Payid Not Successful')
        else:
            print(f'Payid Successful {self.cart.total_price()} Tk')

            for item,ad_cart_quty in self.cart.items.items(): #customar er add_cart theke item and quantity ber hobe
                org_menu_item=restaurant.menu.find_item(item.name) # item list theke item find kore ber kore item er org quantity ber kora
                if org_menu_item:
                   org_menu_item.quantity=org_menu_item.quantity-ad_cart_quty
            self.cart.clear() #ad_cart theke delete diya


class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        self.age=age
        self.designation=designation
        self.salary=salary
        super().__init__(name, phone, email, address)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        

    def add_employee(self,restaurant,employee):#aikhane admin rastaurent and employee er obj pathabe
        restaurant.add_employee(employee)
    
        
    def view_employee(self,restaurant):#aikhane admin rastaurent er obj pathabe
        restaurant.view_employee()

    def add_item(self,restaurant,item):
        restaurant.menu.add_item(item)

    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)

    def view_menu(self,restaurant):
        print('Admin Sir Our Menu List')
        restaurant.menu.show_menu()




        
























