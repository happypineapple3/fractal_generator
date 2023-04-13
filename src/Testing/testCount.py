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
        phoenix = Fractal.Phoenix()
        self.assertEqual(phoenix.count(complex(1.3715877716064453+4.113485813140869j), 102),0)
        self.assertEqual(phoenix.count(complex(2.3041632358551025-3.0412960052490234j), 102),0)  	  
        self.assertEqual(phoenix.count(complex(2.6351680938720703-2.4042677879333496j), 102),0)
 	  	  
    def test_mandelbrot_count(self):
        """Mandelbrot count function works properly"""
        mandel = Fractal.Mandelbrot()
        self.assertEqual(mandel.count(complex(0.5572265624999999-1.2451171875j), 111), 1) 
        self.assertEqual(mandel.count(complex(-0.2999081196223699-0.09429218916331959j), 111), 110)  	  	  
        self.assertEqual(mandel.count(complex(-0.4779296875000001-1.2060546875j), 111), 2)

    def test_julia_count(self):
        """Julia count function works properly"""
        julia = Fractal.Julia()
        self.assertAlmostEqual(julia.count(complex(0.285+0.01j), 200), 141)
        self.assertAlmostEqual(julia.count(complex(-0.8+0.156j), 200), 95)
        self.assertAlmostEqual(julia.count(complex(-0.70176-0.3842j), 200), 200)

    def test_spider_count(self):
        """Spider count function works properly"""
        spider = Fractal.Spider()
        self.assertAlmostEqual(spider.count(complex(0,0), 200), 0)
        self.assertAlmostEqual(spider.count(complex(10,10), 200), 200)
        self.assertAlmostEqual(spider.count(complex(.25), 0), 18)

    def test_burning_ship(self):
        """BurningShip function works properly"""
        ship = Fractal.BurningShip()
        self.assertAlmostEqual(ship.count(complex(-1.8, -.08), 200), 39)
        self.assertAlmostEqual(ship.count(complex(-1.78615, -.0013), 200), 146)
        self.assertAlmostEqual(ship.count(complex(-1.77457, -.0415), 200), 139)
 	  	  

if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
