from tkinter import Tk, Canvas, PhotoImage, mainloop
from Mandelbrot import mandelIterationCount
from Phoenix import phoenixIterationCount
from Palette import phoenixPalette, mandelPalette
import sys
from time import time

IMAGE_SIZE = 512

def printProgress(pixelSize, count):
    fraction_of_pixels_writtenSoFar = (pixelSize - count) / pixelSize	  	  
    print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"  	  	  
            + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",  # 34 is the length of the loading bar 	  	  
            end="\r"  	  	  
            , file=sys.stderr)  	  	  


def makeFractal(fractalDimensions, fractalName, fractalType):

    before = time()
	  	  
    minX = fractalDimensions['centerX'] - (fractalDimensions['axisLength'] / 2.0)  	  	  
    maxX = fractalDimensions['centerX'] + (fractalDimensions['axisLength'] / 2.0)  	  	  
    minY = fractalDimensions['centerY'] - (fractalDimensions['axisLength'] / 2.0)  
      	  	  
    tkWindow = Tk()
    tkPhotoImage = PhotoImage(width=IMAGE_SIZE, height=IMAGE_SIZE)  

    canvas = Canvas(tkWindow, width=IMAGE_SIZE, height=IMAGE_SIZE, background='#000000')  	  	  	  	  
    canvas.create_image((262, 262), image=tkPhotoImage, state="normal")  
    canvas.pack()  	  	  
	  	  
    pixelSize = abs(maxX - minX) / IMAGE_SIZE

    for row in range(IMAGE_SIZE, 0, -1):  	  	  
        colorList = []  	  	  
        for col in range(IMAGE_SIZE):  	  	   	  
            X = minX + col * pixelSize
            Y = minY + row * pixelSize
            if fractalType == 'phoenix':
                pixelColor = phoenixPalette[phoenixIterationCount(complex(X, Y), phoenixPalette)]
            else:
                pixelColor = mandelPalette[mandelIterationCount(complex(X,Y), mandelPalette)]
            colorList.append(pixelColor)

        pixls = '{' + ' '.join(colorList) + '}'
        tkPhotoImage.put(pixls, (0, IMAGE_SIZE - row))
        tkWindow.update()
        printProgress(IMAGE_SIZE, row)

    print(f"\nWrote picture {fractalName}.png", file=sys.stderr)  	
    after = time()	  
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)  
    tkPhotoImage.write(f"{fractalName}.png")  	  	  
    mainloop()
