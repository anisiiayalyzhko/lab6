def split_list():
    A = input("Enter elements of the list using digitals and letters: ")

    mixed_list = A.split()

    letters = [item for item in mixed_list if item.isalpha()]
    numbers = [item for item in mixed_list if item.isdigit()]

    print("Letters:", letters)
    print("Digitals:", numbers)

split_list()
