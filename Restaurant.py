from Menu import Menu
class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[] # aita hocche amader database

        self.menu=Menu()# Menu() class er object banaylam

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} is added')

    def view_employee(self):
        print('Employee List')
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address,emp.age,emp.designation,emp.salary)
        
