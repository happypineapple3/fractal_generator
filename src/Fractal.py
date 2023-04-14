class Fractal:
    def __init__(self, iterations):
        self.iterations = iterations

    def count():
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")


class Phoenix(Fractal):
    def __init__(self, iterations, c):
        super().__init__(iterations)
        self.c = c

    def count(self, coordinates, c):
        phoenix = complex(-0.5, 0.0)
        zPrev = 0+0j  	  	   	  	  
        z = complex(coordinates.imag, coordinates.real)
        for i in range(self.iterations):	  	  
            zNext = z
            z = z * z + c + (phoenix * zPrev)  	  	  
            zPrev = zNext 	  	  
            if abs(z) > 2.0: 
                return i   	  
        return self.iterations - 1 
    

class Mandelbrot(Fractal):
    def __init__(self, iterations):
        super().__init__(iterations)

    def count(self, coordinates):  	  
        z = complex(0, 0)	  	  
        for i in range(self.iterations):  	  	  
            z = z * z + coordinates
            if abs(z) > 2:  	  	  
                z = 2 	  	   	  	   	  	  
                return i  	  
        return self.iterations-1

    
class Julia(Fractal):
    def __init__(self, iterations, c):
        super().__init__(iterations)
        self.c = c

    def count(self, coordinates, c):
        z = coordinates
        for i in range(self.iterations):
            z = z * z + c
            if abs(z) > 2.0:
                return i
        return i
    

class Spider(Fractal):
    def __init__(self, iterations):
        super().__init__(iterations)

    def count(self, coordinates):
        z = complex(0,0)
        for i in range(self.iterations):
            z = z * z + coordinates
            coordinates = (coordinates/2) + z
            if abs(z) > 2.0:
                return i
        return i
    

class BurningShip(Fractal):
    def __init__(self, iterations, c):
        super().__init__(iterations)
        self.c = c

    def count(self, coordinates, c):
        z = complex(0,0)
        for i in range(self.iterations):
            z = (abs(z.real) + abs(z.imag) * 1j) ** 2 + coordinates
            if abs(z) > 2.0:
                return i
        return self.iterations - 1
    

class Ryan(Fractal):
    def __init__(self, iterations):
        super().__init__(iterations)

    def count(self, coordinates):
        z = complex(0,0)
        for i in range(self.iterations):
            z = coordinates**z
            if abs(z) > 2.0:
                return i
        return self.iterations-1


