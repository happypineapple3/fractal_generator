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
import Fractal

class TestFractal(unittest.TestCase):  	  	   	  	  
  	  
    def test_phoenix_count(self):
        """Phoenix count function works properly"""
        phoenix = Fractal.Phoenix(102, complex(0.5667, 0.0))
        self.assertEqual(phoenix.count(complex(1.3715877716064453+4.113485813140869j), complex(0.5667, 0.0)),0)
        self.assertEqual(phoenix.count(complex(2.3041632358551025-3.0412960052490234j), complex(0.5667, 0.0)),0)  	  
        self.assertEqual(phoenix.count(complex(2.6351680938720703-2.4042677879333496j), complex(0.5667, 0.0)),0)
 	  	  
    def test_mandelbrot_count(self):
        """Mandelbrot count function works properly"""
        mandel = Fractal.Mandelbrot(111)
        self.assertEqual(mandel.count(complex(0.5572265624999999-1.2451171875j)), 1) 
        self.assertEqual(mandel.count(complex(-0.2999081196223699-0.09429218916331959j)), 110)  	  	  
        self.assertEqual(mandel.count(complex(-0.4779296875000001-1.2060546875j)), 2)

    def test_julia_count(self):
        """Julia count function works properly"""
        julia = Fractal.Julia(78, (-1.0125+0.275j))
        self.assertEqual(julia.count(complex(-0.16015625+0.6796875j), (-1.0125+0.275j)), 7)
        self.assertEqual(julia.count(complex(-0.109375+0.6796875j), (-1.0125+0.275j)), 14)
        self.assertEqual(julia.count(complex(1.52734375+0.6796875j), (-1.0125+0.275j)), 0)

    def test_spider_count(self):
        """Spider count function works properly"""
        spider = Fractal.Spider(200)
        self.assertEqual(spider.count(complex(0,0)), 199)
        self.assertEqual(spider.count(complex(10,10)), 0)
        self.assertEqual(spider.count(complex(.25)), 4)

    def test_burning_ship(self):
        """BurningShip count function works properly"""
        ship = Fractal.BurningShip(200, (-0.598 + 0.9225j))
        self.assertEqual(ship.count(complex(-1.8, -.08), (-0.598 + 0.9225j)), 3)
        self.assertEqual(ship.count(complex(-1.78615, -.0013), (-0.598 + 0.9225j)), 199)
        self.assertEqual(ship.count(complex(-1.77457, -.0415), (-0.598 + 0.9225j)), 18)
 	  	  

if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
