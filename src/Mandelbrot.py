def mandelIterationCount(coordinates, palette):  	  
    z = complex(0, 0)
    maxIterations = (len(palette))	  	  
    for i in range(maxIterations):  	  	  
        z = z * z + coordinates 
        if abs(z) > 2:  	  	  
            z = 2 	  	   	  	  
            if i >= maxIterations:  	  	  
                i = maxIterations - 1   	  	  
            return i  	  
    return maxIterations-1
	  	  
     