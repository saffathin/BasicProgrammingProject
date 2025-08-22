TEXT ANALYSIS AND EXPLORATION + SENTENCE GUESSING GAME PROJECT, by Saffanah Fathin

This project is divided 3 main parts, including:
File 1. "data_exploration.ipynb"
File 2. "data_processing.ipynb"
File 3. "main.py"

General Description of Each File

FILE 1 - THE DATA EXPLORATION
Name of file: data_exploration.ipynb

This file reports on the statistical exploration of the corpus data by using python scripts. 
It gives information on: (1) 100 most frequent words and its bar plot; (2) words appear less than 10 times and a word cloud of them; 
(3) the distribution of POS tags and the plot; and (3) the distribution of sentence length and its plot. 
Most of the codes are taken and adapted from the project tools provided.

FILE 2 - THE DATA PROCESSING AND FILTERING
Name of file: data_processing.ipynb

This file consists of codes in which the corpus data is being filtered to so that it is suitable for the sentence guessing game. The filtering process inlcude:
1. Eliminating sentences that are too long and too short
2. Eliminating sentences that contain rare words
3. Removing punctuations from the sentences
4. Further filtering for unsuitable sentences

There are two txt files generated: 
(1) dataforgame.txt, which is the main sentences dataset;
(2) data_words_text.txt, which contains lists of words from the corpus to be used as the 3rd hint (getting the words from similar context).

FILE 3 - THE SENTENCE GUESSING GAME
Name of file: main.py

The game is based on Python and takes an input from users in the form of English words.

Description
In this sentence guessing game, user will be given a randomly generated sentence with up to 20 words. 
The sentences were taken from a corpus that previously has been filtered and stored into a txt file.
There are two data (txt files) that are important for this game, hence might be best to be placed in the same folder path. 
The player must then guess each word in the sentence, in order, at a time. Player cannot quit until each word in the sentence in revealed. 
After finishing the game,player will be asked to press enter then the score will be displayed. The user can play the game again by running the py file.

Rules
1. Player will be given 5 turns to guess per each word.
2. 3 hints are available for each word and can be asked by pressing ? during the turn.
3. Asking for a hint is counted as a turn.
4. If the player cannot guess the word even after the 5th turn, the correct word will be revealed
5. Scores: 30 for guessing the word without help of hints, 20 with 1 hint, 15 with 2 hints, and 10 with 3 hints asked.
6. -10 score will be given per each word if player fails to guess after 5 turns
7. The score will be revealed in the end of the game

Note: this game is still not perfect because the condition of the sentences. Some sentences are only a clause/phrase. 
Some others contain numbers. While several of sentences have duplicate negation with apostrophe that is yet to be regulated. 
Furthermore, the first hint regarding the Part of Speech may use abbreviation that might not be friendly to some users.

List of libraries that are used in the game (some packages may need to be priorly downloaded):
- random
- nltk, word_tokenize
- nltk, pos_tag, tagset = "universal"
- nltk, Text
- io
- contextlib