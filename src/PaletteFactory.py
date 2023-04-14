from Palette import Birthday, America
DEFAULT_PALETTE = 'Birthday'
DEFAULT_LENGTH = 256

def makePalette(paletteName, length):
    if paletteName == 'Birthday': return Birthday(length)
    elif paletteName == 'America': return America(length)