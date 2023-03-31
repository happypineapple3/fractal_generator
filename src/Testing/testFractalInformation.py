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
from FractalInformation import fractalDict  

class TestFractalInformation(unittest.TestCase):  	  	  
    def test_dictionaryLength(self):
        """Testing length of dictionary"""
        self.assertEqual(len(fractalDict.keys()), 12)

    def test_dictionaryContents(self):
        """Testing existent elements in the dictionary"""  
        self.assertIsNotNone(fractalDict['phoenix'])	  	  
        self.assertIsNotNone(fractalDict['peacock'])
        self.assertIsNotNone(fractalDict['monkey-knife-fight'])	  	  
        self.assertIsNotNone(fractalDict['shrimp-cocktail'])
        self.assertIsNotNone(fractalDict['mandelbrot'])	  	  
        self.assertIsNotNone(fractalDict['mandelbrot-zoomed'])
        self.assertIsNotNone(fractalDict['spiral0'])	  	  
        self.assertIsNotNone(fractalDict['spiral1'])
        self.assertIsNotNone(fractalDict['leaf'])	  	  
        self.assertIsNotNone(fractalDict['elephants'])
        self.assertIsNotNone(fractalDict['seahorse'])	  	  
        self.assertIsNotNone(fractalDict['starfish'])

    def test_fractalInformation(self):
        """Making sure that each subkey has four elements"""
        self.assertEquals(len(fractalDict['phoenix']),4)	  	  
        self.assertEquals(len(fractalDict['peacock']),4)
        self.assertEquals(len(fractalDict['monkey-knife-fight'])	,4)  	  
        self.assertEquals(len(fractalDict['shrimp-cocktail']),4)
        self.assertEquals(len(fractalDict['mandelbrot']),4)
        self.assertEquals(len(fractalDict['mandelbrot-zoomed']),4)
        self.assertEquals(len(fractalDict['spiral0']),4)
        self.assertEquals(len(fractalDict['spiral1']),4)
        self.assertEquals(len(fractalDict['leaf']),4)  
        self.assertEquals(len(fractalDict['elephants']),4)
        self.assertEquals(len(fractalDict['seahorse']),4)  	  
        self.assertEquals(len(fractalDict['starfish']),4)	  	  
            


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
