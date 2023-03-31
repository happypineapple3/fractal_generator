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
from FractalInformation import fractalDic	  	  

class TestFractalInformation(unittest.TestCase):  	  	  
    def test_dictionaryLength(self):  	  	  
        self.assertEqual(len(fractalDic), 12)	  	  

    def test_dictionaryContents(self):  	  	  
        self.assertIsNone(fractalDic['phoenix']['absent'])	  	  
        self.assertIsNotNone(fractalDic['phoenix']['phoenix'])
        self.assertIsNone(fractalDic['mandelbrot']['absent'])	  	  
        self.assertIsNotNone(fractalDic['mandelbrot']['spiral1'])

    def test_fractalInformation(self):
        for i in range(4):
            self.assertEqual(len(fractalDic['phoenix'][i]), 3) 
        for i in range(8):
            self.assertEqual(len(fractalDic['mandelbrot'][i]), 3)  	  	  
       	  	  


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
