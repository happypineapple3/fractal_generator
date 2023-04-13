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
from Palette import mandelPalette, phoenixPalette
from Fractal import phoenixIterationCount
from Mandelbrot import mandelIterationCount

class TestPallete(unittest.TestCase):  	  

    def test_palleteLength(self):  	  	  
        """Palettes contains the expected number of colors"""
        dynamic = Dynamic()
        static = Static()  	  
        self.assertEqual(500, len(dynamic))
        self.assertEqual(300, len(static))

    def test_getColor_static(self):  	  	  
        """static Palette getColor function works properly"""  
        static = Static()	  	  
        self.assertEqual(static.getColor(n), color)  	  
        self.assertEqual(static.getColor(n), color)  	  
        self.assertEqual(static.getColor(n), color)  	  	  
        self.assertEqual(static.getColor(n), color)  	  	  
        self.assertEqual(static.getColor(n), color)  	  	 


    def test_getColor_dynamic(self):  	  	  
        """dynamic Palette getColor function returns colors in their hex form"""
        dynamic = Dynamic()  	  
        self.assertTrue(dynamic.getColor(100).startswith('#'))  	  	  
        self.assertTrue(dynamic.getColor(176).startswith('#'))  	  	  
        self.assertTrue(dynamic.getColor(1).startswith('#'))  	  	  
        self.assertTrue(dynamic.getColor(321).startswith('#'))  	  	  
        self.assertTrue(dynamic.getColor(88).startswith('#'))  	  	  
        self.assertTrue(dynamic.getColor(250).startswith('#'))  
 	  
if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
