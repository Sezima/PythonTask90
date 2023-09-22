def has_unique_chars(string):
    if len(string) == len(set(string)):
        return True
    else:
        return False
        