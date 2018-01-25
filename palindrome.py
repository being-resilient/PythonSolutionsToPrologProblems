def reverse_list(l):
    l_sliced = l[:int(len(l)/2)]
    l_sliced_rev = l[:-(int((len(l))/2) + 1):-1]
    
    for index in range(len(l_sliced)):
        if l_sliced[index] != l_sliced_rev[index]:
            return "Not palindrome!!"
    return "Palindrome!!"

print(reverse_list(["x","a","m","m","a","x"])) #true
print(reverse_list(["x","a","m","x","a","m"])) #false
