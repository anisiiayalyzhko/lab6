def no_negatives():
    numbers = list(map(int, input("Enter the numbers of the list: ").split()))

    for i in range(len(numbers)):
        if numbers[i] < 0:
            numbers[i] = 0

    print("List with no negatives:", numbers)

no_negatives()
