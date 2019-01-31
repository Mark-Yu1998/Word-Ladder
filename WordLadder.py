import time

def buildSet(fileName = None):
    if fileName == None:
        return None
    inFile = open(fileName,'r')
    data = inFile.readlines()
    uniques = set()
    for elem in data:
        elem = elem.rstrip("\n")
        uniques.add(elem)
    inFile.close()
    return uniques


def findNeighbor(current,filtered):

    neighbor = []
    for i in range(len(current)):
        for char in range(ord('a'), ord('z') + 1):
            word = current[:i] + chr(char) + current[i + 1:]
            if word in filtered and word != current and filtered[word] == False:
                neighbor.append(word)

    return neighbor


def filter(data, start_word,target):

    filtered = set()
    if start_word.lower() not in data or target.lower() not in data or len(start_word) != len(target):
        return None
    if start_word == "" or target == "" or start_word == None or target == None:
        return None

    for key in data:
        if len(key) == len(start_word):
            filtered.add(key)

    return filtered

def ConstructTest(fileName = "pairs.txt"):
    inFile = open(fileName,"r")
    data = inFile.readlines()
    test = []
    for case in data:
        test.append(case.strip("\n").split(" "))

    return test

def BuildLadder(start, target, wordList):
    # If the start word and end word are the same
    if start == target:
        return [start, target]
    # Queue to keep track of all the possible path
    queue = [[start]]
    # Keep track of the visited word

    visited = set()
    done = False
    ladder = None

    while (len(queue)) and (not done):
            # remove the first element
            current = queue.pop(0)
            lastElem = current[len(current) - 1]
            if lastElem not in visited:
                temp = findNeighbor(lastElem, wordList)
                visited.add(lastElem)
                for each in temp:
                    queue.append(current + [each])
            # All the list in the queue
            for item in queue:
                # If one of the list contains the target, means that the ladder is found
                if target in item:
                    done = True
                    ladder = item
    # ladder = helper(start,target,wordList,queue,ladder,visited)

    return ladder

def main():

    begin = time.time()

    inFileName = input("Enter the file name(.txt)")
    testFileName = input("Enter the test file name:")
    ExpectedLenth = 2
    first = 0
    second = 1
    # A set of unique word from the text file, with no duplicates
    data = buildSet(inFileName)
    test = ConstructTest(testFileName)
    ladder = None
    for case in test:
        start = case[first]
        target = ""
        if len(case) == ExpectedLenth:
            target = case[second]
        filtered = filter(data, start, target)
        # avoid duplicates in the visited neighbors
        wordList = dict()
        # If there is nothing in the filtered data, there is no point of finding the ladder
        print("\nStart word: {} Target Word: {}".format(start,target))
        if filtered != None:
            start = start.lower()
            target = target.lower()
            # Make a dictionary of filtered word, to ensure key: string value: boolean if the word is finished
            for item in filtered:
                wordList[item] = False
            ladder = BuildLadder(start, target, wordList)
        if ladder == None or filtered == None:
            print("No ladder can be found")
        else:
            print(ladder)

    end = time.time()

    print("\nTime for {} cases: {} ".format(len(test), round(end - begin,2)))
main() 
