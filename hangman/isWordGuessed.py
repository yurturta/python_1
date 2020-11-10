# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 02:13:21 2017

@author: yurtaturta
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count=0
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            count+=1
    if count==len(secretWord):
        return True
    else:
        return False
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word=[]
    result=''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            word.append(secretWord[i])
        else:
            word.append('_')
    for i in word:
        if i=='_':
            result+=i
            result+=' '
        else:
            result+=i
    return result
    
    
import string   
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a=string.ascii_lowercase
    word=[]
    for i in a:
        if i not in lettersGuessed:
            word.append(i)
    result=''.join(word)
    return result
    
    
    
























    