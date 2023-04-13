#!/usr/bin/env python3  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

from ImagePainter import ImagePainter
from FractalFactory import makeFractal, defaultConfig
from FractalParser import fractalParser
from PaletteFactory import makePalette
import sys  

def printFractal(fractal, palette, config):
    print("Rendering %s fractal" % config['imagename'], file=sys.stderr)  	  	  	  	  
    ImagePainter(fractal, palette, config)
    print("Close the image window to exit the program", file=sys.stderr)  	  	  


if len(sys.argv) < 2:
    defaultFractal = makeFractal(defaultConfig)
    defaultPalette = makePalette('America', defaultConfig['iterations'])
    print("Generating a default Fractal...")
    print("Generating a default Palette...")
    printFractal(defaultFractal, defaultPalette, defaultConfig)  	  

elif len(sys.argv) < 3:
    if sys.argv[1].endswith('.frac'):
        config = fractalParser(sys.argv[1])
        fractal = makeFractal(config)
        palette = makePalette('America', config['iterations'])
        print("Generating a default Palette...")
        printFractal(fractal, palette, config)
    else:
        print("Please provide a fractal configuration profile")

else: 
    config = fractalParser(sys.argv[1])
    fractal = makeFractal(config)
    palette = makePalette(sys.argv[2], config['iterations'])
    printFractal(fractal, palette, config)
