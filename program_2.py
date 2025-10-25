# David Stalmakov, 10/23/2025
# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here
    # Add a space
    for char in sentence:
        if char.isupper() and new_sentence:
            new_sentence += " " + char
        else:
            new_sentence += char

    # Lowercase the rest of the words
    new_sentence = new_sentence.lower()
    if new_sentence:
        new_sentence = new_sentence[0].upper() + new_sentence[1:]
    new_sentence += "."

    return new_sentence.strip()

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)