import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

# test integer:
    # base 10
        #    0
    def test_int_0(self):
        """test_int_0 """
        input="0"
        expect="0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))

        #   noundercore
    def test_int_x10_no_undercore(self):
        """test_int_x10_no_undercore"""
        input="1214342"
        expect="1214342,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))

        # undercore
    def test_int_x10_with_undercore(self):
        """test_int_x10_with_undercore"""
        input="123_54_5_9605305"
        expect="1235459605305,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))
    # base 8
        #   noundercore
    def test_int_x8_no_undercore(self):
        """test_int_x8_no_undercore"""
        input="0424543543"
        expect="0424543543,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,104))

        # undercore
    def test_int_x8_with_undercore(self):
        """test_int_x8_no_undercore"""
        input="04245_4_35_43"
        expect="0424543543,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))

    # base 16
        #   noundercore and no a-f
    def test_int_x16_no_undercore_no_letter1(self):
        """test_int_x8_no_undercore"""
        input="0x424543543"
        expect="0x424543543,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,106))

    def test_int_x16_no_undercore_no_letter2(self):
        """test_int_x8_no_undercore"""
        input="0X424543543"
        expect="0X424543543,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))

        # no undercore have a-f
    def test_int_x16_no_undercore_have_letter1(self):
        """test_int_x16_no_undercore_have_letter"""
        input="0xF534A53CD"
        expect="0xF534A53CD,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))

    def test_int_x16_no_undercore_have_letter2(self):
        """test_int_x16_no_undercore_have_letter"""
        input="0XF534A53CD"
        expect="0XF534A53CD,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))
        # undercore
    def test_int_x16_with_undercore_no_letter1(self):
        """test_int_x16_with_undercore_no_letter"""
        input="0X4_2_454_354_3"
        expect="0X424543543,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,110))

    def test_int_x16_with_undercore_no_letter2(self):
        """test_int_x16_with_undercore_no_letter"""
        input="0x4_2_454_354_3"
        expect="0x424543543,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))
    def test_int_x16_with_undercore_with_letter1(self):
        """test_int_x16_with_undercore_with_letter"""
        input="0xF_534_A53C_D"
        expect="0xF534A53CD,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))

    def test_int_x16_with_undercore_with_letter2(self):
        """test_int_x16_with_undercore_with_letter"""
        input="0XF_534_A53C_D"
        expect="0XF534A53CD,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,113))
    
    # base 2
        # nounderore
    def test_int_x2_no_undercore1(self):
        """test_int_x2_no_undercore"""
        input="0b01010101011101"
        expect="0b01010101011101,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))

    def test_int_x2_no_undercore2(self):
        """test_int_x2_no_undercore"""
        input="0B01010101011101"
        expect="0B01010101011101,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))
        # withunderscore
    def test_int_x2_with_undercore1(self):
        """test_int_x2_with_undercore"""
        input="0b0_101_010101_1_101"
        expect="0b01010101011101,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,116))

    def test_int_x2_with_undercore2(self):
        """test_int_x2_with_undercore"""
        input="0B0_101_010101_1_101"
        expect="0B01010101011101,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,117))