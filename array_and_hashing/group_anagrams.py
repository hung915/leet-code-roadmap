from collections import defaultdict


def group_anagrams_sort(strs: list[str]) -> list[list[str]]:
    ans = defaultdict(list)

    for string in strs:
        key = ''.join(sorted(string))
        ans[key].append(string)

    return list(ans.values())


def group_anagrams_ascii(strs: list[str]) -> list[list[str]]:
    ans = defaultdict(list)

    for string in strs:
        counter = [0] * 26
        for char in string:
            counter[ord(char) - ord('a')] += 1
        ans[tuple(counter)].append(string)

    return list(ans.values())
