c = complex(.5667, 0.0)
pheonix = complex(-0.5, 0.0)  	  	  

def phoenixIterationCount(z):  	  	    	  
 	  
    zPrev = 0+0j  	  	   	  	  
    z = complex(z.imag, z.real)  	  

    for i in range(102): 	  	  

        zSave = z 	  	  
        z = z * z + c + (pheonix * zPrev)  	  	  
        zPrev = zSave 	  	  
	  	  
        if abs(z) > 2:  	  	  
            return i   	  
    return 101 	  	  
 