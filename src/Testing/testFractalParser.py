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
import FractalParser
import os

class TestFractalParser(unittest.TestCase):
    def setUp(self):
        self.fileContents1 = """\
# The full Julia set in all its glory
# You'll need to implement this formula yourself so your program can produce this image
type: julia
creal: -1.0125
cimag: 0.275
pixels: 1024
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 78
"""

        self.fileContents2 = """\
            # Basic mandelbrot set, fully zoomed out
type: mandelbrot
pixels: 640
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 100
"""

        self.fileName1 = "_TEST_READ_file1.txt"
        self.fileName2 = "__TEST_READ_file2.txt"

        f = open(self.fileName1, 'w')
        print(self.fileContents1, end="", file=f)
        f.close()

        f = open(self.fileName2, 'w')
        print(self.fileContents2, end="", file=f)
        f.close()


    def test_FractalParser(self):
        """
        Make sure that the fractal parser returns the correct number of keys in the dictionary 
        """
        with_c = FractalParser.fractalParser(self.fileName1)
        self.assertEqual(len(with_c.keys()), 12)
        without_c = FractalParser.fractalParser(self.fileName2)
        self.assertEqual(len(without_c.keys()), 10)


    def tearDown(self):
        os.remove(self.fileName1)
        os.remove(self.fileName2)

            


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
