def is_palindrome_reverse(s: str) -> bool:
    filtered_str = ''.join(c.lower() for c in s if c.isalnum())

    return filtered_str == filtered_str[::-1]


def is_palindrome_two_pointers(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
