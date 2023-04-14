import colour

class Palette:
    def __init__(self, length):
        self.colors=[]
        self.length = length
    
    def getColor(self):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")
    

class America(Palette):
    def __init__(self, length):
        super().__init__(length)
        red = colour.Color('firebrick')
        white = colour.Color('white')
        blue = colour.Color('blue')
        section = self.length//3+2
        
        self.colors = (list(c.hex for c in red.range_to(white, section)) +
                           list(c.hex for c in white.range_to(blue, section)) +
                           list(c.hex for c in blue.range_to(red, section)))

    def getColor(self, n):
        return self.colors[n]
    

class Birthday(Palette):
    def __init__(self, length):
        super().__init__(length)
        red = colour.Color('firebrick')
        blue = colour.Color('blue')
        pink = colour.Color('pink')
        yellow = colour.Color('yellow')
        purple = colour.Color('purple')
        green = colour.Color('green')
        section = self.length//6+2

        self.colors = (list(c.hex for c in pink.range_to(green, section)) +
                           list(c.hex for c in green.range_to(red, section)) +
                           list(c.hex for c in red.range_to(blue, section)) +
                           list(c.hex for c in blue.range_to(purple, section)) +
                           list(c.hex for c in purple.range_to(yellow, section)) +
                           list(c.hex for c in yellow.range_to(pink, section)))
        
    def getColor(self, n):
        return self.colors[n]