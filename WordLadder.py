import time

"""Building a set with the words of the same length"""


def buildSet(size, fileName=None):
    if fileName == None:
        return None
    inFile = open(fileName, 'r')
    data = inFile.readlines()
    uniques = set()
    for elem in data:
        elem = elem.rstrip("\n")
        if len(elem) == size:
            uniques.add(elem)
    inFile.close()
    return uniques


"""Find all the words with the one character difference of the given word"""


def findNeighbor(current, filtered, visited):

    neighbor = []
    # for each character in the word
    for i in range(len(current)):
        # find all new words by altering one character from a to z
        for char in range(ord('a'), ord('z') + 1):
            word = current[:i] + chr(char) + current[i + 1:]
            # if the word is in the dictionary, not the same word as currrent, and it has not been added to the neighbor list
            if word in filtered and word != current and word not in visited:
                neighbor.append(word)

    return neighbor


"""Building the test from input file"""


def ConstructTest(fileName="pairs.txt"):
    inFile = open(fileName, "r")
    data = inFile.readlines()
    test = []
    for case in data:
        test.append(case.strip("\n").split(" "))

    return test


"""Building the ladder using Breadth First Search"""


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
            temp = findNeighbor(lastElem, wordList, visited)
            visited.add(lastElem)
            for each in temp:
                queue.append(current + [each])
        # All the list in the queue
        for item in queue:
            # If one of the list contains the target, means that the ladder is found
            if target in item:
                done = True
                ladder = item
    return ladder


def main():
    # Input of dictionary
    inFileName = input("Enter the file name(.txt)")

    '''Making sure user pick a valid option'''
    try:
        testOption = int(input("1.File testing or 2.input testing: "))
    except ValueError:
        print("Invalid option")
        testOption = int(input("1.File testing or 2.input testing: "))

    begin = 0
    if testOption == 1:
        testFileName = input("Enter the test file name:")
        ExpectedLenth = 2
        first = 0
        second = 1
        # A set of unique word from the text file, with no duplicates
        begin = time.time()
        test = ConstructTest(testFileName)
        ladder = None

        for case in test:
            start = case[first]
            target = ""
            if len(case) == ExpectedLenth:
                target = case[second]
            print("\nStart word: {} Target Word: {}".format(start, target))
            if len(target) != len(start):
                print("No ladder found due to: Different length for start and end word")
                break

            filtered = buildSet(len(start), inFileName)
            # avoid duplicates in the visited neighbors
            # If there is nothing in the filtered data, there is no point of finding the ladder

            if filtered is not None:
                start = start.lower()
                target = target.lower()
                # Make a dictionary of filtered word, to ensure key: string value: boolean if the word is finished
                ladder = BuildLadder(start, target, filtered)

            if ladder is None or filtered is None:
                print("No ladder can be found")
            else:
                print(ladder)

        print("\n{} cases are tested".format(len(test)))
    else:
        start = input("Enter start word: ")
        target = input("Enter ending word: ")
        print("\nStart word: {} Target Word: {}".format(start, target))
        begin = time.time()
        if len(start) != len(target):
            print("No ladder found due to: Different length for start and end word")

        else:
            wordList = buildSet(len(start), inFileName)
            ladder = BuildLadder(start, target, wordList)
            if ladder is None:
                print("No ladder is found")
            else:
                print(ladder)

    end = time.time()

    print("Total time used: ", round(end - begin, 2))


main()
