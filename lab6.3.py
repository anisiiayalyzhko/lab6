def count():
    A = input("Enter a text: ")

    vowels_set = set('aeiouyAEIOUY')

    vowels_text = set(A) & vowels_set

    print("Number of vowels:", len(vowels_text))

    return

count()
