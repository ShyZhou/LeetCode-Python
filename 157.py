# Read N Characters Given Read4

# The API: int read4(char *buf) reads 4 characters at a time from a file.
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
# Note:
# The read function will only be called once for each test case.

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i

class Solution(object):
    def read(self, buf, n):
        read_bytes = 0
        buffer = [''] * 4
        for i in range(n/4 + 1):
            size = read4(buffer)
            if size:
                size = min(size, n - read_bytes)
                buf[read_bytes: read_bytes + size] = buffer[:size]
                read_bytes += size
            else:
                break
        return read_bytes

# The read function may be called multiple times.

# 第一次调用时，如果read4读出的多余字符我们要先将其暂存起来，这样第二次调用时先读取这些暂存的字符
# 第二次调用时，如果连暂存字符都没读完，那么这些暂存字符还得留给第三次调用时使用
# 所以，难点就在于怎么处理这个暂存字符。因为用数组和指针控制对第二种情况比较麻烦，且这些字符满足先进先出，所以我们可以用一个队列暂存这些字符。这样，只要队列不为空，就先读取队列。

class Solution(object):
    def __init__(self):
        self._buf4 = [''] * 4
        self._i4 = 0
        self._n4 = 0

    def read(self, buf, n):
        i = 0
        while i < n:
            if self._i4 < self._n4: # Any characters in buf4
                buf[i] = self._buf4[self._i4]
                i += 1
                self._i4 += 1
            else:
                self._n4 = read4(self._buf4) # Read more characters
                if self._n4:
                    self._n4 = 0
                else: # Buffer has been empty
                    break
        return i
