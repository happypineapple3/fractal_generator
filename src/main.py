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

import ImagePainter
import FractalFactory
import FractalParser
import PaletteFactory
import sys  

def printFractal(fractal, palette, config):
    print("Rendering %s fractal" % config['imagename'], file=sys.stderr)  	  	  	  	  
    ImagePainter.ImagePainter(fractal, palette, config)
    print("Close the image window to exit the program", file=sys.stderr)


if len(sys.argv) < 2:
    defaultFractal = FractalFactory.makeFractal(FractalFactory.DEFAULTCONFIG)
    defaultPalette = PaletteFactory.makePalette(PaletteFactory.DEFAULT_PALETTE, PaletteFactory.DEFAULT_LENGTH)
    print("Generating a default Fractal...")
    print("Generating a default Palette...")
    printFractal(defaultFractal, defaultPalette, FractalFactory.DEFAULTCONFIG)  	  

elif len(sys.argv) < 3:
    config = FractalParser.fractalParser(sys.argv[1])
    fractal = FractalFactory.makeFractal(config)
    palette = PaletteFactory.makePalette(PaletteFactory.DEFAULT_PALETTE, config['iterations'])
    print("Generating a default Palette...")
    printFractal(fractal, palette, config)

else: 
    config = FractalParser.fractalParser(sys.argv[1])
    fractal = FractalFactory.makeFractal(config)
    palette = PaletteFactory.makePalette(sys.argv[2], config['iterations'])
    printFractal(fractal, palette, config)
