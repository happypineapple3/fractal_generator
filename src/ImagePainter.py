from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
import sys



class ImagePainter:
    def __init__(self, fractal, palette, config):
        self.fractal = fractal
        self.palette = palette
        self.config = config

        before = time()
            
        tkWindow = Tk()
        tkPhotoImage = PhotoImage(width=self.config['pixels'], height=self.config['pixels'])  

        canvas = Canvas(tkWindow, width=self.config['pixels'], height=self.config['pixels'], background='#000000')  	  	  	  	  
        canvas.create_image((self.config['pixels']//2 +2, self.config['pixels']//2 +2), image=tkPhotoImage, state="normal")  
        # canvas.create_image((0,0), anchor='nw', image=tkPhotoImage, state="normal")  

        canvas.pack()  	  	  
            
        for row in range(self.config['pixels'], 0, -1):  	  	  
            colorList = []  	  	  
            for col in range(self.config['pixels']):  	  	   	  
                X = self.config['min']['x'] + col * self.config['pixelsize']
                Y = self.config['min']['y'] + row * self.config['pixelsize']
                if 'creal' and 'cimag' in config:
                    c = self.config['creal'] + self.config['cimag']
                    pixelColor = self.palette.getColor(self.fractal.count((complex(X, Y)), c))
                else:
                    pixelColor = self.palette.getColor(self.fractal.count((complex(X,Y))))
                colorList.append(pixelColor)    

            pixls = '{' + ' '.join(colorList) + '}'
            tkPhotoImage.put(pixls, (0, self.config['pixels'] - row))
            tkWindow.update()
            printProgress(self.config['pixels'], row)

        print(f"\nWrote picture {self.config['imagename']}.png", file=sys.stderr)  	
        after = time()	  
        print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)  
        tkPhotoImage.write(f"{self.config['imagename']}.png")  	  	  
        mainloop()



def printProgress(pixelSize, count):
    fraction_of_pixels_writtenSoFar = (pixelSize - count) / pixelSize	  	  
    print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"  	  	  
            + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",	  	  
            end="\r"  	  	  
            , file=sys.stderr)  	  	  

