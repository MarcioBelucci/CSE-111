def main():
    provinces_list = read_list("week05/provinces.txt")
    print(provinces_list)
    provinces_list.pop(0)
    provinces_list.pop()
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")

def read_list(filename):
    row_list = []
    with open(filename, "rt") as file_list:
        for line in file_list:
            clean_line = line.strip()
            row_list.append(clean_line)
    return row_list

if __name__ == "__main__":
    main()