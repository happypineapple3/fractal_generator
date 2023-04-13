from Palette import Birthday, America

def makePalette(paletteName, length):
    if paletteName == 'Birthday': return Birthday(length)
    elif paletteName == 'America': return America(length)