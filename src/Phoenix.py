def phoenixIterationCount(z, palette):
    # 'c' and 'phoenix' are mathematical constants for working with imaginary numbers
    c = complex(.5667, 0.0)
    phoenix = complex(-0.5, 0.0)
    maxIterations = len(palette)

    zPrev = 0+0j  	  	   	  	  
    z = complex(z.imag, z.real)
    for i in range(maxIterations):	  	  
        zNext = z 	  	  
        z = z * z + c + (phoenix * zPrev)  	  	  
        zPrev = zNext 	  	  
        if abs(z) > 2: 
            return i   	  
    return maxIterations - 1 
 
