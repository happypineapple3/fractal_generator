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
from tkinter import Tk, PhotoImage, mainloop
from time import time

import sys  	  	  

ALL_FRACTALS = ['phoenix', 'peacock', 'monkey-knife-fight', 'shrimp-cocktail',
                'mandelbrot', 'mandelbrot-zoomed', 'spiral0', 'spiral1', 'seahorse',
                'elephant', 'leaf', 'starfish']


def phoenix_main(i):  	  	  
    """The main entry-point for the Phoenix fractal generator"""  	  	   
    b4 = time() 

    print("Rendering %s fractal" % i, file=sys.stderr)  	  	  
    # construct a new TK PhotoImage object that is 512 pixels square...  	  	  
    tkPhotoImage = PhotoImage(width=512, height=512)  	  	  
    # ... and use it to make a picture of a fractal  	  	  
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?  	  	  
    makePictureOfFractal(fractalDict['phoenixDict'][i], phoenixPalette, tkPhotoImage, '#000000', 512)  	  	  

    # Write out the Fractal into a .gif image file  	  	  
    tkPhotoImage.write(i + ".png")  	  	  
    #tkPhotoImage.write(f"{i}.png")  	  	  
    print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)  	  	  
	  	  

    print("Close the image window to exit the program", file=sys.stderr)  	  	  
    # Call tkinter.mainloop so the GUI remains open  	  	  
    mainloop()  


def mbrot_main(image):  	  	  
    global img  	  	  
    print("Rendering {} fractal".format(image), file=sys.stderr)  	  	  
    before = time()	  	  
    global window  	  	  
    window = Tk()  	  	  
    img = PhotoImage(width=512, height=512)  	  	  
    paint(fractalDict['mandelDict'], image, window)  	  	  

    # Save the image as a PNG  	  	  
    after = time()	  
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)  	  	  
    img.write(f"{image}.png")  	  	  
    print(f"Wrote picture {image}.png", file=sys.stderr)  	  	  

    # Call tkinter.mainloop so the GUI remains open  	  	  
    print("Close the image window to exit the program", file=sys.stderr)  	  	  
    mainloop()  	  	  


if len(sys.argv) < 1:
    print("USAGE: the first argument needs to be the name of a fractal")
if sys.argv[1] in fractalDict['phoenixDict'].keys(): 
    phoenix_main(sys.argv[1])  	  	  
elif sys.argv[1] in fractalDict['mandelDict'].keys(): 	  	  
    mbrot_main(sys.argv[1]) 	  
else: 
    print(f"ERROR: {sys.argv[1]} is not a valid fractal.")
    print("Please select from one of the following:\n")
    for i in range(len(ALL_FRACTALS)):
        print(ALL_FRACTALS[i])
