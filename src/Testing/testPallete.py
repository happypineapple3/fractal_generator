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
import Palette

class TestPallete(unittest.TestCase):

    def test_palleteLength(self):  	  	  
        """Palettes contains the expected number of colors"""
        america0 = Palette.America(100)
        america1 = Palette.America(500)
        america2 = Palette.America(1)
        birthday0 = Palette.Birthday(100)
        birthday1 = Palette.Birthday(500)
        birthday2 = Palette.Birthday(1)
        self.assertEqual(105, len(america0.colors))
        self.assertEqual(504, len(america1.colors))
        self.assertEqual(6, len(america2.colors))
        self.assertEqual(108, len(birthday0.colors))
        self.assertEqual(510, len(birthday1.colors))
        self.assertEqual(12, len(birthday2.colors))


    def test_getColor(self):  	  	  
        """getColor functions return colors in their hex form"""
        america = Palette.America(300)
        birthday = Palette.Birthday(300)
        for i in range(len(america.colors)):     
            self.assertTrue(america.getColor(i).startswith('#'))
        for i in range(len(birthday.colors)):
            self.assertTrue(birthday.getColor(i).startswith('#'))
 	  
if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
