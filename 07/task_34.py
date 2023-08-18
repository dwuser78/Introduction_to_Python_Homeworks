def calc_vowels(phrase) -> int:
    vowel_letters = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
    sum_vowels = 0

    for char in phrase:
        if char in vowel_letters:
            sum_vowels += 1

    return sum_vowels

phrases = input("Введите стих: ").lower().split()

num_vowels = list(map(calc_vowels, phrases))

if num_vowels.count(num_vowels[0]) == len(num_vowels):
    print("Парам пам-пам")
else:
    print("Пам парам")