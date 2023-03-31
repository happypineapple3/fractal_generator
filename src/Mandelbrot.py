MAX_ITERATIONS = 111

def mandelIterationCount(coordinates):  	  
    z = complex(0, 0) 	  	   	  	  
    for i in range(MAX_ITERATIONS):  	  	  
        z = z * z + coordinates 
        if abs(z) > 2:  	  	  
            z = 2 	  	   	  	  
            if i >= MAX_ITERATIONS:  	  	  
                i = MAX_ITERATIONS - 1 
            print(i)
            print(coordinates)  	  	  	  
            return i  	  
    return MAX_ITERATIONS-1
	  	  
     