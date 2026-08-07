import csv
from datetime import datetime

def read_inventory(filename, key_column_index):
    inventory_dict = {}
    try:
        with open(filename, "rt") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            next(csvreader)
            for row in csvreader:
                key_value = row[key_column_index]
                inventory_dict[key_value] = row[1:]
        return inventory_dict
    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)
    except PermissionError as perm_err:
        print(perm_err)
        print("Check if you have the permission of the owner of the file!")
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file {key_err}")

#def read_request(filename, key_column_index):
    request_dict = {}
    try:
        with open(filename, "rt") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            next(csvreader)
            for row in csvreader:
                key_value = row[key_column_index]
                request_dict[key_value] = row
        return request_dict
    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)
    except PermissionError as perm_err:
        print(perm_err)
        print("Check if you have the permission of the owner of the file!")
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file {key_err}")

def process_movement(product_dict, key, quantity, action_file):
    if action_file == "add":
        product_dict[key][1] = int(product_dict[key][1]) + quantity
        return True
    elif action_file == "subtract":
        if quantity > int(product_dict[key][1]):

            return False
        product_dict[key][1] = int(product_dict[key][1]) - quantity
        return True


def save_inventory(inventory_dict, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Code","Name","Quantity"])
        for key, values in inventory_dict.items():
            writer.writerow([key] + values)

def log_event(date, key, quantity, action, filename):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, key, quantity, action])

def get_input(message):
    user_input = input(message)
    return user_input

def main():
    KEY_INDEX = 0
    NAME_INDEX = 0
    QUANTITY_INDEX = 1
    today = datetime.now()
    action = 0
    while action != 5:
        print("\nPlease select one of the following options: \n1. Add itens\n2. View the inventory\n3. Deduct Inventory\n4. Reports\n5. Quit")
        try:
            action = int(input("Please enter an option: "))
        except ValueError as val_err:
            print()
            print(type(val_err).__name__, val_err, sep=": ")
            print("You entered an invalid option.")
            continue
   
        if action < 1 or action > 5:
            print("Sorry, that is not a valid option.")
        else:
            inventory_dict = read_inventory("week07/inventory.csv", KEY_INDEX)
            # Adding itens in the inventory system
            if action == 1:
                product_code = get_input("Enter the code of the product: ")
                product_quantity = int(get_input("Enter the quantity of the product: "))
                try:
                    system_answer = process_movement(inventory_dict, product_code, product_quantity, "add")
                    if system_answer == True:
                        log_event(today.strftime("%a %b %e %H:%M:%S %Y"), product_code, product_quantity, "add", "week07/log.csv")
                        save_inventory(inventory_dict, "week07/inventory.csv")
                except KeyError as key_err:
                    print(f"Error: unknown product ID in the request.csv file {key_err}")

            # Viewing which itens has in the inventory
            elif action == 2:
                for code, data in inventory_dict.items():
                    print(f"{code} - {data[NAME_INDEX]}: {data[QUANTITY_INDEX]} units")
                
            # Deducting itens from inventory
            elif action == 3:
                product_code = get_input("Enter the code of the product: ")
                product_quantity = int(get_input("Enter the quantity of the product: "))
                try:
                    system_answer = process_movement(inventory_dict, product_code, product_quantity, "subtract")
                    if system_answer == True:
                        log_event(today.strftime("%a %b %e %H:%M:%S %Y"), product_code, product_quantity, "add", "week07/log.csv")
                        save_inventory(inventory_dict, "week07/inventory.csv")
                except KeyError as key_err:
                    print(f"Error: Unable to process: insufficient quantity or product not found. {key_err}")

            # Reports of the inventory
            elif action == 4:
                try:
                    with open("week07/log.csv", "rt") as file:
                        reader = csv.reader(file, delimiter=",")
                        next(reader)
                        for row in reader:
                            print(row)
                except FileNotFoundError as file_err:
                    print("Error: missing file")
                    print(file_err)
                except PermissionError as perm_err:
                    print(perm_err)
                    print("Check if you have the permission of the owner of the file!")                

if __name__ == "__main__":
    main()