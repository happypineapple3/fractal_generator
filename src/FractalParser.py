from pathlib import Path
import sys

def fractalParser(fractFile):
    p = Path(fractFile)
    fractalConfig = {}
    f = open(fractFile)
    for line in f:
        if '#' in line:
            continue
        if line == '\n':
            continue
        data = line.split(':', maxsplit=1)
        print(data)
        key = data[0]
        value = data[1].strip('\n').strip()
        fractalConfig[key] = value
    f.close()
    fractalConfig['centerx'] = safe_convert(fractalConfig['centerx'], float)
    fractalConfig['centery'] = safe_convert(fractalConfig['centery'], float)
    fractalConfig['axislength'] = safe_convert(fractalConfig['axislength'], float)
    fractalConfig['pixels'] = safe_convert(fractalConfig['pixels'], int)
    fractalConfig['iterations'] = safe_convert(fractalConfig['iterations'], int)
    if 'creal' in fractalConfig:
        fractalConfig['creal'] = safe_convert(fractalConfig['creal'], float)
    if 'cimag' in fractalConfig:
        fractalConfig['cimag'] = safe_convert(fractalConfig['cimag'], float)


    fractalConfig['min'] = {'x': fractalConfig['centerx'] - fractalConfig['axislength'] / 2, 
                          'y': fractalConfig['centery'] - fractalConfig['axislength'] / 2}
    fractalConfig['max'] = {'x': fractalConfig['centerx'] + fractalConfig['axislength'] / 2, 
                          'y': fractalConfig['centery'] + fractalConfig['axislength'] / 2}
    fractalConfig['pixelsize'] = abs(fractalConfig['max']['x']-fractalConfig['min']['x']) / fractalConfig['pixels']
    fractalConfig['imagename'] = p.stem
    print(fractalConfig)
    return fractalConfig



def safe_convert(obj, new_type):
    """
    Convert 'obj' to 'new_type' without crashing.

    :param obj: An object to convert into a new type
    :param new_type: Type constructor function

    :return: A new object of type 'new_type', or None if the conversion is not possible
    """
    if not type(new_type) == type:
        raise ValueError(f"Second argument must be a valid Python type")
    try:
        return new_type(obj)
    except ValueError:
        return None
