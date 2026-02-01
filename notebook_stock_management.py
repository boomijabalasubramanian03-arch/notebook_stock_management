import os

class Notebook:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def to_line(self):
        return f"{self.name},{self.price},{self.quantity}\n"

    @staticmethod
    def from_line(line):
        name, price, quantity = line.strip().split(",")
        return Notebook(name, float(price), int(quantity))

class NotebookStockManager:
    def __init__(self):
        self.inventory_file = "inventory.txt"
        self.admin_file = "admin.txt"
        self.inventory = {}
        self.load_inventory()
        self.load_admin_credentials()

    def load_inventory(self):
        self.inventory.clear()
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, "r") as f:
                for line in f:
                    notebook = Notebook.from_line(line)
                    self.inventory[notebook.name] = notebook

    def save_inventory(self):
        with open(self.inventory_file, "w") as f:
            for notebook in self.inventory.values():
                f.write(notebook.to_line())

    def load_admin_credentials(self):
        if not os.path.exists(self.admin_file):
            with open(self.admin_file, "w") as f:
                f.write("admin:Boomijabalasubramanian\n")

    def admin_login(self):
        username = input("Admin Username: ")
        password = input("Admin Password: ")
        try:
            with open(self.admin_file, "r") as f:
                for line in f:
                    stored_user, stored_pass = line.strip().split(":")
                    if username == stored_user and password == stored_pass:
                        print("Login successful.\n")
                        self.admin_menu()
                        return
            print("Invalid credentials.")
        except Exception as e:
            print("Login error: ",e)

    def admin_menu(self):
        while True:
            print("\n=======ADMIN MENU=====")
            print("1. ADD NOTEBOOK")
            print("2. UPDATE NOTEBOOK STOCK")
            print("3. DELETE NOTEBOOK")
            print("4. VIEW INVENTORY")
            print("5. LOGOUT")
            choice = input("ENTER YOUR CHOICE: ")

            if choice == "1":
                self.add_notebook()
            elif choice == "2":
                self.update_notebook()
            elif choice == "3":
                self.delete_notebook()
            elif choice == "4":
                self.view_inventory()
            elif choice == "5":
                break
            else:
                print("INVALID CHOICE.")

    def add_notebook(self):
        try:
            name = input("NOTEBOOK NAME: ")
            price = float(input("PRICE OF THE NOTEBOOK: "))
            quantity = int(input("QUANTITY: "))
            self.inventory[name] = Notebook(name, price, quantity)
            self.save_inventory()
            print(name,"ADDED.")
        except ValueError:
            print("INVALID INPUT...PRICE AND QUANTITY MUST BE NUMBERS...")

    def update_notebook(self):
        name = input("NOTEBOOK NAME TO UPDATE: ")
        if name in self.inventory:
            try:
                quantity = int(input("ENTER NEW QUANTITY: "))
                self.inventory[name].quantity = quantity
                self.save_inventory()
                print(name,"UPDATED.")
            except ValueError:
                print("INVALID QUANTITY.")
        else:
            print("BILLS...")
    def delete_notebook(self):
        name = input("ENTER NOTEBOOK TO DELETE: ")
        if name in self.inventory:
            del self.inventory[name]
            self.save_inventory()
            print(name,"DELETED.")
        else:
            print("NOTEBOOK NOT FOUND...")

    def view_inventory(self):
        print("\n=====INVENTORY=====")
        if not self.inventory:
            print("NO NOTEBOOKS FOUND...")
        for notebook in self.inventory.values():
            print(notebook.name,":","₹",notebook.price,"STOCK:",notebook.quantity)

    def customer_menu(self):
        while True:
            print("\n=====CUSTOMER MENU=====")
            print("1. VIEW NOTEBOOKS")
            print("2. BUY NOTEBOOK")
            print("3. EXIT")
            choice = input("ENTER YOUR CHOICE:")

            if choice == "1":
                self.view_inventory()
            elif choice == "2":
                self.buy_notebook()
            elif choice == "3":
                break
            else:
                print("INVALID CHOICE")

    def buy_notebook(self):
        name = input("ENTER NOTEBOOK TO BUY: ")
        if name in self.inventory:
            try:
                qty = int(input("ENTER QUANTITY: "))
                if qty <= self.inventory[name].quantity:
                    self.inventory[name].quantity -= qty
                    self.save_inventory()
                    print("YOU BOUGHT",qty,name)
                else:
                    print("NOT ENOUGH STOCK...")
            except ValueError:
                print("INVALID QUANTITY...")
        else:
            print("NOTEBOOK NOT AVAILABLE...")

    def run(self):
        while True:
            print("\n=====WELCOME TO NOTEBOOK STORE=====")
            print("1. ADMIN LOGIN")
            print("2. CUSTOMER ACCESS")
            print("3. EXIT")
            choice = input("ENTER YOUR CHOICE: ")

            if choice == "1":
                self.admin_login()
            elif choice == "2":
                self.customer_menu()
            elif choice == "3":
                print("EXITING!")
                print("THANK YOU FOR USING...")
                break
            else:
                print("INVALID INPUT...")
obj = NotebookStockManager()
obj.run()
