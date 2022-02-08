import random

SOMEWORDS = ['kanye','donda','music','award','jesus',
            'godly','beast','crazy','throne','power','mercy',
            'beard','track','album','apple','kylie',
            'storm','burna','first','canon','speak','voice',
            'magic','gamer','manly','super','great','daddy']

for word in SOMEWORDS: #making sure the words I put in the list are actually 5 letters long!
    if len(word) != 5:
        SOMEWORDS.remove(word)

secretword = random.choice(SOMEWORDS)
#need to figure out howt o make word hidden if im sending the code over
#maybe a browser site to run the code but not show the code
letteramount = len(secretword)
lines = ('_' * letteramount + '\n') * 5

print('')
print('')
print('WELCOME TO KANYORDLE')
print('Essentially...it\'s a worldle for all about your number one comfort, Kanye West.')

print(lines)




print('\n\nThe Kanyordle begins...\n\n')

cycleWords = ['first', 'second', 'third','fourth','fifth']
amountOfWins = 0

for wordlocation in range(len(cycleWords)):
    plugInWord = cycleWords[wordlocation]

    randomstopper = True
    while randomstopper:

        guess = input('Make your ' + plugInWord + ' guess:   ')
        guess = guess.lower()
        randomstopper = False #setting it to false immediately so it can keep cycling

        if guess.isalpha():
            if len(guess) == letteramount: #checking to see if the guess is the same amount of letters

                if secretword == guess: #if they EVEN DISCOVER THE WORD
                    print('\n\nHURRAYYYYYYY! You did it! You cracked the secret word.')
                    print('Here is your well-deserved combination for the lock to your puzzle box: ')
                    print('2-4-8\n')
                    exit() #if they crack the word three times, then the game exits and they get the code for lock


                else: #if they havent guessed the word entirely, do the two types of evaluations
                    secondSecretWord = secretword
                    sharedList = []

                    #---------EVAL ONE-------------
                    #FIRST LETTER
                    guessletter = guess[0]
                    wordletter = secondSecretWord[0]
                    if guessletter == wordletter:
                        print('\nTHE LETTER \'' + guessletter + '\' IS IN THE RIGHT SPOT') #maybe take all the remaining letters and append to a list,
                        print('(Your guess\'s first letter)\n')
                        sharedList.append(1)


                    #SECOND LETTER
                    guessletter = guess[1]
                    wordletter = secondSecretWord[1]
                    if guessletter == wordletter:
                        print('\nTHE LETTER \'' + guessletter + '\' IS IN THE RIGHT SPOT')
                        print('(Your guess\'s second letter)\n')
                        sharedList.append(2)


                    #THIRD LETTER
                    guessletter = guess[2]
                    wordletter = secondSecretWord[2]
                    if guessletter == wordletter:
                        print('\nTHE LETTER \'' + guessletter + '\' IS IN THE RIGHT SPOT')
                        print('(Your guess\'s third letter)\n')
                        sharedList.append(3)


                    #FOURTH LETTER
                    guessletter = guess[3]
                    wordletter = secondSecretWord[3]
                    if guessletter == wordletter:
                        print('\nTHE LETTER \'' + guessletter + '\' IS IN THE RIGHT SPOT')
                        print('(Your guess\'s fourth letter)\n')
                        sharedList.append(4)


                    #FIFTH LETTER
                    guessletter = guess[4]
                    wordletter = secondSecretWord[4]
                    if guessletter == wordletter:
                        print('\nTHE LETTER \'' + guessletter + '\' IS IN THE RIGHT SPOT')
                        print('(Your guess\'s fifth letter)\n')
                        sharedList.append(5)


                    #take out hte characters in tehs secondSecretWord and guess word that is in Sharedlist
                    loopCounter = 0
                    for item in sharedList:
                        letter = secondSecretWord[item-1-loopCounter]
                        secondSecretWord = secondSecretWord.replace(letter,'',1)
                        guess = guess.replace(letter,'',1)
                        loopCounter += 1


                    #the remains of the word guessed move onto next evalution...




                    #---------EVAL TWO-------------
                    #Checking if the rest of the letters, that aren't in the right spot, are IN THE WORD
                    for cycle in range(len(secondSecretWord)):
                        wordletter = secondSecretWord[cycle] #comparing eachletter in guess to remaining letters in secret word
                        for guesscycle in range(len(guess)):
                            guessletter = guess[guesscycle]
                            if wordletter == guessletter:
                                print('\nTHE LETTER \'' + guessletter + '\' IS IN SECRET WORD BUT NOT IN RIGHT SPOT\n') #TO DO, LEFT OFF HERE, add the cycle name
                                break







            else:
                print('')
                print('Please enter a word with the correct amount of letters.')
                print('')
                randomstopper = True


        else:
            print('')
            print('Please enter a WORD.')
            if len(guess) != letteramount:
                print('Please enter a word with the correct amount of letters.')
            print('')
            randomstopper = True


#maybe add that if they guess the word, they get a letter for the combination lock...play three times
    #add an else if you they dont finish in five tries,
    #add sorry you didnt get the word, here was the actual word, keep tyring, and must do this three times in this
    #RUNNING PROGRAM to get the key

#right now, if you win or just lose in the 5 given tries, you just run theprogram again and again
