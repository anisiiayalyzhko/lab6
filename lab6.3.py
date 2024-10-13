def count_vowels():
    A = input("Enter a text: ")

    vowel_count = sum(1 for char in A if char in 'aeiouyAEIOUY')

    print("Number of vowels:", vowel_count)

count_vowels()
