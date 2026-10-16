from collections import Counter
def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer

    dict1 = Counter(list1)
    dict2 = Counter(list2)
    result = 0

    for key in dict1:
        if dict1[key] == 1 and key in dict2 and dict2[key] == 1:
            result+=1

    return result 
    