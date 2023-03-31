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

from Phoenix import *
from Mandelbrot import *
from Palette import *
from ImagePainter import *
from FractalInformation import *
import sys  	  	  

def phoenix_main(fractalName):  	  	  
    print("Rendering %s fractal" % fractalName, file=sys.stderr)  	  	  	  	  
    makeFractalPhoenix(fractalDict['phoenixDict'][fractalName], fractalName) 
    print("Close the image window to exit the program", file=sys.stderr)  	  	  


def mbrot_main(fractalName):  	  	  
    print("Rendering %s fractal" % fractalName, file=sys.stderr)  	  	  
    makeFractalMandel(fractalDict['mandelDict'][fractalName], fractalName)	  	    	  
    print("Close the image window to exit the program", file=sys.stderr)  	  	  


if len(sys.argv) < 1:
    print("USAGE: the first argument needs to be the name of a fractal")
if sys.argv[1] in fractalDict['phoenixDict'].keys(): 
    phoenix_main(sys.argv[1])  	  	  
elif sys.argv[1] in fractalDict['mandelDict'].keys(): 	  	  
    mbrot_main(sys.argv[1]) 	  
else: 
    print(f"ERROR: {sys.argv[1]} is not a valid fractal.")
    print("Please select from one of the following:")
    for key in fractalDict:
        for element in fractalDict[key]:
            print(element)
