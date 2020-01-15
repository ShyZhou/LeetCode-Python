# Alien Dictionary

# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example 1:

# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"

# Example 2:
# Input:
# [
#   "z",
#   "x"
# ]

# Output: "zx"

# Example 3:
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]

# Output: ""

# Explanation: The order is invalid, so return "".

# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# 给一个单词字典，单词是按照字典序排序，求字母的排序。以题中例子，先看所有单词的第1个字符，可知顺序是w->e-r。然后对于两个连续的单词，找到第一个不相同的字符，比如 wrt和wrf，wr之后t在f之前，所以排序是 t->f。按照当前字母前面出现的字母个数排序，比如w前面有0个字母，e前面有w一个字母，r前面有e和w两个字母，所以排序是w->e->r。因此可以归结为一个拓扑问题，先建图，然后进行遍历。首先统计入度：w的入度是0，e的入度是1，r的入度是2。先把入度为0的节点放入结果中，然后取出w后面连接的节点，将他们的入度-1，如果有入度为0的节点，再放入结果中。

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res, zero_in_degree_queue, in_degree, out_degree = [], collections.deque(), {}, {}
        nodes = set()
        for word in words:
            for c in word:
                nodes.add(c)

        for i in range(1, len(words)):
            if len(words[i - 1]) > len(words[i]) and words[i - 1][:len(words[i])] == words[i]:
                return ''
            self.findEdges(words[i - 1], words[i], in_degree, out_degree)

        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)

        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft()
            res.append(precedence)

            if precedence in out_degree:
                for c in out_degree[precedence]:
                    in_degree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)

                del out_degree[precedence]

        if out_degree:
            return ''

        return ''.join(res)

    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len = min(len(word1), len(word2))
        for i in range(str_len):
            if word1[i] != word2[i]:
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = set()
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = set()
                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break
