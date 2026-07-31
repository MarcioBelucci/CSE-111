# I set a reminder of how many days until the New Years Sale begins (Jan 1) at the bottom of the receipt.
import csv
from datetime import datetime

def read_dictionary(filename,
key_column_index):
    p_dictionary = {}
    try:
        with open(filename, "rt") as csvfile_p:
            csvreader_p = csv.reader(csvfile_p, delimiter=",")
            next(csvreader_p)
            for row in csvreader_p:
                key_value = row[key_column_index]
                p_dictionary[key_value] = row
        return p_dictionary
    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)
    except PermissionError as perm_err:
        print(perm_err)
        print("Check if you have the permission of the owner of the file!")
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file {key_err}")

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1
    today = datetime.now()
    new_years_sale = datetime(2027, 1, 1)
    day_to_new_years_sale = new_years_sale - today
    store_name = "MB Store"
    total_quantity = 0
    subtotal = 0
    products_dict =  read_dictionary("week05/products.csv", KEY_INDEX)
    print(store_name)
    print("\nOrdered Items:")
    try:
        with open("week05/request.csv", "rt") as csvfile_r:
            csvreader_r = csv.reader(csvfile_r, delimiter=",")
            next(csvreader_r)
            for line in csvreader_r:
                requested_product_key = line[KEY_INDEX]
                requested_quantity = int(line[QUANTITY_INDEX])
                product = products_dict[requested_product_key]
                product_name = product[NAME_INDEX]
                product_price = float(product[PRICE_INDEX])
                subtotal = subtotal + product_price * requested_quantity
                total_quantity += requested_quantity

                print(f"{product_name}: {requested_quantity} - ${product_price:.2f}")

            print(f"\nTotal of items: {total_quantity}")
            print(f"Subtotatl: ${subtotal:.2f}")
            tax_amount = subtotal * 0.06
            print(f"Tax Amount: ${tax_amount:.2f}")
            total_price = tax_amount + subtotal
            print(f"Total: ${total_price:.2f}")
            print("\nThank you for shopping at the MB Store.")
            print(today.strftime("%a %b %e %H:%M:%S %Y"))
            print(f"We have {day_to_new_years_sale.days} days until the New Years Sale!")
    except PermissionError as perm_err:
        print(perm_err)
        print("Check if you have the permission of the owner of the file!")
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file {key_err}")
    except FileNotFoundError as file_err:
            print("Error: missing file")
            print(file_err)




if __name__ == "__main__":
    main()
