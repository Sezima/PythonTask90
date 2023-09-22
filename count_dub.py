"Counting Duplicate"
def duplicate_count(text):
    c = {c: text.lower().count(c) for c in text.lower()}
    return len([i for i in c if c[i]>=2 ])
