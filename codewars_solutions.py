def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
#The function works by checking whether a number is divisible by 2. If the remainder is 0, the number is even; otherwise, it's odd.

def number_to_string(num):
    return str(num)
#str() is a built-in Python function that converts values into text (a string).


def no_space(x):
    return x.replace(" ", "")
#The function works by replacing all spaces in a string with an empty string, effectively removing them.


def get_count(sentence):
    vowels = "aeiou"
    count = 0

    for letter in sentence:
        if letter in vowels:
            count += 1

    return count
#The function works by iterating through each letter in the sentence and checking if it is a vowel.
#If it is, the count is incremented. The final count is returned.    