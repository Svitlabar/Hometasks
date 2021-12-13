class Warehouse:
    devices_dict = []
    department_dict = []

    def __init__(self, i, n):
        self.i = i
        self.n = n

    @staticmethod
    def acceptance(cls, obj):
        Warehouse.devices_dict = Warehouse.devices_dict + [cls.accept(obj)]
        return Warehouse.devices_dict

    def write_off(self):
        transferred_items = Warehouse.devices_dict[self.i].copy()
        transferred_items.popitem()
        if Warehouse.devices_dict[self.i].get("quantity") > self.n:
            print(f"Device {[i]} in quantity {n}, units has been moved to the department X\n")
            Warehouse.department_dict = Warehouse.department_dict + [transferred_items]
            Warehouse.devices_dict[self.i]["quantity"] = Warehouse.devices_dict[self.i].get("quantity") - self.n
            Warehouse.department_dict[-1].update({"quantity dep": self.n})
        elif Warehouse.devices_dict[self.i].get("quantity") == self.n:
            print(f"Device {[i]} in quantity {n}, units has been moved to the department X\n")
            Warehouse.department_dict = Warehouse.department_dict + [transferred_items]
            Warehouse.devices_dict.pop(self.i)
            Warehouse.department_dict[-1].update({"quantity dep": self.n})
        else:
            print("Number chosen is bigger than quantity of devices available at stock\n")
        return Warehouse.devices_dict, Warehouse.department_dict


class OfficeEquipment:

    def __init__(self, brand, quantity, price):
        self.brand = brand
        self.quantity = quantity
        self.price = price

    def accept(self):
        devices_dict = {"name": "Printer", "brand": self.brand, "price, EUR/unit": self.price,
                        "quantity": self.quantity}
        return devices_dict


class Printer(OfficeEquipment):
    devices_list = []

    def __init__(self, brand, quantity, price, color):
        OfficeEquipment.__init__(self, brand, quantity, price)
        self.color = color

    def accept(self):
        devices_dict = {"name": "Printer", "brand": self.brand, "color": self.color, "price, EUR/unit": self.price,
                        "quantity": self.quantity}
        return devices_dict


class Scanner(OfficeEquipment):
    def __init__(self, brand, quantity, price, type):
        OfficeEquipment.__init__(self, brand, quantity, price)
        self.type = type

    def accept(self):
        devices_dict = {"name": "Scanner", "brand": self.brand, "type": self.type, "price, EUR/unit": self.price,
                        "quantity": self.quantity}
        return devices_dict


class Copier(OfficeEquipment):
    def __init__(self, brand, quantity, price, speed):
        OfficeEquipment.__init__(self, brand, quantity, price)
        self.speed = speed

    def accept(self):
        devices_dict = {"name": "Copier", "brand": self.brand, "speed": self.speed, "price, EUR/unit": self.price,
                        "quantity": self.quantity}
        return devices_dict


printer_1: Printer = Printer("Canon", 5, 200.00, "black-white")
printer_1.accept()
Warehouse.acceptance(Printer, printer_1)

printer_2 = Printer("HP", 8, 180.00, "black-white")
printer_2.accept()
Warehouse.acceptance(Printer, printer_2)

scanner_1 = Scanner("Canon", 4, 220.00, "flatbed")
scanner_1.accept()
Warehouse.acceptance(Scanner, scanner_1)

scanner_2 = Scanner("HP", 9, 350.00, "broaching")
scanner_2.accept()
Warehouse.acceptance(Scanner, scanner_2)

copier_1 = Copier("HP", 7, 800.00, "20 copies/min")
copier_1.accept()
Warehouse.acceptance(Copier, copier_1)

copier_2 = Copier("Canon", 9, 700.00, "20 copies/min")
copier_2.accept()
Warehouse.acceptance(Copier, copier_2)

while True:
    print("\nChose action:\n"
          "[1] Retrieve list of goods available at Warehouse\n"
          "[2] Add new goods to Warehouse\n"
          "[3] Retrieve list of goods available in Department X\n"
          "[4] Transfer goods to Department X\n"
          "[Q] Quit \n")
    action = input("Your choice: ")
    if action == "Q":
        break
    elif action == "1":
        print("List of goods available at Warehouse: \n")
        for el, v in enumerate(Warehouse.devices_dict, 1):
            print(f"{el}. {v}")

    elif action == "2":
        while True:
            name = input("Chose name of product: \n"
                         "  [1] Printer\n"
                         "  [2] Scanner\n"
                         "  [3] Copier\n"
                         "  or enter [Q] for quit\n")
            if name == "Q":
                break
            elif name == "1" or name == "2" or name == "3":
                brand = input("Enter brand: ")
                quantity = input("Enter quantity of devices: ")
                price = input("Enter price, EUR/unit in format 0.00: ")
                try:
                    quantity = int(quantity)
                    price = f"{float(price):.2f}"
                except ValueError as err:
                    print("Incorrect Value added for quantity or price, please enter data for last goods item "
                          "one more time")
                    break
                if name == "1":
                    color = input("Enter color (color or black-white): ")
                    printer_i = Printer(brand, quantity, price, color)
                    printer_i.accept()
                    Warehouse.acceptance(Printer, printer_i)
                    print("Device successfully added to Warehouse\n")

                elif name == "2":
                    type = input("Enter type (flatbed or broaching): ")
                    scanner_i = Scanner(brand, quantity, price, type)
                    scanner_i.accept()
                    Warehouse.acceptance(Scanner, scanner_i)
                    print("Device successfully added to Warehouse\n")

                elif name == "3":
                    speed = input("Enter speed: ")
                    copier_i = Copier(brand, quantity, price, speed)
                    copier_i.accept()
                    Warehouse.acceptance(Copier, copier_i)
                    print("Device successfully added to Warehouse\n")

            else:
                print("Incorrect data entered\n")

    elif action == "3":
        if not Warehouse.department_dict:
            print("No devices yet in Department X")
        else:
            for el_1, v_1 in enumerate(Warehouse.department_dict, 1):
                print(f"{el_1}. {v_1}")

    elif action == "4":
        while True:
            name = input("Chose name of product: \n"
                         "      [1] Printer\n"
                         "      [2] Scanner\n"
                         "      [3] Copier\n"
                         "      or enter [Q] for returning to previous menu\n")
            if name == "Q":
                break
            elif name == "1" or name == "2" or name == "3":
                codes_list = []
                print("List of goods available at Warehouse: \n")
                for p in Warehouse.devices_dict:
                    if p.get("name") == "Printer" and name == "1":
                        print(f"Device code: [{Warehouse.devices_dict.index(p)}] {p}")
                        codes_list = codes_list + [Warehouse.devices_dict.index(p)]
                    elif p.get("name") == "Scanner" and name == "2":
                        print(f"Device code: [{Warehouse.devices_dict.index(p)}] {p}")
                        codes_list = codes_list + [Warehouse.devices_dict.index(p)]
                    elif p.get("name") == "Copier" and name == "3":
                        print(f"Device code: [{Warehouse.devices_dict.index(p)}] {p}")
                        codes_list = codes_list + [Warehouse.devices_dict.index(p)]

                i = input("\nChose product data from the list by entering number of device position number from [ ]: ")
                n = input("Enter number of units for transferring to Department X: ")
                try:
                    i = int(i)
                    n = int(n)
                except (ValueError, IndexError) as err:
                    print(err, "\n")
                else:
                    if codes_list.count(i) == 1:
                        transfer_item = Warehouse(i, n)
                        transfer_item.write_off()
                    else:
                        print("\nPosition code is out of the list\n")

            else:
                print("Incorrect data entered")
    else:
        print("Incorrect data entered")
