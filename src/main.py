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

from ImagePainter import makeFractal
from FractalInformation import fractalDict
import sys  	  	  

def printFractal(fractalName):  	  	  
    print("Rendering %s fractal" % fractalName, file=sys.stderr)  	  	  	  	  
    makeFractal(fractalDict[fractalName], fractalName, fractalDict[fractalName]['type']) 
    print("Close the image window to exit the program", file=sys.stderr)  	  	  


if len(sys.argv) < 2:
    print("USAGE: please input the name of one of the following fractals as an argument")
    for key in fractalDict:
        print(key)
    sys.exit(1)
if sys.argv[1] in fractalDict: 
    printFractal(sys.argv[1])  	  	    
else: 
    print(f"ERROR: \'{sys.argv[1]}\' is not a valid fractal.")
    print("Please select from one of the following:")
    for key in fractalDict:
        print(key)
    sys.exit(1)
