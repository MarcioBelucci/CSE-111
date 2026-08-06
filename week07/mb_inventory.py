import csv
import datetime from datetime

def read_inventory(filename, key_column_index):
    i_dictionary = {}
    try:
        with open(filename, "rt") as csvfile:
            csvreader_p = csv.reader(csvfile, delimiter=",")
            next(csvreader_p)
            for row in csvreader_p:
                key_value = row[key_column_index]
                i_dictionary[key_value] = row
        return i_dictionary
    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)
    except PermissionError as perm_err:
        print(perm_err)
        print("Check if you have the permission of the owner of the file!")
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file {key_err}")

def read_requests(filename):
    return request_dict
def process_movement(product_dict, key, quantity, action):
    return 
def save_inventory(inventory_dict, filename):

def log_event(date, key, quantity, action, filename):

def get_input(message):
    return str
def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1
    action = 0
    while action != 5:
        print("\nPlease select one of the following options: \n1. Add itens\n2. View the inventory\n3. Deduct Inventory\n4. Reports\n5. Quit")
        action = int(input("Please enter an action: "))
        if action < 1 or action > 5:
            print("Sorry, that is not a valid option.")
        else:
            # Adding itens in the inventory system
            if action == 1:
            

            # Viewing which itens has in the inventory
            elif action == 2:
            
                
            # Deducting itens from inventory
            elif action == 3:
            

            # Reports of the inventory
            elif action == 4:
            

if __name__ == "__main__":
    main()
