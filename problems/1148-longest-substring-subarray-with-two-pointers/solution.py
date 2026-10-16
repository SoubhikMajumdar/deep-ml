def longest_unique_substring(s):
    # s: a string
    # return an integer length
    seen = set()
    left = 0

    longestsub = 0
    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left+=1

        seen.add(s[right])
        
        longestsub = max(longestsub, right - left + 1)
    
    return longestsub