

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