from collections import OrderedDict

dup_removed = []

def duplicates(l):
    for element in l:
        if element not in dup_removed:
            dup_removed.append(element)
    return dup_removed

print(duplicates(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"]))

def duplicates_alternative(l):
    return list(set(l))

print(duplicates_alternative(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"])) # ['d', 'e', 'c', 'a', 'b']