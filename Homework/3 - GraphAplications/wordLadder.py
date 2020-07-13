"""
Write a function that takes in two words (beginWord and endWord), and a dictionary’s word list. A word can be transformed into another word if 1), they differ by only one letter, and 2) the new word exists in the dictionary.

Return the length of shortest transformation sequence from beginWord to endWord.
"""


def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""

    def compareWords(firstWord, secondWord):
        difference = 0
        for i in range(len(firstWord)):
            if firstWord[i] != secondWord[i]:
                difference += 1
        return difference == 1

    def findClosest(word):
        close = []
        for i in wordList:
            if compareWords(word, i):
                close.append(i)
        return close

    def recursive(currentWord, targetWord, path=[], seen=set()):
        seen.add(currentWord)
        path.append(currentWord)
        neighbors = findClosest(currentWord)
        for neighbor in neighbors:
            if neighbor == targetWord:
                return path
            fullPath = None
            if neighbor not in seen:
                fullPath = recursive(neighbor, targetWord, path, seen)
            if fullPath is not None:
                return fullPath
        path.pop()
        return None

    return len(recursive(beginWord, endWord))

    pass


# Test Cases
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

assert wordLadderLength(beginWord, endWord, wordList) == 5
