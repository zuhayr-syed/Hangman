# Decription: Hangman game where the user attempts to guess the letters of a word with limited lives

import random #Import random
from easygui import * #Import easygui

def blankLine (): #Define blankLine()
    print (" ") #Prints space

print ("\t\t\t\t\t Hangman") #Displays title 'Hangman'

blankLine () #Space
msgbox ("Guess the letters of a word before you run out of guesses") #Tells user instructions
blankLine () #Space

def game (): #Creates a menu function.
    blankLine () #Space
    message = ("Would you like to continue or quit?") #Asks user if they want to continue or quit
    choices = ["Continue", "Quit"] #User options
    reply = buttonbox (message, choices=choices) #Displays buttonbox
    if reply == "Quit": #Let's user leave if they choose to
        quit ()  #Ends the program
    blankLine () #Space

while game () != 'Q': #When the user chooses to continue
   
    words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
            "computer", "python", "program", "glasses", "sweatshirt",
            "sweatpants", "mattress", "friends", "clocks", "biology",
            "algebra", "suitcase", "knives", "ninjas", "shampoo",
            "service", "computers", "jawbreaker", "microwave",
            "syndrome", "pneumonia", "xylophone", "zigzagging"] #All the possible words for hangman

    word = random.choice(words) #Chooses random word from the word bank
    reply = None # will hold the players guess
    letters = [] # a list of letters guessed so far
    term = [] #Term is what appears on screen with both the "_ ", and the correct letters that replace the blanks
    for letter in word: #For loop for the correct letters in the word
        term.append("_ ") # create an unguessed, blank version of the word
    joined = None # joins the words in the list term

    HANGMAN = (\
"""

""", #Provides a space for every life of hangman: life 8 (where the image appears)
"""

""", #Provides a space for every life of hangman: life 7 (where the image appears)
"""

""", #Provides a space for every life of hangman: life 6 (where the image appears)
"""

""", #Provides a space for every life of hangman: life 5 (where the image appears)
"""

""", #Provides a space for every life of hangman: life 4 (where the image appears)
"""

""", #Provides a space for every life of hangman: life 3 (where the image appears)
"""

""", #Provides a space for every life of hangman: life 2 (where the image appears)
"""

""", #Provides a space for every life of hangman: life 1 (where the image appears)
"""

""") #Hangman pictures

    print(HANGMAN[0]) #Print picture of the hangman
    attempts = len(HANGMAN) - 1 #For every wrong guess, the next hangman picture appears


    while (attempts != 0 and "_ " in term): #While attempts does not equal to zero, and the word is not completely guessed
        blankLine () #Space
        joined = "".join(term) #Joins letters with the blanks
        blankLine () #Space
           
       
        statement = ("PICK A LETTER \n ----> You have guessed the letters: ",(' '.join(letters)), "\n\n\t ", (joined)) #Tells the statement to the user and tells which letters already guessed
        title = "Hangman" #Title
        choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] #Gives the user the choices of letters to choose from
        reply = buttonbox (statement, title, choices=choices) #Displays the buttonbox                
 
        if reply in letters: #Checks if the letter hasn't been guessed already
            msgbox ("You have already guessed that letter, try again.") #Tells user that they have tried that guess already
            continue #Continue loop

        letters.append(reply) #This displays the letters already guessed and ensures that the number of attempts does not decrease for the same guess

        for letter in range (len(word)): #For the letters that are guessed that are in the word
            if reply == word[letter]: #If the guess is in the word
                term[letter] = reply #Replaces all letters in the chosen word that match the players guess
                print ("CORRECT") #Tells the user that they are correct

        if reply not in word: #If the user's guess is not in the word
            attempts -= 1 #Subtracts an attempt when wrong
            print ("INCORRECT") #Tells the user that they are wrong
            print(HANGMAN [(len(HANGMAN) - 1) - attempts]) #For every wrong attempt the next hangman picture is shown in order

            if attempts == 7: #When user has 7 attempts remaining
                image = "C:\Zuhayr\Code/stand.gif" #Prints specific image of hangman
                msg = ("INCORRECT", '\n -----> Attempts remaining: ', int(attempts)) #Tells user that they are incorrect and displays their remaining attempts
                choices = ["Continue"] #Continue option
                reply = buttonbox(msg, image=image, choices=choices) #Displays the buttonbox

            if attempts == 6: #When user has 6 attempts remaining
                image = "C:\Zuhayr\Code/rope.gif" #Prints specific image of hangman
                msg = ("INCORRECT", '\n -----> Attempts remaining: ', int(attempts)) #Tells user that they are incorrect and displays their remaining attempts
                choices = ["Continue"] #Continue option
                reply = buttonbox(msg, image=image, choices=choices) #Displays the buttonbox

            if attempts == 5: #When user has 5 attempts remaining
                image = "C:\Zuhayr\Code/head.gif" #Prints specific image of hangman
                msg = ("INCORRECT", '\n -----> Attempts remaining: ', int(attempts)) #Tells user that they are incorrect and displays their remaining attempts
                choices = ["Continue"] #Continue option
                reply = buttonbox(msg, image=image, choices=choices) #Displays the buttonbox

            if attempts == 4: #When user has 4 attempts remaining
                image = "C:\Zuhayr\Code/body.gif" #Prints specific image of hangman
                msg = ("INCORRECT", '\n -----> Attempts remaining: ', int(attempts)) #Tells user that they are incorrect and displays their remaining attempts
                choices = ["Continue"] #Continue option
                reply = buttonbox(msg, image=image, choices=choices) #Displays the buttonbox

            if attempts == 3: #When user has 3 attempts remaining
                image = "C:\Zuhayr\Code/left arm.gif" #Prints specific image of hangman
                msg = ("INCORRECT", '\n -----> Attempts remaining: ', int(attempts)) #Tells user that they are incorrect and displays their remaining attempts
                choices = ["Continue"] #Continue option
                reply = buttonbox(msg, image=image, choices=choices) #Displays the buttonbox

            if attempts == 2: #When user has 2 attempts remaining
                image = "C:\Zuhayr\Code/right arm.gif" #Prints specific image of hangman
                msg = ("INCORRECT", '\n -----> Attempts remaining: ', int(attempts)) #Tells user that they are incorrect and displays their remaining attempts
                choices = ["Continue"] #Continue option
                reply = buttonbox(msg, image=image, choices=choices) #Displays the buttonbox

            if attempts == 1: #When user has 1 attempts remaining
                image = "C:\Zuhayr\Code/left leg.gif" #Prints specific image of hangman
                msg = ("INCORRECT", '\n -----> Attempts remaining: ', int(attempts)) #Tells user that they are incorrect and displays their remaining attempts
                choices = ["Continue"] #Continue option
                reply = buttonbox(msg, image=image, choices=choices) #Displays the buttonbox

            if attempts == 0: #When user has 0 attempts remaining
                image = "C:\Zuhayr\Code/right leg.gif" #Prints specific image of hangman
                msg = ("INCORRECT", '\n -----> YOU LOST') #Tells user that they are incorrect and lost
                choices = ["Continue"] #Continue option
                reply = buttonbox(msg, image=image, choices=choices) #Displays the buttonbox

    if "_ " not in term: #When there are no blanks remaining in the word
        msgbox ("You win, you guessed the word") #Tells user that they have won

    else: #When there are still blanks when no attempts remain
        msgbox ("You lose, you did not guess the word. The word was:") #Tells user that they lose and did not guess the word
        msgbox (str(word)) #Displays the correct word
