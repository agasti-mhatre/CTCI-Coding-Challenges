def is_it_palindrome(pal_string):
    num_characters_not_space = 0
    hashtable_count = dict()
    for letter in pal_string:
        if letter != ' ':
            num_characters_not_space += 1
        else:
            continue

        if letter in hashtable_count.keys():
            hashtable_count[letter] += 1
        else:
            hashtable_count[letter] = 1

    if (num_characters_not_space % 2) == 0:
        for count in hashtable_count.values():
            if (count % 2) != 0:
                return False
    else:
        off_by_one = 1
        for count in hashtable_count.values():
            if (count % 2) != 0:
                off_by_one -= 1

            if off_by_one < 0:
                return False


    return True


if __name__ == "__main__":
    pal_string = "taco cat"
    print(is_it_palindrome(pal_string))