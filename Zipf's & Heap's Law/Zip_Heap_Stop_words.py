__author__ = 'Rajkumar Pillai'
import operator
import math
import  matplotlib.pyplot as plt
from scipy import  stats
from matplotlib import style
import re


"""
CSCI-722 : Data Analytics Cognitive Comp
Author: Rajkumar Lenin Pillai
Description: This program implements the Zip's Law and Heap's Law on three text files and plots the result using the stop word list
"""

## Declaring the stop words
stopWords=set(['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'])



def ReadingWordsInDictionary(f):
    '''
    This function reads the words of the text files into Dictionary.Words are keys and the value is list of length 2.
    The list stores the frequency and rank of the word.
    :param f: The file object
    :return: DictionaryOfWords: The Dictionary of the words in text file
    '''
    DictionaryOfWords = dict()
    f1 = f.read()      #Reading the file


    wordslist=re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', f1) # Using Regular Expression to consider only the relevant words from text

    Allwords=[]    ## List to store all the words

    for word in wordslist:

        ## To ignore the words that are in the stop word list
        if word not in stopWords:
             Allwords.append(word.lower())  #Converting the words into lower case
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
    # To store  words which are not in stop words list
    NewWordsList=[]
    for words in wordslist:
        if words not in stopWords:
            NewWordsList.append(words)

    # List to store unique words
    UniqueWords = []
    TotalNoOfWords=len(NewWordsList)        # To store total no of words in text file which are considered
    Allwords = [] ## List to store all the words
    for word in NewWordsList:
        Allwords.append(word.lower())       # Converting the words into lower case
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
    Rank=[]
    Frequency=[]
    for keys,values in DictionaryOfWords.items():
        templist=DictionaryOfWords[keys]
        Log10Frequency.append(math.log10(templist[0]))
        Log10Rank.append(math.log10(templist[1]))
        Frequency.append(templist[0])
        Rank.append(templist[1])

    return Log10Frequency,Log10Rank,Frequency,Rank

def plottingZipsLaw(Log10Frequency,Log10Rank,f):
    '''
   This function plots the result computed using Zip's Law and the stop words list
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
    plt.plot(line, Log10Frequency,color='r')


    ## Labeling the plot
    plt.tick_params(axis='y',labelleft=True)
    plt.tick_params(axis='x',labelbottom=True)
    plt.xlabel("Log10(r)", fontsize='x-large')
    plt.ylabel("Log10(f)", fontsize='x-large')
    plt.title("Zipf's Law Stopwords "+f, fontsize='x-large')
    plt.savefig(f+"Stopwords.png")
    plt.show()


def plottingHeapsLaw(Log10Unique,TotalNoofWords):
    '''
    This function plots the result computed using Heap's Law
    :param Log10Unique: Log base 10 value of UniqueWords
    :param TotalNoofWords: Total no of words in file
    :return:
    '''

    ## Calculating log to base 10 of total no of words in each that are considered
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
    plt.xlabel("Log10(words)", fontsize='x-large')
    plt.ylabel("Log10(ditinct)", fontsize='x-large')
    plt.title("Heap's Law using StopWords list", fontsize='x-large')
    plt.savefig("Heap's Law Stop Words.png")
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
        print("Plotting Zipf's Law using StopWords list for "+files+".txt")
        DictionaryOfWordsForZipsLaw=ReadingWordsInDictionary(f)
        DictionaryOfWordsForZipsLaw=RankingtheWords(DictionaryOfWordsForZipsLaw)
        Log10Frequency, Log10Rank,Frequency,Rank=FindingLogOfFrequencyAndRank(DictionaryOfWordsForZipsLaw)
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
