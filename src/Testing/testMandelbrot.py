#!/usr/bin/env python3  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  


import unittest 
from Mandelbrot import mandelIterationCount 

class TestMandelbrot(unittest.TestCase):  	  	  
 	  	  
    def test_iterationCount(self):
        """Mandelbrot iterationCount function works properly"""
        self.assertEqual(mandelIterationCount(complex(0.5572265624999999-1.2451171875j)), 1) 
        self.assertEqual(mandelIterationCount(complex(-0.2999081196223699-0.09429218916331959j)), 110)  	  	  
        self.assertEqual(mandelIterationCount(complex(-0.4779296875000001-1.2060546875j)), 2)  	  	  
 	  	  

if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
