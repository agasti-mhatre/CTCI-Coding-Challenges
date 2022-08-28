# ord() - gets ascii value of a character

def anagram_sort(s_list):
    sum_chars = dict()
    for item in s_list:
        sum = 0
        for character in item:
            if character.isupper():
                x = character.lower()
            else:
                x = character

            sum += ord(x)

        if sum in sum_chars:
            sum_chars[sum].append(item)
        else:
            sum_chars[sum] = [item]

    i = 0
    for a_list in sum_chars.values():
        for anagram in a_list:
            s_list[i] = anagram
            i += 1

    return s_list


if __name__ == "__main__":
    s_list = ["bruh", "hrbu", "this", "hist", "yer", "Hrub"]

    print(anagram_sort(s_list))

    # Runtime: O(s * a) {where s is the number of strings and a is the numbers of characters of the longest string}