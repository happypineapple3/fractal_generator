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
from Pallete import mandelPallete, phoenixPallete, returnColor	  


# autocmd BufWritePost <buffer> !python3 runTests.py  	  	  

class Pallete(unittest.TestCase):  	  	  
    def test_mandelPalleteColor(self):  	  	  
        self.assertEqual(returnColor(mandelPallete, complex(0, 0)), '#7D387D')  	  	  
        self.assertEqual(returnColor(mandelPallete, complex(-0.751, 1.1075)), '#E0DC9C')  	  	  
        self.assertEqual(returnColor(mandelPallete, complex(-0.2, 1.1075)), '#CDDC93')  	  	  
        self.assertEqual(returnColor(mandelPallete, complex(-0.75, 0.1075)), '#79D078')  	  	  
        self.assertEqual(returnColor(mandelPallete, complex(-0.748, 0.1075)), '#59C0BD')  	  	  
        self.assertEqual(returnColor(mandelPallete, complex(-0.7562500000000001, 0.078125)), '#6ECB8A')  	  	  
 	  

    def test_phoenixPalleteColor(self):  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(0, 0)), '#ffeca5')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.751, 1.1075)), '#ffe4b5')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.2, 1.1075)), '#ffe5b2')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.750, 0.1075)), '#86ff4a')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.748, -0.1075)), '#002277')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.75625, 0.078125)), '#002277')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.75625, -0.234375)), '#94ff51')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(0.33749, -0.625)), '#ffe7af')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.678125, -0.46875)), '#002277')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.406, -0.837)), '#ffe5b2')  	  	  
        self.assertEqual(returnColor(phoenixPallete, complex(-0.186, -0.685)), '#ffe7af')  	  	  

    def test_palleteLength(self):  	  	  
        """Palette contains the expected number of colors"""  	  	  
        self.assertEqual(111, len(mandelPallete))
        self.assertEqual(108, len(phoenixPallete))
 	  
 	  	  


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
