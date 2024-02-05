import random


def number_guessing_game(range_list):
    """
    Guess the number game

    This function asks the user to guess the number between the given range

    :param range_list: an integer
    :precondition: range_list's first element must be smaller than the second element
    :precondition: list should have exactly two elements
    :postcondition:the user plays the games without any bugs
    """
    guess_answer = random.randint(range_list[0], range_list[1])
    guess_counter = 0
    print(guess_answer)
    while guess_counter < 7:
        number_guessed = int(input(f"Guess your number [{range_list[0]}-{range_list[1]}]: "))
        if number_guessed == guess_answer:
            print("Congratulations!")
            break
        elif number_guessed < guess_answer:
            guess_counter += 1
            print(f"Your guess is too low, chances left: {7 - guess_counter}")

        elif number_guessed > guess_answer:
            guess_counter += 1
            print(f"Your guess is too high, chances left: {7 - guess_counter}")

    if guess_counter == 7:
        print(f"Your guesses were not right, the correct number was {guess_answer}")


def main():
    range_list = []
    while not range_list:
        range_list = [int(number) for number in
                      input("Please enter a range of numbers separated by a '-': ").split("-")]
        if range_list[0] >= range_list[1]:
            range_list = []
        else:
            break

    number_guessing_game(range_list)


if __name__ == '__main__':
    main()
