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


# Given string L representing a letter and string N representing a newspaper,
# return true if the L can be written entirely from N and false otherwise.
def newspaper_letter(N, L):
    L_dict = Counter(L)
    N_dict = Counter(N)
    return N_dict & L_dict == L_dict


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


# COMPRESS A STRING

def compress_string(string):
    compressed_str = ''
    if string:
        current_count = 1
        compressed_str += string[0]
        for letter in string[1:]:
            current_letter = compressed_str[-1]
            if letter == current_letter:
                current_count += 1
            else:
                compressed_str += str(current_count)
                compressed_str += letter
                current_count = 1
        compressed_str += str(current_count)
        if len(compressed_str) < len(string):
            return compressed_str
    return string


# REVERSE LIST OF CHARACTERS IN PLACE
# We cannot reverse a string in place because strings are immutable
# Both slice operator and reverse function create new strings

def reverse_list(list_of_chars):
    if list_of_chars:
        index = 0
        length = len(list_of_chars)
        for char in list_of_chars:
            if index < length/2:
                new_index = length - index - 1
                temp_char = list_of_chars[new_index]
                list_of_chars[new_index] = char
                list_of_chars[index] = temp_char
                index += 1
    return list_of_chars


# REMOVE DUPLICATES IN ARRAY OF NUMBERS
def remove_duplicates(arr):
    if not arr:
        return arr
    else:
        sorted_arr = sorted(arr)
        new_arr = []
        for i in range(0, len(sorted_arr)):
            if i+1 == len(sorted_arr) or sorted_arr[i] != sorted_arr[i+1]:
                new_arr.append(sorted_arr[i])
        return new_arr


# SORT ARRAY OF USERS BY AGE
class User:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.name,
                                  self.age)

    def __lt__(self, other):
        if hasattr(other, 'age'):
            return self.age < other.age


def sort_users(user_list):
    if user_list:
        return sorted(user_list)
    return user_list

if __name__ == "__main__":
    # execute only if run as a script
    main()
