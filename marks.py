#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: December 2019
# This is a program which finds the average of your grade.


def average_of_numbers(list_of_numbers):

    total = 0
    total_number_of_numbers = 0
    counter = 0
    for counter in range(0, len(list_of_numbers)):
        total += list_of_numbers[counter]
        total_number_of_numbers += 1

    average = total/total_number_of_numbers

    average = (average*(10**2)+0.5)
    average = int(average)
    average = float(average)
    average = (average/(10**2))

    return average


def main():
    words = []
    temp_word = None

    # input
    print("Please enter 1 grade at a time. Enter -1 to end.")

    temp_word_as_string = input("Enter a grade: ")
    try:
        temp_word = int(temp_word_as_string)
        words.append(temp_word)

        while temp_word_as_string.upper() != "-1":
            temp_word_as_string = input("Enter a grade: ")

            try:
                temp_word = int(temp_word_as_string)
                words.append(temp_word)
                print("")

            except Exception:
                print('That is not a valid number...')
                print("")
        words.pop()


    # remove the "-1" that was added

        print("Here are the grades you inputted.")
        print(words)

        average = average_of_numbers(words)
        print("average = {0}".format(average))

    except Exception:
        print('That is not a valid number...')
        print("")



if __name__ == "__main__":
    main()
