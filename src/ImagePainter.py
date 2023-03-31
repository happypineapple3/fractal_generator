from tkinter import Tk, Canvas, PhotoImage, mainloop
from Mandelbrot import *
from Phoenix import *
from Palette import *
import sys

SIZE = 512
WINDOW = Tk()


# this comes from mandelbrot
def paint(fractals, imagename, window):  	  	  
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
    This code creates an image which is 640x640 pixels in size."""  	  	  

    global palette  	  	  
    global img  	  	  

    fractal = fractals[imagename]  	  	  

    # Figure out how the boundaries of the PhotoImage relate to coordinates on  	  	  
    # the imaginary plane.  	  	  
    minx = fractal['centerX'] - (fractal['axisLength'] / 2.0)  	  	  
    maxx = fractal['centerX'] + (fractal['axisLength'] / 2.0)  	  	  
    miny = fractal['centerY'] - (fractal['axisLength'] / 2.0)  	  	  
    maxy = fractal['centerY'] + (fractal['axisLength'] / 2.0)  	  	  

    # Display the image on the screen  	  	  
    canvas = Canvas(window, width=SIZE, height=SIZE, bg='#000000')  	  	  
    canvas.pack()  	  	  
    img = PhotoImage(width=SIZE, height=SIZE)  	  	  

    canvas.create_image((256, 256), image=img, state="normal")  	  	  

    # At this scale, how much length and height on the imaginary plane does one  	  	  
    # pixel take?  	  	  
    pixelsize = abs(maxx - minx) / SIZE  	  	  


    # loop  	  	  
    for row in range(SIZE, 0, -1):  	  	  
        cc = []  	  	  
        for col in range(SIZE):  	  	  
            x = minx + col * pixelsize  	  	  
            y = miny + row * pixelsize  	  	  
            # "Leaf" is the only well-behaved fractal - all of the others crash  	  	  
            #  	  	  
            color = mandelPalette[mandelIterationCount(complex(x,y))]	  	  
            # The rest of the fractals  	  	  	  	  
            cc.append(color)  	  	  
            y = miny + row * pixelsize # prepare for next loop  	  	  
            x = minx + col * pixelsize # prepare for next loop  	  	  

        img.put('{' + ' '.join(cc) + '}', to=(0, SIZE-row))  	  	  
        window.update()  # display a row of pixels  	  	  
 	  
        printProgress(SIZE, row)

# this comes from phoenix
def makePictureOfFractal(f, w, p, W, s): 	 
	  	  
	  	  
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),  	  	  
           (f['centerY'] - (f['axisLength'] / 2.0)))  	  	  	  	  
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),  	  	  
           (f['centerY'] + (f['axisLength'] / 2.0)))
      	  	  

    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(WINDOW, width=s, height=s, bg=W)  	  	  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((SIZE/2, SIZE/2), image=p, state="normal")  	  	  
   
    size = abs(max[0] - min[0]) / SIZE
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  	  	  

    for row in range(SIZE, 0, -1):  	  	  
        cs = []  	  	  
        for c in range(SIZE):  	  	   	  
            X = min[0] + c * size  	  	  	  	  
            Y = min[1] + row * size  	  	  	  	  
            cp = phoenixPalette[phoenixIterationCount(complex(X, Y)) - 1]	  
            cs.append(cp)
        pixls = '{' + ' '.join(cs) + '}'
        p.put(pixls, (0, s - row))
        WINDOW.update()
        printProgress(SIZE, row)


def printProgress(size, count):
    fraction_of_pixels_writtenSoFar = (size - count) / size	  	  
    print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"  	  	  
            + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",  	  	  
            end="\r"  	  	  
            , file=sys.stderr)  	  	  
