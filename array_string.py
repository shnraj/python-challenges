def main():
    print has_unique_chars('start')  # False
    print has_unique_chars('asd')  # True


# IMPLEMENT AN ALGORITHM TO DETERMINE IF A STRING HAS ALL UNIQUE CHARACTERS

# My solution - Time: O(n) Space: O(n)
def has_unique_chars(str):
    character_set = set()
    for character in str:
        if character in character_set:
            return False
        else:
            character_set.add(character)
    return True

# Other solutions: sets and length, in place


# DETERMINE IF A STRING IS A PERMUTATION OF ANOTHER

# My solution - Time: O(n) Space: O(2n)
def is_permutation(str1, str2):
    str1_set = set(str1)
    str2_set = set(str2)

    str1_set.symmetric_difference_update(str2_set)
    return len(str1_set) == 0

# Other solutions: sorting, hash map lookup


# DETERMINE IF A STRING S1 IS A ROTATION OF ANOTHER STRING S2

# My solution - Time: O(n) Space: O(2n)
def is_rotation(s1, s2):
    if len(s1) == len(s2):
        double_str = s1 + s1
        if s2 in double_str:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    # execute only if run as a script
    main()