from Food_item import FoodItem
from Menu import Menu
from User import User,Customer,Employee,Admin
from Order import Order
from Restaurant import Restaurant

GromMosla_restaurent=Restaurant('GromMosla_restaurent')#restaurent er obj declare
#Customer Interface
def customar_menu():
    name=input('Enter Your Name: ')
    email=input('Enter Your Email: ')
    phone=input('Enter Your Phone: ')
    address=input('Enter Your Address: ')
    customar=Customer(name=name,phone=phone,email=email,address=address)#customar declare

    while True:
        print(f'Welcome {customar.name}')
        print('1.View Menu')
        print('2.Add Item to Cart')
        print('3.View Cart')
        print('4.Paybill')
        print('5.Exit')
        try:
            choice=int(input("Enter Your Choice: "))
        except ValueError:
            print('Invalid input. Please enter a number between 1-5')
            continue
        if choice==1:
            customar.view_menu(GromMosla_restaurent)
        elif choice==2:
            item=input('Enter Your Item: ')
            quantity=int(input('Enter Your Quantity: '))
            customar.add_to_cart(GromMosla_restaurent,item,quantity)
        elif choice==3:
            customar.view_cart()
        elif choice==4:
            amount=int(input('Enter Your Amount: '))
            customar.paybil(GromMosla_restaurent,amount)
        elif choice==5:
            break
        else:
            print('Invalid Input')
#Admin Interface
def admin_menu():
    name=input('Enter Admin Name: ')
    email=input('Enter Admin Email: ')
    phone=input('Enter Admin Phone: ')
    address=input('Enter Admin Address: ')
    admin=Admin(name=name,phone=phone,email=email,address=address)#Admin declare

    while True:
        print(f'Welcome {admin.name}')
        print('1.Add Item: ')
        print('2.Add Employee: ')
        print('3.View Employee: ')
        print('4.View Menu: ')
        print('5.Item Delete: ')
        print('6.Exit: ')
        try:
            choice=int(input("Enter Your Choice: "))
        except ValueError:
            print('Invalid input. Please enter a number between 1-6')
            continue
        if choice==1:
            item_name =input('Enter Your Add Item Name: ')
            item_price =int(input('Enter Your Add Item price: '))
            item_quantity =int(input('Enter Your Add Item quantity: '))
            item=FoodItem(item_name,item_price,item_quantity)#item banaylam
            admin.add_item(GromMosla_restaurent,item)
        elif choice==2:
             name=input('Enter Employee Name: ')
             email=input('Enter Employee Email: ')
             phone=input('Enter Employee Phone: ')
             address=input('Enter Employee Address: ')
             age=input('Enter Employee Age: ')
             designation=input('Enter Employee Designation: ')
             salary=input('Enter Employee Salary: ')
             employee=Employee(name=name,phone=phone,email=email,
                               address=address,age=age,designation=designation,salary=salary)#Employee declare
             admin.add_employee(GromMosla_restaurent,employee)
        elif choice==3:
            admin.view_employee(GromMosla_restaurent)
        elif choice==4:
            admin.view_menu(GromMosla_restaurent)
        elif choice==5:
            item=input('Enter Your Delete Item: ')
            admin.remove_item(GromMosla_restaurent,item)
        elif choice==6:
            break
        else:
            print('Invalid Input')

#UI-User Interface
while True:
    print('*<->*WELCOME*<->*')
    print('1.ARE YOU ADMIN')
    print('2.ARE YOU CUSTOMAR')
    print('3.EXIT')
    try:
       choice=int(input('Enter Your Choice into (1/2/3):'))
    except ValueError:
        print('Invalid input. Please enter a number between 1-3')
        continue
        #continue
    if choice==1:
        admin_menu()
    elif choice==2:
        customar_menu()
    elif choice==3:
        break
    else:
        print('Invalid Input')

   