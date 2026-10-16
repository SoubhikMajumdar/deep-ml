def valid_palindrome(s):
    l, r = 0, len(s) - 1
    margin = 1

    while l < r:
        if s[l] != s[r]:
            if margin == 0:
                return False

            margin -= 1

            # Skip either the left or right character
            return (
                is_palindrome(s, l + 1, r) or
                is_palindrome(s, l, r - 1)
            )

        l += 1
        r -= 1

    return True


def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True