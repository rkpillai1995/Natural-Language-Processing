__author__ = 'Rajkumar Pillai'
import operator
import math
import  matplotlib.pyplot as plt
from scipy import  stats
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from statistics import mean,stdev
import string
import nltk

"""
Description: This program reads sentences from text file then calculates mean,standard deviation,minimum,maximum length of sentences, 
performs POS tagging and generates parse trees.
"""


def ReadingSentences(f):
    '''
    This function reads the senteneces of .txt into sentence list
    :param f: The file object
    :return: Sentence_list : The list containing the sentences
    '''

    entiretext=""
    for lines in f.readlines():
        if lines.strip():
            entiretext+=(lines)

    ## Tokenizing using nltk package
    Sentence_list=sent_tokenize(entiretext)

    return Sentence_list


def Calcualting_length_0f_Sentences(Sentence_list):
    '''
    This function finds longest,shortest sentences along with their length and mean , standard deviation of each corpus
    :param Sentence_list:  The list containing the sentences
    :return: Sentence_list_for_POS: list of sentences with 10-15 words for POS tagging
    '''

    ##Initializing variables for computation
    Max_length_sentence=0
    max_sentence=""
    Min_length_sentence=999999999999999999999999999999
    min_sentence=""
    word_length_of_sentence=[]  ## To store number of words in each sentence
    Sentence_list_for_POS=[]    ## list of sentences with 10-15 words for POS tagging

    count=0 ## TO make sure only two sentences are choosen

    ## Tokenizing every word of sentence
    for sentence in Sentence_list:
        wordlist = word_tokenize(sentence)

        ## To remove punctuation from sentence
        wordlist=[''.join(character for character in word if character not in string.punctuation) for word in wordlist]
        wordlist=[word for word in wordlist if word]

        ##Computing length of longest sentence
        if len(wordlist)>Max_length_sentence:
            Max_length_sentence=len(wordlist)
            max_sentence=sentence

        ##Computing length of shortest sentence
        if len(wordlist)<Min_length_sentence:
            Min_length_sentence=len(wordlist)
            min_sentence=sentence

        ##Choosing two sentence for POS tagging
        if len(wordlist)>=12 and len(wordlist)<=13 and count!=2:
            Sentence_list_for_POS.append(sentence)
            count+=1

        ##To compute mean of corpus
        sum_of_length_words = 0
        for words in wordlist:
            sum_of_length_words+=1
        word_length_of_sentence.append(sum_of_length_words)




    ##Printing the results
    print("Mean: ",mean(word_length_of_sentence))
    print("Standard Deviation: ",stdev(word_length_of_sentence))
    print("Length of Longest sentence: ",Max_length_sentence)
    print("The Longest sentence:\n ",max_sentence)
    print("Length of shortest sentence: ",Min_length_sentence)
    print("The Shortest sentence: ", min_sentence)

    return Sentence_list_for_POS


def POS_Tagging(Sentence_list_for_POS):
    '''
    This function performs POS tagging of sentence and generates a parse tree
    :param Sentence_list_for_POS:  list of sentences with 10-15 words for POS tagging
    :return:
    '''

    ## Using nltk pos_tag for POS tagging of the sentences
    for sentence in Sentence_list_for_POS:

        ##Removing punctuations
        wordlist = word_tokenize(sentence)
        wordlist = [''.join(character for character in word if character not in string.punctuation) for word in wordlist]
        wordlist = [word for word in wordlist if word]
        print("The Selected Sentence for POS Tagging: ")
        print(sentence)
        print("Parts of speech tag:",pos_tag(wordlist))

        #######The below comments should be uncommented for display of parse trees
        #sentence_without_punctutation=" "
        #sentence_without_punctutation=sentence_without_punctutation.join(wordlist)
        #parser = CoreNLPParser(url='http://localhost:9000')
        #next(parser.raw_parse(sentence_without_punctutation)).pretty_print()





def main():
    '''
    The main function
    :return:
    '''

    ListOfFileNames=["Dracula","HoundBaskervilles","WarAndPeace"]
    ## To iterate through all files and producing results for each corpus

    for files in ListOfFileNames:
        f=open(files+".txt","r+",encoding='utf-8-sig')
        print("RESULTS FOR FILE "+files+".txt")

        Sentence_list=ReadingSentences(f)
        Sentence_list_for_POS=Calcualting_length_0f_Sentences(Sentence_list)
        POS_Tagging(Sentence_list_for_POS)


        #######The below comments should be uncommented for display of parse trees for corpus having one sentence from each text
        #New_corpus="We left in pretty good time 89 and came after nightfall to Klausenburgh There were several Mortimers but only one who could be our   visitor Our gracious sovereign recognizes his high vocation and will be true to it"
        #parser = CoreNLPParser(url='http://localhost:9000')
        #next(parser.raw_parse(New_corpus)).pretty_print()


if __name__ == '__main__':
    main()
