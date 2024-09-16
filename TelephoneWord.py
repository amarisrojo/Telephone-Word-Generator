"""
script: Telephone Word Generator
action: Allows user to enter phone number and receive every possible word outcome
author: Amaris Rojo
date: 09/14/2024
"""

# Create a tuple full of lists for number/letter correlation
myLetters = ([],
             [],
             ['A','B','C'],
             ['D','E','F'],
             ['G','H','I'],
             ['J','K','L'],
             ['M','N','O'],
             ['P','R','S'],
             ['T','U','V'],
             ['W','X','Y']
             )

def generateWords(number):
    """
    action:a loop to generate each word
    input: none
    output: none
    return: list of possible word combinations
    """
    # if no response is given
    if len(number) == 0:
        return ['']
    
    # set first digit as the number in the index 0, set as int
    digit1 = int(number[0])
    
    # repeat for the rest of the numbers
    restOfNumber = number[1:]
    
    wordsForRest = generateWords(restOfNumber)
    
    # declare result variable
    result = []

    # for statement, to add on to each letter
    for letter in myLetters[digit1]:
        for word in wordsForRest:
            result.append(letter + word)
    
    return result

def main():
    """
    action: ask for number, display possible outcomes
    input: phone number
    output: total list of possible outcomes
    return: none
    """

    # ask for number
    phoneNum = input('Please enter a 7-digit phone number: ')
    

    # pass phone number into the looping function
    words = generateWords(phoneNum)
    
    # display message and all possible outcomes
    print(f"All possible 7-letter word combinations for {phoneNum}:")
    for word in words:
        print(word)
    

# call main 
if __name__ == "__main__":
    main()
    