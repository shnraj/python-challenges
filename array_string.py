def main():
    print has_unique_chars('start')
    print has_unique_chars('asd')


# Implement an algorithm to determine if a string has all unique characters
def has_unique_chars(str):
    character_set = set()
    for character in str:
        if character in character_set:
            return False
        else:
            character_set.add(character)
    return True

if __name__ == "__main__":
    # execute only if run as a script
    main()
