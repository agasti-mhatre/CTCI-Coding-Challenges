# Part 1

s = "program"
lookup = dict()

for letter in s:
    if letter in lookup:
        raise Exception("{} exists in the string and it is not unique".format(letter))
    else:
        lookup[letter] = letter

print("This string is unique!!!")



# Part 2
'''
s = "program"
i = 0
while i < len(s):
    j = i + 1
    while j < len(s):
        if s[i] == s[j]:
            raise Exception("{} exists in the string and it is not unique".format(s[i]))

        j += 1
    
    i += 1


print("This string is unique!!!")
'''