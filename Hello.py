def new_game():
    # This function starts a new quiz game
    guesses = []  # List to store all the user's guesses
    correct_guesses = 0  # Counter for the number of correct answers
    question_num = 1  # Counter to keep track of the current question

    # Loop through each question in the Questions dictionary
    for key in Questions:
        print("--------------------------------------")
        print(key)  # Display the question

        # Display answer choices for the current question
        for option in Answers[question_num - 1]:  # Fetch answers using question_num - 1
            print(option)

        # Get the user's input (A, B, or C) and convert to uppercase
        guess = input("Enter (A, B, C): ").upper()

        # Keep asking until the user enters a valid choice
        while guess not in ['A', 'B', 'C']:
            guess = input("Invalid choice. Enter (A, B, C): ").upper()

        # Store the user's guess
        guesses.append(guess)

        # Check if the guess is correct and update the correct_guesses counter
        correct_guesses += check_answer(Questions[key], guess)

        # Move to the next question
        question_num += 1

    # After all questions are answered, display the results
    display_score(correct_guesses, guesses)


def display_score(correct_guesses, guesses):
    # This function displays the user's quiz results
    print("--------------------------")
    print("Results")
    print("--------------------------")

    # Print the correct answers for all questions
    print("Correct Answers: ", end="")
    for answer in Questions.values():
        print(answer, end=" ")
    print()  # Move to a new line

    # Print the guesses the user made
    print("Your Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()  # Move to a new line

    # Calculate the score as a percentage
    score = int((correct_guesses / len(Questions)) * 100)

    # Display the score
    print(f"Your score is: {score}%")


def check_answer(answer, guess):
    # This function checks if the user's guess is correct
    if answer == guess:
        print("Correct!")  # Notify the user of a correct guess
        return 1  # Return 1 to add to the correct_guesses counter
    else:
        print("Wrong!")  # Notify the user of an incorrect guess
        return 0  # Return 0, no point added


def play_again():
    # This function asks the user if they want to play again
    response = input("Do you want to play again? (yes or no): ").lower()
    return response == "yes"  # Return True if 'yes', False otherwise


# Question-Answer Data
Questions = {
    "Is Earth round?": "A",  # Question 1 and correct answer A
    "How to fight?": "B",    # Question 2 and correct answer B
    "Is Python difficult?": "C",  # Question 3 and correct answer C
}

# Possible answers for each question (lists for each question)
Answers = [
    ["A. Yes", "B. No"],  # Choices for Question 1
    ["A. Punch", "B. Kick"],  # Choices for Question 2
    ["A. Yes", "B. No", "C. Kinda"]  # Choices for Question 3
]

# Game Execution
new_game()  # Start the first game
while play_again():  # Ask if the user wants to play again
    new_game()  # Start a new game if yes
print("Goodbye!")  # Say goodbye after the game ends
