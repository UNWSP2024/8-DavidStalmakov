# David Stalmkaov, 10/24/2025
# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random
# Dictionary of the states and their capitals. (I didn't do all of them).
state_capitals = {"Alaska": "Juneau", "Minnesota": "StPaul", "Hawaii": "Honolulu", "Idaho": "Boise",
                  "Iowa": "Des Moines", "Wisconsin": "Madison", "Texas": "Austin", "Nebraska": "Lincoln"}
states = list(state_capitals.keys())
random.shuffle(states)

correct = 0
incorrect = 0

# Quiz
for state in states:
    answer = input(f"What is the capital of {state}?  ").strip()

    if answer == state_capitals[state]:
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect. The capital of {state} is {state_capitals[state]}.")
        incorrect += 1

# Results
print("Finished Quiz with:")
print(f"Correct answers: {correct}")
print(f"Incorrect answers: {incorrect}")