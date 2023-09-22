def make_acronym(phrase):
    if not isinstance(phrase, str):
        return 'Not a string'
    elif not all(n.isalpha() for n in phrase.replace(" ", "")):
        return "Not letters"
    else:
        return ''.join(n[0].upper() for n in phrase.split())
