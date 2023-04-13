import Fractal

defaultConfig = {'type': 'julia', 
                'creal': -1.0125, 
                'cimag': 0.275, 
                'pixels': 1024, 
                'centerx': 0.0, 
                'centery': 0.0, 
                'axislength': 4.0, 
                'iterations': 78, 
                'min': {'x': -2.0, 
                        'y': -2.0}, 
                'max': {'x': 2.0,
                        'y': 2.0},
                'pixelsize': 0.00390625,
                'imagename': 'default'}

def makeFractal(fractalInfo):
    fracType = fractalInfo['type']
    iterations = fractalInfo['iterations']

    if fracType == 'mandelbrot':
        return Fractal.Mandelbrot(iterations)
    elif fracType == 'phoenix':
        return Fractal.Phoenix(iterations, complex(fractalInfo['creal'], fractalInfo['cimag']))
    elif fracType == 'julia':
        return Fractal.Julia(iterations, complex(fractalInfo['creal'], fractalInfo['cimag']))
    elif fracType == 'spider':
        return Fractal.Spider(iterations)
    elif fracType == 'burningship':
        return Fractal.BurningShip(iterations, complex(fractalInfo['creal'], fractalInfo['cimag']))
    elif fracType == 'ryan':
        return Fractal.Ryan(iterations)
