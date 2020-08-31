from ActivityAnalysis import gymActivities
from ActivityAnalysis import trainingAndSport
from ActivityAnalysis import outdoorActivities
from ActivityAnalysis import homeAndDailyActivities
from ActivityAnalysis import homeRepairActivities
from ActivityAnalysis import occupationalActivities



# Making a trie structure for the keyword search
# This class will contain the structure of a node
class trieNode:
    def __init__(self):
        self.index = 0     #A unique index which identifies a word that ends on a node
        self.charsInChildren = set()  #A set which holds all the characters that are children of the node
        self.wordEnd = False     #Will be true if a word ends at this node.
        self.nextNodes = {}  #Will be a dictionary containing a character as the key and next node as the value


#Insert a new word into the trie structure
def insertInTrie(root,activityName,activityIndex):
    insertHelper = root
    activityName = activityName.lower()
    for letter in activityName:

        #If a new node is required for the character
        if letter not in insertHelper.charsInChildren:
            newNode = trieNode()
            insertHelper.nextNodes[letter] = newNode
            insertHelper.charsInChildren.add(letter)

        #traversing to the next node
        insertHelper = insertHelper.nextNodes[letter]



    #Adds the index at the final node and marks the end of a word
    insertHelper.wordEnd = True
    insertHelper.index = activityIndex


#Function which finds the words in the trie that match the keyword
#All the indices of words that come under a node are stored in indexCache
def findWords(node, indexCache):
    if node.wordEnd == True:
        indexCache.append(node.index)

    if len(node.charsInChildren) != 0:
        for character in node.charsInChildren:
            findWords(node.nextNodes[character], indexCache)

#Function which returns the node that a search term leads to
def traverseTrie(root, keyword):
    currentNode = root
    i = 0
    nodeFound = False
    while i<len(keyword) and not nodeFound:
        if keyword[i] in currentNode.nextNodes:
            currentNode = currentNode.nextNodes[keyword[i]]
            i+=1
        else:
            nodeFound = True

    return currentNode



#Populating the trie structure
trieRoot = trieNode()
index = 0

for activity in gymActivities:
    insertInTrie(trieRoot,activity,index)
    index += 1

index = 100
for activity in trainingAndSport:
    insertInTrie(trieRoot,activity,index)
    index += 1

index = 200
for activity in outdoorActivities:
    insertInTrie(trieRoot,activity,index)
    index += 1

index = 300
for activity in homeAndDailyActivities:
    insertInTrie(trieRoot,activity,index)
    index += 1

index = 400
for activity in homeRepairActivities:
    insertInTrie(trieRoot,activity,index)
    index += 1

index = 500
for activity in occupationalActivities:
    insertInTrie(trieRoot,activity,index)
    index += 1










