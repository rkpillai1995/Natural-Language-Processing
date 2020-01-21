__author__ = 'Rajkumar Pillai'
import operator
import math
import  matplotlib.pyplot as plt
from scipy import  stats
import re
"""
Description: This program implements the Zip's Law and Heap's Law on three text files and plots the result
"""

def ReadingWordsInDictionary(f):
    '''
    This function reads the words of the text files into Dictionary.Words are keys and the value is list of length 2.
    The list stores the frequency and rank of the word.
    :param f: The file object
    :return: DictionaryOfWords: The Dictionary of the words in text file
    '''

    DictionaryOfWords = dict()

    f1 = f.read() #Reading the file

    wordslist=re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', f1) # Using Regular Expression to consider only the relevant words from text

    Allwords=[]  ## List to store all the words
    for word in wordslist:
        Allwords.append(word.lower())     #Converting the words into lower case
    for word in Allwords:
        templist=[]

        ## To make sure only every word is considered
        if word not in DictionaryOfWords:
            DictionaryOfWords[word] = [1]
        else:

            ## To keep track of frequency of words
            templist=DictionaryOfWords[word]
            templist[0]+=1
            DictionaryOfWords[word]=templist
    return DictionaryOfWords


def ReadingWordsForHeapsLaw(f):
    '''
    This function reads the unique words which can be usedfor heap's law
    :param f: The file object
    :return:TotalUniqueWords,TotalNoOfWords: The total no of unique words and total no of words
    '''
    f1 = f.read() # Reading file

    wordslist = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', f1) # Using Regular Expression to consider only the relevant words from text file
    UniqueWords = []  # List to store unique words

    TotalNoOfWords=len(wordslist)  # To store total no of words in text file which are considered
    Allwords = [] ## List to store all the words

    for word in wordslist:
        Allwords.append(word.lower())    #Converting the words into lower case

    for word in Allwords:
        templist = []
        ## To make sure only every word is considered only once
        if word not in UniqueWords:
            UniqueWords.append(word)
    TotalUniqueWords=len(UniqueWords)

    return TotalUniqueWords,TotalNoOfWords



def RankingtheWords(DictionaryOfWords):
    '''
    This function ranks the words according to their frequency
    :param DictionaryOfWords:  The Dictionary of the words in text file
    :return: DictionaryOfWords
    '''

    rank=0

    ## Iterating through word and ranking them by frequency
    for keys, values in sorted(DictionaryOfWords.items(), key=operator.itemgetter(1), reverse=True):
        rank+=1
        templist=DictionaryOfWords[keys]
        templist.append(rank)
        DictionaryOfWords[keys]=templist
    return DictionaryOfWords


def FindingLogOfFrequencyAndRank(DictionaryOfWords):
    '''
    Computing the log to the base 10 value of rank and frequency of every word
    :param DictionaryOfWords:   The Dictionary of the words in text file
    :return: Log10Frequency,Log10Rank
    '''

    Log10Rank=[]
    Log10Frequency = []
    for keys,values in DictionaryOfWords.items():
        templist=DictionaryOfWords[keys]
        Log10Frequency.append(math.log10(templist[0]))
        Log10Rank.append(math.log10(templist[1]))

    return Log10Frequency,Log10Rank

def plottingZipsLaw(Log10Frequency,Log10Rank,f):
    '''
    This function plots the result computed using Zip's Law
    :param Log10Frequency: Log base 10 value of frequency
    :param Log10Rank: Log base 10 value of Rank
    :param f: The file object
    :return:
    '''

    # Plotting the words in decreasing order of frequency
    plt.scatter(Log10Rank, Log10Frequency, color='b')

    ## To plot the linear regression line for the plot
    slope,intercept,_,_,_=stats.linregress(Log10Rank,Log10Frequency)
    line=[]
    for i in range(len(Log10Frequency)):
        line.append(slope*Log10Frequency[i]+intercept)
    plt.plot(line,Log10Frequency,color='r')


    ## Labeling the plot
    plt.tick_params(axis='y',labelleft=True)
    plt.tick_params(axis='x',labelbottom=True)
    plt.xlabel("log10(rank)", fontsize='x-large')
    plt.ylabel("log10(frequency)", fontsize='x-large')
    plt.title("Zipf's Law "+f+".txt", fontsize='x-large')
    plt.savefig(f+".png")
    plt.show()





def plottingHeapsLaw(Log10Unique,TotalNoofWords):
    '''
    This function plots the result computed using Heap's Law
    :param Log10Unique: Log base 10 value of UniqueWords
    :param TotalNoofWords: Total no of words in file
    :return:
    '''

    ## Computing Log base 10 value of the total no of words in file
    Log10Words = []
    for i in range(len(TotalNoofWords)):
        Log10Words.append(math.log10(TotalNoofWords[i]))

    ## Plotting the result
    plt.scatter(Log10Words, Log10Unique, color='b')

    ## To plot the linear regression line for the plot
    slope,intercept,_,_,_=stats.linregress(Log10Words,Log10Unique)
    line=[]
    ## Using the Heap's law
    b=slope
    k=math.pow(10,intercept)
    for i in range(len(TotalNoofWords)):
        line.append(math.log10(k*math.pow(TotalNoofWords[i],b)))
    plt.plot(Log10Words, line,color='r')


    ## Labeling the plot
    plt.tick_params(axis='y',labelleft=True)
    plt.tick_params(axis='x',labelbottom=True)
    plt.xlabel("log10(words)", fontsize='x-large')
    plt.ylabel("log10(ditinct)", fontsize='x-large')
    plt.title("Heap's Law", fontsize='x-large')
    plt.savefig("Heap's Law.png")
    plt.show()





def main():
    '''
    The main function
    :return:
    '''


    ListOfFileNames=["Dracula","HoundBaskervilles","WarAndPeace"]

    ## To iterate through all files and producing result for Zip's Law
    for files in ListOfFileNames:
        f=open(files+".txt","r+",encoding='utf-8-sig')
        print("Plotting Zipf's Law for "+files+".txt")
        DictionaryOfWordsForZipsLaw=ReadingWordsInDictionary(f)
        DictionaryOfWordsForZipsLaw=RankingtheWords(DictionaryOfWordsForZipsLaw)
        Log10Frequency, Log10Rank=FindingLogOfFrequencyAndRank(DictionaryOfWordsForZipsLaw)
        plottingZipsLaw(Log10Frequency,Log10Rank,files)

    ## To iterate through all files and producing result for Heap's Law
    ListOfTotalUniqueWords=[]
    ListOfTotalNoOfWords = []
    print("Plotting Heap's Law")
    for files in ListOfFileNames:
        f = open(files + ".txt", "r+", encoding='utf-8-sig')
        TotalUniqueWords, TotalNoOfWords=ReadingWordsForHeapsLaw(f)
        ListOfTotalUniqueWords.append(math.log10(TotalUniqueWords))
        ListOfTotalNoOfWords.append((TotalNoOfWords))
    plottingHeapsLaw(ListOfTotalUniqueWords,ListOfTotalNoOfWords)

if __name__ == '__main__':
    main()