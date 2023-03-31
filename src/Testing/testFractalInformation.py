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
        self.assertEqual(len(fractalDict['phoenixDict'].keys()), 4)
        self.assertEqual(len(fractalDict['mandelDict'].keys()), 8)	  

    def test_dictionaryContents(self):
        """Testing existent elements in the dictionary"""  
        self.assertIsNotNone(fractalDict['phoenixDict']['phoenix'])	  	  
        self.assertIsNotNone(fractalDict['phoenixDict']['peacock'])
        self.assertIsNotNone(fractalDict['phoenixDict']['monkey-knife-fight'])	  	  
        self.assertIsNotNone(fractalDict['phoenixDict']['shrimp-cocktail'])
        self.assertIsNotNone(fractalDict['mandelDict']['mandelbrot'])	  	  
        self.assertIsNotNone(fractalDict['mandelDict']['mandelbrot-zoomed'])
        self.assertIsNotNone(fractalDict['mandelDict']['spiral0'])	  	  
        self.assertIsNotNone(fractalDict['mandelDict']['spiral1'])
        self.assertIsNotNone(fractalDict['mandelDict']['leaf'])	  	  
        self.assertIsNotNone(fractalDict['mandelDict']['elephants'])
        self.assertIsNotNone(fractalDict['mandelDict']['seahorse'])	  	  
        self.assertIsNotNone(fractalDict['mandelDict']['starfish'])

    def test_fractalInformation(self):
        """Making sure that each subkey has three elements"""
        self.assertEquals(len(fractalDict['phoenixDict']['phoenix']),3)	  	  
        self.assertEquals(len(fractalDict['phoenixDict']['peacock']),3)
        self.assertEquals(len(fractalDict['phoenixDict']['monkey-knife-fight'])	,3)  	  
        self.assertEquals(len(fractalDict['phoenixDict']['shrimp-cocktail']),3)
        self.assertEquals(len(fractalDict['mandelDict']['mandelbrot']),3)
        self.assertEquals(len(fractalDict['mandelDict']['mandelbrot-zoomed']),3)
        self.assertEquals(len(fractalDict['mandelDict']['spiral0']),3)
        self.assertEquals(len(fractalDict['mandelDict']['spiral1']),3)
        self.assertEquals(len(fractalDict['mandelDict']['leaf']),3)  
        self.assertEquals(len(fractalDict['mandelDict']['elephants']),3)
        self.assertEquals(len(fractalDict['mandelDict']['seahorse']),3)  	  
        self.assertEquals(len(fractalDict['mandelDict']['starfish']),3)	  	  
            


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
