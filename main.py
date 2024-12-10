

def isWordValid(word, boardSides):
    """
    Checks if a word is valid:
    No consecutive letters from same side.
    Uses letters only presented by the board.
    """

    for letterIndex in range(len(word) - 1):
        for side in boardSides:
            if word[letterIndex] in side and word[letterIndex + 1] in side:
                return False
    return True

def readWords(dictionaryFile, allLetters):
    """
    Reads and filters word from the dictionary file to only include words
    that can be formed with the given board letters, and of length three.
    """

    with open(dictionaryFile, "r",) as file:
        dictionary = [line.strip().upper() for line in file]

    # Remove words with less than three letters
    dictionary = [word for word in dictionary if len(word) >= 3 and set(word).issubset(set(allLetters))]
    return dictionary





def backtrackFunction(boardSides, dictionary, usedWords, currentWord, usedLetters, allLetters):
    """
    Function that implements backtracking to find the solution that uses 
    the fewest amount of words.
    """

    # All letters have been used
    if set(usedLetters) == set(allLetters): 
        return usedWords

    for word in dictionary:
        if isWordValid(word, boardSides) and word[0] == currentWord[-1]: # Check if word is "drawn" correctly, and that the last letter is the first in new word
            newUsedLetters = usedLetters + list(word)
            newUsedWords = usedWords + [word]
            result = backtrackFunction(boardSides, dictionary, newUsedWords, newUsedLetters, allLetters)

            if result:
                return result
            
    return None


if __name__ == "__main__":
    # Input data
    sides = [
        "WMSY",  # Letters on each side of the square
        "TLOR",
        "HNID"
    ]
    dictionary_file = "dictionary.txt"  # Path to the dictionary file

    # Solve the puzzle
    solution = solveLetterBoxed(sides, dictionary_file)

    # Output the solution
    if solution:
        print(f"Solution: {' -> '.join(solution)}")
    else:
        print("No solution found.")

