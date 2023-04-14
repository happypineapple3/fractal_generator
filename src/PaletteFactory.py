import Palette
DEFAULT_PALETTE = 'Birthday'
DEFAULT_LENGTH = 240

def makePalette(paletteName, length):
    if paletteName == 'Birthday': return Palette.Birthday(length)
    elif paletteName == 'America': return Palette.America(length)
    else:
        raise NotImplementedError("Invalid palette requested")