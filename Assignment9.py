import sys
import operator

#argv[0] is the name of this python file
cmdStoryFile = sys.argv[1]
cmdSkipFile = sys.argv[2]

print("The story %s" % cmdStoryFile)
print("The skip file %s" % cmdSkipFile)

#open files and set all text to lower case
with open(cmdStoryFile, 'r') as storyFile:
    storyContent = storyFile.read()

with open(cmdSkipFile, 'r') as skipFile:
    skipContent = skipFile.read()

storyContent = storyContent.lower()
skipContent = skipContent.lower()
skipArray = skipContent.split(",",-1)

#replacment loop for easures
erasures = ['\n','\t','.','?','!',',',';',':','\'','\"']
for x in erasures:
    if( x == "'"):
        storyContent = storyContent.replace(x,"")
    else:
        storyContent = storyContent.replace(x," ")

storyArray = storyContent.split()
storyArray.pop()


for x in skipArray: #Get a value from skip 
    while(storyArray.count(x) > 0 ):
        storyArray.remove(x)


print(storyArray)

input()