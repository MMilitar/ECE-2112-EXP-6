def isWordGuessed(secretWord, lettersGuessed):
    
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True