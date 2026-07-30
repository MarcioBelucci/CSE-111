import csv

def read_dictionary(filename,
key_column_index):
    p_dictionary = {}
    with open(filename, "rt") as csvfile_p:
        csvreader_p = csv.reader(csvfile_p, delimiter=",")
        next(csvreader_p)
        for row in csvreader_p:
            key_value = row[key_column_index]
            p_dictionary[key_value] = row
    return p_dictionary

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1
    products_dict =  read_dictionary("week05/products.csv", KEY_INDEX)
    print("All products:")
    print(products_dict)
    print("Requested products:")
    with open("week05/request.csv", "rt") as csvfile_r:
        csvreader_r = csv.reader(csvfile_r, delimiter=",")
        next(csvreader_r)
        for line in csvreader_r:
            requested_product_key = line[KEY_INDEX]
            requested_quantity = line[QUANTITY_INDEX]
            product = products_dict[requested_product_key]
            product_name = product[NAME_INDEX]
            product_price = product[PRICE_INDEX]

            print(f"{product_name} {requested_quantity} @ {product_price}")




if __name__ == "__main__":
    main()
