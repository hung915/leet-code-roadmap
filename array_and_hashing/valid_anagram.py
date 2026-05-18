from collections import defaultdict


def is_anagram_counter(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter = defaultdict(int)

    for i in range(len(s)):
        counter[s[i]] += 1
        counter[t[i]] -= 1

    return all(counter[c] == 0 for c in counter)


def is_anagram_two_counter(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_counter = defaultdict(int)
    t_counter = defaultdict(int)

    for i in range(len(s)):
        s_counter[s[i]] += 1
        t_counter[t[i]] += 1

    return s_counter == t_counter


def is_anagram_ascii(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter = [0] * 26

    for char in s:
        counter[ord(char) - ord('a')] += 1

    for char in t:
        if counter[ord(char) - ord('a')] == 0:
            return False
        counter[ord(char) - ord('a')] -= 1

    return True
