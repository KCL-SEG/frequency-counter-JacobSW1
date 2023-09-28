"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    count = 0
    for item in items:
        item = str(item)
        for entry in items:
            entry = str(entry)
            if entry == item:
                count +=1
        frequencies.update({item: count})
        count = 0
    return frequencies