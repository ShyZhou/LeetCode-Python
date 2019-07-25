# Game of Life

"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.

In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        locations = []
        for i in range(m):
            for j in range(n):
                live_neighbor = self._count_live_neighbors(board, i, j, m, n)
                if board[i][j] == 1:
                    if live_neighbor < 2 or live_neighbor > 3:
                        locations.append([i, j])
                else:
                    if live_neighbor == 3:
                        locations.append([i, j])
        for l in locations:
            board[l[0]][l[1]] = 1 - board[l[0]][l[1]]
        return None

    def _count_live_neighbors(self, board, i, j, m, n):
        s = 0
        s += board[i-1][j-1] if self._is_inbounds(i-1, j-1, m, n) else 0
        s += board[i-1][j] if self._is_inbounds(i-1, j, m, n) else 0
        s += board[i-1][j+1] if self._is_inbounds(i-1, j+1, m, n) else 0
        s += board[i][j-1] if self._is_inbounds(i, j-1, m, n) else 0
        s += board[i][j+1] if self._is_inbounds(i, j+1, m, n) else 0
        s += board[i+1][j-1] if self._is_inbounds(i+1, j-1, m, n) else 0
        s += board[i+1][j] if self._is_inbounds(i+1, j, m, n) else 0
        s += board[i+1][j+1] if self._is_inbounds(i+1, j+1, m, n) else 0
        return s

    def _is_inbounds(self, i, j, m, n):
        return (0 <= i < m and 0 <= j < n)

# Excellent discussion about follow-up:
# https://segmentfault.com/a/1190000003819277#articleHeader0
