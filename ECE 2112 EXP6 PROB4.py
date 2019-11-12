def Hangaroo(secretWord):
    
    print('WHAT IS THE SECRET WORD? GUESS A LETTER!')
    print('YOU HAVE 10 GUESSES')
    print('THE WORD HAS ' + str(len(secretWord)) + ' LETTERS')
    guess = ''
    lettersGuessed = []
    guessleft = 10

    while True: 
        
        guess = input()
        
        if guess in secretWord:
            if guess not in lettersGuessed:
                lettersGuessed += guess
                print(getGuessedWord(secretWord, lettersGuessed))
                guessleft -= 1
                print("YOU HAVE "  + str(guessleft) + " GUESSES LEFT!")
                
            elif guess in lettersGuessed:
                print("YOU ALREADY GUESSED THAT LETTER! TRY AGAIN!")
                lettersGuessed += guess
                print(getGuessedWord(secretWord, lettersGuessed))
                guessleft -= 1
                print("YOU HAVE "  + str(guessleft) + " GUESSES LEFT!")
                
        elif guess not in secretWord:
            if guess in lettersGuessed:
                print("YOU ALREADY GUESSED THAT LETTER! TRY AGAIN!")
                lettersGuessed += guess
                print(getGuessedWord(secretWord, lettersGuessed))
                guessleft -= 1
                print("YOU HAVE "  + str(guessleft) + " GUESSES LEFT!") 
            else:
                print("SORRY! WRONG GUESS!")
                lettersGuessed += guess
                print(getGuessedWord(secretWord, lettersGuessed))
                guessleft -= 1
                print("YOU HAVE "  + str(guessleft) + " GUESSES LEFT!")
        
        if guessleft <= 0:
            print("SORRY! YOU LOST!")
            print("THE SECRET WORD WAS " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print("CONGRATULATIONS! YOU WON!")
            break
                