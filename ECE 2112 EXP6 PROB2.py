def getGuessedWord(secretWord, lettersGuessed):
    
    z = ''
    
    for x in secretWord:
        
        if x not in lettersGuessed:
            z = z + '_'
            
        else:
            z = z + x
            
    return z