# Approach 1 — Length Prefix (Most Optimal)
# Core Idea
# Before each word, store its length + a separator. During decode, read the length first, then extract exactly that many characters — no ambiguity possible.


def encode(strs: list[str]) -> str:
    result = ''
    for s in strs:
        result += str(len(s)) + '#' + s  # prefix each word with length#
    return result


def decode(s: str) -> list[str]:
    result = []
    i = 0

    while i < len(s):
        # find the # separator
        j = i
        while s[j] != '#':
            j += 1

        length = int(s[i:j])  # extract the length number
        word = s[j + 1 : j + 1 + length]  # extract exactly `length` chars
        result.append(word)
        i = j + 1 + length  # move pointer past this word

    return result


# Approach 2 — Chunked Transfer Encoding Approach
# Core Idea
# Inspired by HTTP chunked transfer encoding — each chunk is prefixed with its size in hex, followed by \r\n, then the data, then another \r\n. A chunk of size 0 signals the end.
def encode_chunked(strs: list[str]) -> str:
    result = ''
    for s in strs:
        size = format(len(s), 'x')
        result += size + '\r\n' + s + '\r\n'
    result += 'end\r\n\r\n'  # unambiguous terminator
    return result


def decode_chunked(s: str) -> list[str]:
    result = []
    i = 0

    while i < len(s):
        j = s.index('\r\n', i)
        size_str = s[i:j]

        if size_str == 'end':  # unambiguous end signal
            break

        size = int(size_str, 16)
        data_start = j + 2
        data = s[data_start : data_start + size]
        result.append(data)
        i = data_start + size + 2

    return result


# print(encode_chunked(['hi', 'we#', '']))
print(decode_chunked('2\r\nhi\r\n3\r\nwe#\r\n0\r\n\r\nend\r\n\r\n'))
