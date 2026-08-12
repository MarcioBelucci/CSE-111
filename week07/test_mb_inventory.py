from mb_inventory import process_movement, save_inventory, read_inventory
import pytest
import csv


def test_process_movement_add():
    inventory_dict = {"P001": ["Mouse", 45], "P002": ["Keyboard",29], "P003": ["Mousepad",5], "P004": ["Headphone",8]}
    assert process_movement(inventory_dict, "P001", 10, "add") == True 
    assert inventory_dict["P001"][1] == 55
    assert process_movement(inventory_dict, "P002", 1, "add") == True 
    assert inventory_dict["P002"][1] == 30
    assert process_movement(inventory_dict, "P003", 20, "add") == True 
    assert inventory_dict["P003"][1] == 25
    assert process_movement(inventory_dict, "P004", 2, "add") == True 
    assert inventory_dict["P004"][1] == 10

def test_process_movement_subtract_success():
    inventory_dict = {"P001": ["Mouse", 45], "P002": ["Keyboard",29], "P003": ["Mousepad",5], "P004": ["Headphone",8]}
    assert process_movement(inventory_dict, "P001", 10, "subtract") == True 
    assert inventory_dict["P001"][1] == 35
    assert process_movement(inventory_dict, "P002", 1, "subtract") == True 
    assert inventory_dict["P002"][1] == 28
    assert process_movement(inventory_dict, "P003", 3, "subtract") == True 
    assert inventory_dict["P003"][1] == 2
    assert process_movement(inventory_dict, "P004", 4, "subtract") == True 
    assert inventory_dict["P004"][1] == 4

def test_process_movement_subtract_insufficient():
    inventory_dict = {"P001": ["Mouse", 45], "P002": ["Keyboard",29], "P003": ["Mousepad",5], "P004": ["Headphone",8]}
    assert process_movement(inventory_dict, "P001", 50, "subtract") == False 
    assert inventory_dict["P001"][1] == 45
    assert process_movement(inventory_dict, "P002", 30, "subtract") == False 
    assert inventory_dict["P002"][1] == 29
    assert process_movement(inventory_dict, "P003", 6, "subtract") == False 
    assert inventory_dict["P003"][1] == 5
    assert process_movement(inventory_dict, "P004", 10, "subtract") == False 
    assert inventory_dict["P004"][1] == 8

def test_read_inventory():
    with open("test_inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Code","Name","Quantity"])
        writer.writerow(["P010", "Graphic-Card", "100"])
        writer.writerow(["P020", "Monitor", "30"])
    result = read_inventory("test_inventory.csv", 0)

    assert read_inventory("test_inventory.csv", 0) == {"P010": ["Graphic-Card", "100"], "P020": ["Monitor", "30"]}
    assert result["P020"] == ["Monitor", "30"]

def test_save_inventory():
    inventory_dict = {"P015": ["Webcam", "50"]}
    save_inventory(inventory_dict, "test_inventory.csv")

    inventory_dict2 = {"P009": ["Monitor", "20"]}
    save_inventory(inventory_dict2, "test_inventory.csv") 


    with open("test_inventory.csv", "rt") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        for row in reader:
            inventory_list = row

    assert header == ["Code","Name","Quantity"]
    assert inventory_list == ["P009", "Monitor", "20"]


pytest.main(["-v", "--tb=line", "-rN", __file__])