MAX_ITERATIONS = 111


def mandelIterationCount(coordinate):  	  
    z = complex(0, 0) 	  	   	  	  
  	  
    for i in range(MAX_ITERATIONS):  	  	  
        z = z * z + coordinate 
        if abs(z) > 2:  	  	  
            z = 2 	  	   	  	  
            if i >= MAX_ITERATIONS:  	  	  
                i = MAX_ITERATIONS - 1  	  	  
            return i 	  	  
    return MAX_ITERATIONS-1
	  	  
     