# Word Ladder

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newword = word[:i] + c + word[i + 1:]
                    if newword != word and newword in wordset:
                        wordset.remove(newword)
                        bfs.append((newword, length + 1))
        return 0

# II

# BFS
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)

        result, cur, visited, found, trace = [], [start], set([start]), False, {word: [] for word in dict}

        while cur and not found:
            for word in cur:
                visited.add(word)

            next = set()
            for word in cur:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in dict:
                            if candidate == end:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next

        if found:
            self.backtrack(result, trace, [], end)

        return result

    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)

sol = Solution()
print(sol.ladderLength(beginWord='hit', endWord='cog', wordList=["hot","dot","dog","lot","log","cog"]))
