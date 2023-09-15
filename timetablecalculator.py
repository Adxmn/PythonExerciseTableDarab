# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculator():
    length = 100
    line = "*" * length
    print(line)

    print("\t\t\t\t\t\t\t\t\t\tJADUAL DARAB")

    print(line)

    print("\t", end="")

    for i in range(1, 13):
        print(f"\t{i}\t", end="")
    print()
    print("--------------------------------------------------------------------------------------------------")

    # Print the table
    for j in range(1, 13):
        print(f" {j}\t\t|", end="")
        for i in range(1, 13):
            product = i * j
            print(f"{product}\t\t", end="")
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
