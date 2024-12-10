

def isValidWord(word, boardSides):
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

def loadDictionary(dictionaryFile, allLetters):
    """
    Reads and filters word from the dictionary file to only include words
    that can be formed with the given board letters, and of length three.
    """

    with open(dictionaryFile, "r",) as file:
        dictionary = [line.strip().upper() for line in file]

    # Remove words with less than three letters
    dictionary = [word for word in dictionary if len(word) >= 3 and set(word).issubset(set(allLetters))]
    return dictionary


def backtrackFunction(boardSides, dictionary, usedWords, currentWord, usedLetters, allLetters, maxWords = 5):
    """
    Function that implements backtracking to find a solution.
    """

    # All letters have been used
    if set(usedLetters) == set(allLetters): 
        return usedWords
    
    if len(usedWords) >= maxWords:
        return None

    for word in dictionary:
        if word[0] == usedWords[-1][-1]: # Next word must start with last word's last letter
            # Ensure that the word is valid and hasn't been used already
            if isValidWord(word, boardSides) and word[0] and word not in usedWords:
                newUsedLetters = usedLetters | set(word)
                newUsedWords = usedWords + [word]
                result = backtrackFunction(boardSides, dictionary, newUsedWords, word, newUsedLetters, allLetters)

                if result:
                    return result       
    return None


def solveLetterBoxedDFS(boardSides, dictionaryFile):
    """
    Solves the Letter Boxed using DFS with a maxiumum word constraint.
    """

    print("Started solution searching")

    allLetters = "".join(boardSides)
    dictionary = loadDictionary(dictionaryFile, allLetters)

    print("Finished reading dictionary")
    
    # Find solution using backtracking
    for word in dictionary:
        if isValidWord(word, boardSides):
            solution = backtrackFunction(boardSides, dictionary, [word], word, set(word), allLetters)

            if solution:
                return solution
    return None

def solveLetterBoxedBFS(boardSides, dictionaryFile):
    """
    Solve the Letter Boxed using BFS to find the solution with the fewest amount of words.
    """
    pass

if __name__ == "__main__":
    sides = [
        "AWH",
        "PTG",
        "NRC",
        "EYO"
    ]

    dictionaryFile = "dictionary.txt"  # Path to the dictionary file
    solution = solveLetterBoxedDFS(sides, dictionaryFile)

    if solution:
        print(f"Solution: {' -> '.join(solution)}")
    else:
        print("No solution found.")