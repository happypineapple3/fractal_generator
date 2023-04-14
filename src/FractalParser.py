from pathlib import Path


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
    
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def fractalParser(fractFile):
    p = Path(fractFile)

    fractalConfig = {'type': None, 
                'creal': None, 
                'cimag': None, 
                'pixels': None, 
                'centerx': None, 
                'centery': None, 
                'axislength': None, 
                'iterations': None}
    
    f = open(fractFile)
    try:
        for line in f:
            if '#' in line or line == '\n' or not ':' in line:
                continue
            data = line.split(':', maxsplit=1)
            key = data[0].lower()
            if not key in fractalConfig:
                continue
            value = data[1].strip('\n').strip().lower()
            fractalConfig[key] = value
    except:
        pass
    f.close()

    if fractalConfig['type'] != 'phoenix' and fractalConfig['type'] != 'mandelbrot' and fractalConfig['type'] != 'julia' and fractalConfig['type'] != 'spider' and fractalConfig['type'] != 'burningship' and fractalConfig['type'] != 'ryan':
        raise NotImplementedError("The selected fractal type is not supported. Please check the user's manual for a list of valid fractal types")

    if fractalConfig['type'] == None:
        raise RuntimeError("Please specify a 'type' of fractal.\nMake sure there is a colon in between the values and nothing is misspelled.")
    if not fractalConfig['type'].isalpha():
        raise RuntimeError("The 'type' of fractal should not be a number.\nMake sure there is a colon in between the values and nothing is misspelled.")
    
    if fractalConfig['centerx'] == None:
        raise RuntimeError("Please specify a 'centerx' value.\nMake sure there is a colon in between the values and nothing is misspelled.")
    if not is_float(fractalConfig['centerx']):
        raise RuntimeError("The 'centerx' value should be a floating point number.\nMake sure there is a colon in between the values and nothing is misspelled.")
    
    if fractalConfig['centery'] == None:
        raise RuntimeError("Please specify a 'centery' value.\nMake sure there is a colon in between the values and nothing is misspelled.")
    if not is_float(fractalConfig['centery']):
        raise RuntimeError("The 'centery' value should be a floating point number.\nMake sure there is a colon in between the values and nothing is misspelled.")
    
    if fractalConfig['iterations'] == None:
        raise RuntimeError("Please specify an 'iterations' value.\nMake sure there is a colon in between the values and nothing is misspelled.")
    if not fractalConfig['iterations'].isdigit():
        raise RuntimeError("The 'iterations' value should be a positive integer.\nMake sure there is a colon in between the values and nothing is misspelled.")
    
    if fractalConfig['pixels'] == None:
        raise RuntimeError("Please specify a 'pixels' value.\nMake sure there is a colon in between the values and nothing is misspelled.")
    if not fractalConfig['pixels'].isdigit():
        raise RuntimeError("The 'pixels' value should be a positive integer.\nMake sure there is a colon in between the values and nothing is misspelled.")
    
    if fractalConfig['axislength'] == None:
        raise RuntimeError("Please specify an 'axislength' value.\nMake sure there is a colon in between the values and nothing is misspelled.")
    if not is_float(fractalConfig['axislength']):
        raise RuntimeError("The 'axislength' value should be a floating point number.\nMake sure there is a colon in between the values and nothing is misspelled.")
    
    if (fractalConfig['type'] == 'ryan' or fractalConfig['type'] == 'burningship' or fractalConfig['type'] == 'julia' or fractalConfig['type'] == 'phoenix' or fractalConfig['type'] == 'burningshipjulia'):
        if fractalConfig['creal'] == None:
            raise RuntimeError("The fractal specified requires a 'creal' value, but none is provided.\nMake sure there is a colon in between the values and nothing is misspelled.")
        elif not is_float(fractalConfig['creal']):
            raise RuntimeError("The 'creal' value must be a floating point number.\nMake sure there is a colon in between the values and nothing is misspelled.")
        elif fractalConfig['cimag'] == None:
            raise RuntimeError("The Fractal specified requires a 'cimag' value, but none is provided.\nMake sure there is a colon in between the values and nothing is misspelled.")
        elif not is_float(fractalConfig['cimag']):
            raise RuntimeError("The 'cimag' value must be a floating point number.\nMake sure there is a colon in between the values and nothing is misspelled.")
    else:
        del fractalConfig['creal']
        del fractalConfig['cimag']
        
    
    fractalConfig['centerx'] = safe_convert(fractalConfig['centerx'], float)
    fractalConfig['centery'] = safe_convert(fractalConfig['centery'], float)
    fractalConfig['axislength'] = safe_convert(fractalConfig['axislength'], float)
    fractalConfig['pixels'] = safe_convert(fractalConfig['pixels'], int)
    fractalConfig['iterations'] = safe_convert(fractalConfig['iterations'], int)
    if 'creal' in fractalConfig and fractalConfig['creal'] != None:
        fractalConfig['creal'] = safe_convert(fractalConfig['creal'], float)
    if 'cimag' in fractalConfig and fractalConfig['cimag'] != None:
        fractalConfig['cimag'] = safe_convert(fractalConfig['cimag'], float)


    fractalConfig['min'] = {'x': fractalConfig['centerx'] - fractalConfig['axislength'] / 2, 
                          'y': fractalConfig['centery'] - fractalConfig['axislength'] / 2}
    fractalConfig['max'] = {'x': fractalConfig['centerx'] + fractalConfig['axislength'] / 2, 
                          'y': fractalConfig['centery'] + fractalConfig['axislength'] / 2}
    fractalConfig['pixelsize'] = abs(fractalConfig['max']['x']-fractalConfig['min']['x']) / fractalConfig['pixels']
    fractalConfig['imagename'] = p.stem
    return fractalConfig

