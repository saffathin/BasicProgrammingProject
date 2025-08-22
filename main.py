# Python 3.10
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:49:30 2022

@author: Saffanah Fathin

This file contains the code script for sentence guessing game.
The data is taken from a corpus that is already stored in a txt file.
The sentence is choosen randomly.
Users have 5 chances in total to guess each word, 3 hints included.
When the game finishes, the user has the option to reveal the game score.

"""

#importing the data(filtered) from txt file for the game 
datafile = open("dataforgame.txt") 

#storing and converting the data into a list
list_data = [(line.strip()).split() for line in datafile]

#function will get one random sentence from the dataset
import random
sentence = random.choice(list_data)

#creating underscore for display of game
display = []
for word in sentence:
    display.append("_")

###############  POS DATA FOR HINT 1   #######################################
#import necessary library
from nltk import word_tokenize

#defining the function to get the POS of the word
def get_pos(word):
    """
    Get the part of speech of a given word.

    Parameters
    ----------
    word : str
        A word.
    text : nltk.word_tokenize

    Returns
    -------
    result : the last item of list, the part of speech only
    """
    text = word_tokenize(word)
    pair = nltk.pos_tag(text, tagset = 'universal') #tagset is set to be universal
                                                    #might need to be downloaded first
    for item in pair:
        for i in item:
            i.strip()
    return i.lower()


####### SIMILAR CONTEXT WORD FOR HINT 3 #####################################
#importing necessary library
import io
from contextlib import redirect_stdout
import nltk

#opening the stored file contained list of data from the corpus
f = open('data_words_text.txt','r', encoding='UTF-8')
fill = f.read()
tokens = nltk.word_tokenize(fill)
text = nltk.Text(tokens) #convert the data into Text

#defining the function to get words in similar context
def get_similar(word, text):
    """
    Get words similar to a given word based on its context in a corpus.

    Parameters
    ----------
    word : str
        A word.
    text : nltk.text.Text
        A corpus as a nltk Text object.

    Returns
    -------
    result : list
        A list of words occuring in similar contexts, or an empty list if no results were found.]

    """
    with io.StringIO() as f, redirect_stdout(f):
        text.similar(word, num=5) #printing 5 words
        result = f.getvalue().replace('\n', ' ').strip(' ').split(' ')
        if result == ['No', 'matches']:
            result = []
        else:
            result = f"'{result[0]}', '{result[1]}', '{result[2]}', '{result[3]}', and '{result[4]}'"
    return result

#set the initial score
score = 0

#empty prompt
prompt = ""

######################## WELCOME MESSAGE #####################################
print("Welcome to the sentence guessing game! Your challenge is to guess the word and complete the sentence.")
print("You have 5 tries for each word and can press ? for hint.")

#begin prompt for user
ready_input = input('Press enter to play:') # prompt user to enter any key, or write quit

if ready_input == "": #if user press enter, the game will proceed
        
    print(f"The sentence has {len(sentence)} words. What's the first one?")
    
    print(*display, sep = " ") 
    
    #++++++++++++++++++++++ MAIN GAME +++++++++++++++++++++++++++++++++++++++
    for i in range(0,len(sentence)-1): #for first word until the word before the last
        turn = 5 #number of turn for each word
        hint = 3 #the number of hints for each word
        
        while turn > 0:
            guess = input("Your guess:")
            
            #to make sure user input is not alphabet and lowercase,no empty string
            guess = guess.lower()
            
            #condition for hints
            if guess == '?':
                turn -= 1 #hint will be counted as losing one turn
                hint -= 1
                if hint<0: #if the user asks for more than 3 hints
                    print("No more hint!")
                elif hint == 2:
                    print(f"Hint 1: This word is a {get_pos(sentence[i])} and it contains {len(sentence[i])} letters.")
                elif hint == 1:
                    print(f"Hint 2: This word start with {sentence[i][0]} and ends with {sentence[i][-1]}.")
                elif hint == 0:
                    print(f"Hint 3: Words in similar contexts are {get_similar(sentence[i], text)}.")
                    
            elif guess == sentence[i]: #if the user guess matches with the word
                turn -= 1
                display[i] = guess
                print(*display, sep = " ") 
                success = prompt.replace("", "Great! What is the next word?")
                print(success)
                
                #determining the score 
                if hint==3:
                    score+=30
                elif hint==2:
                    score+=20
                elif hint==1:
                    score+=15
                elif hint==0:
                    score+=10
                break
            
            else:#condition for wrong guess
                turn -= 1
                wrong = prompt.replace("", "Wrong! Try again or press ? for hint.")
                print(wrong)
                continue
        
        if turn == 0: #condition when user still cant guess correctly after 5 attempts
            if guess != sentence[i]:     
                score -=10
                display[i] = sentence[i] #the correct word will be revealed
                print(*display, sep = " ") #change list into a string
        
        continue
    
    #game for last word only
    for i in sentence[-1]:
        turn = 5 #set the turn for each word
        hint = 3 #set the number of hints for each word
        
        while turn > 0:
            guess = input("Your guess:")
            
            #to make sure user input is lowercase
            guess = guess.lower()
            
            #condition for hints
            if guess == '?':
                turn -= 1
                hint -= 1
                if hint < 0: #if the user asks for more than 3 hints
                    print("No more hint!")
                elif hint == 2:
                    print(f"Hint 1: This word is a {get_pos(sentence[-1])} and it contains {len(sentence[-1])} letters.")
                elif hint == 1:
                    print(f"Hint 2: This word start with {sentence[-1][0]} and ends with {sentence[-1][-1]}.")
                elif hint == 0:
                    print(f"Hint 3: Words in similar contexts are {get_similar(sentence[-1], text)}.")
                    
            elif guess == sentence[-1]: #if the user guess matches with the word
                turn -= 1
                display[-1] = guess
                print(*display, sep = " ") 
                success = prompt.replace("", "Great!")
                print(success)
                
                #determining the score 
                if hint==3:
                    score+=30
                elif hint==2:
                    score+=20
                elif hint==1:
                    score+=15
                elif hint==0:
                    score+=10
                break
            
            else:#condition for wrong guess
                turn -= 1
                wrong = prompt.replace("", "Wrong! Try again or press ? for hint.")
                print(wrong)
                continue
        
        #condition for the last turn of the last word
        while turn == 1:
            guess = input("Your guess:")
            
            #to make sure user input is not alphabet and lowercase,no empty string
            guess = guess()
            
            #condition for hints
            if guess == '?':
                turn -= 1
                hint -= 1
                if hint<0: #if the user asks for more than 3 hints
                    print("No more hint!")
                elif hint == 2:
                    print(f"Hint 1: This word is a {get_pos(sentence[-1])} and it contains {len(sentence[i])} letters.")
                elif hint == 1:
                    print(f"Hint 2: This word start with {sentence[-1][0]} and ends with {sentence[-1][-1]}.")
                elif hint == 0:
                    print(f"Hint 3: Words in similar contexts are {get_similar(sentence[-1], text)}.")
                    
            elif guess == sentence[-1]: #if the user guess matches with the word
                turn -= 1
                display[-1] = guess
                print(*display, sep = " ") 
                success = prompt.replace("", "Great!")
                print(success)
                break
            
            else:#condition for wrong guess
                turn -= 1
                wrong = prompt.replace("", "Wrong!")
                print(wrong)
                continue
        
        if turn == 0 : #condition when user still cant guess correctly after 5 attempts
            if guess != sentence[-1]: 
                score -=10
                display[-1] = sentence[-1] #the correct word will be revealed
                print(*display, sep = " ") #change list into a string       
        break
    
    #printing the finish prompt when the game is finished        
    if display[-1] == sentence[-1]: 
        print('\n')
        print("Congratulation! You finish the game!")
        
    #score reveal option
    score_reveal = input("Press enter to reveal score:")

    if score_reveal == "": 
        print(f"Your score is {score}. See you next time!")
    else:
        print("Thanks for playing. See you next time!")
                
else: #if user input something else
    print("See you next time or reload the game to play")