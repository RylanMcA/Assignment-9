import sys
import operator
# Used a LOT documentation from w3schools.com/python


#argv[0] is the name of this python file
cmdStoryFile = sys.argv[1]
cmdSkipFile = sys.argv[2]
print("The story: %s" % cmdStoryFile)
print("The skip-file: %s" % cmdSkipFile)


#open files and set all text to lower case
with open(cmdStoryFile, 'r') as storyFile:
    storyContent = storyFile.read()

with open(cmdSkipFile, 'r') as skipFile:
    skipContent = skipFile.read()


#Remove uppercase letters and 
#split the skip-words since thats all do to it
storyContent = storyContent.lower()
skipContent = skipContent.lower()
skipArray = skipContent.split(",",-1)


#Printing words skipped
print("Words skipped: [", end="")
print(*skipArray, sep=",", end="")
print("]")


#replacment loop for easures
erasures = ['\n','\t','.','?','!',',',';',':','\'','\"']
for x in erasures:
    if( x == "'"):
        storyContent = storyContent.replace(x,"")
    else:
        storyContent = storyContent.replace(x," ")


#split the story string into the array
#remove the needed words
storyArray = storyContent.split()
storyArray.pop() #Theres some weird end of file stuff in emperor3.txt
for x in skipArray: #Get a value from skip 
    while(storyArray.count(x) > 0 ):
        storyArray.remove(x)


#Create dictonary. It's like a Hash Table!
#Create pairs of words. 
#So each word has a pair with the word to the left and one to the right. 
# ex. {word1 word2 word3 ... wordN, wordN+1} so we have word1+word2, word2+word3, ... , wordN+wornN+1
storyConsecutiveDictonary = {}
i = 0
while(i < (len(storyArray)-1)):
    if storyArray[i]+" "+storyArray[i+1] in storyConsecutiveDictonary:
        storyConsecutiveDictonary[ storyArray[i]+" "+storyArray[i+1] ] += 1
    else:
        storyConsecutiveDictonary[ storyArray[i]+" "+storyArray[i+1] ] = 1
    i += 1


#This is now sorted from SMALLEST to LARGEST
#Since we're small to large, we need to
#grab the last 5 elements in the dictronary
storySortedCount = sorted(storyConsecutiveDictonary.items(), key=operator.itemgetter(1))
print("The 5 most common word pairs in", cmdStoryFile)
i=1
while(i <= 5): #1-5
    print(storySortedCount[len(storySortedCount)-i])
    i += 1

input()
