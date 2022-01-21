import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    # test identifier
    def test_iden_1(self):
        """test id 1"""
        self.assertTrue(TestLexer.test("hehe","hehe,<EOF>",101))

    def test_iden_2(self):
        """test id 1"""
        self.assertTrue(TestLexer.test("AhiHi","AhiHi,<EOF>",102))

    # test integer:

        # base 10
            # decimal base without underscore
    def test_int_dec_without_under(self):
        """test decimal number without undercore """
        self.assertTrue(TestLexer.test("2342534534","2342534534,<EOF>",103))

            # decimal base with 0
    def test_int_dec_0(self):
        """test decimal number is zero """
        self.assertTrue(TestLexer.test("0","0,<EOF>",104))

            # decimal base with undercored
    def test_int_dec_with_under_1(self):
        """test decimal number with undercore 1"""
        self.assertTrue(TestLexer.test("1_323_4343_435","13234343435,<EOF>",105))
    
        # base 16:
            # hex base with x and _           
    def test_int_hex_with_under_1 (self):
        """test hex number 1 """
        self.assertTrue(TestLexer.test("0x342_42_53_5353","0x34242535353,<EOF>",106))
            
            # hex base with x and ABCDEF and _
    def test_int_hex_with_under_2 (self):
        """test hex number 2 """
        self.assertTrue(TestLexer.test("0x342_AF_5D_5353","0x342AF5D5353,<EOF>",107))
            
            # hex base with X and _
    def test_int_hex_with_under_3 (self):
        """test hex number 1 """
        self.assertTrue(TestLexer.test("0X342_42_53_5353","0X34242535353,<EOF>",106))
            
            # hex base with X and _ and ABCD
    def test_int_hex_with_under_4 (self):
        """test hex number 2 """
        self.assertTrue(TestLexer.test("0X342_AF_5D_5353","0X342AF5D5353,<EOF>",109))
            
            # hex base with X and ABCD
    def test_int_hex_without_under_1(self):
        """test hex num 3 """
        self.assertTrue(TestLexer.test("0X43253143ABD0","0X43253143ABD0,<EOF>",110))
    
        # base 8
            # oct base with _
    def test_int_oct_with_under_1(self):
        """test oct number with undercore"""
        self.assertTrue(TestLexer.test("00","00,<EOF>",111))

    #test_float
        # test float normal
    def test_float_1(self):
        """test float 1"""
        self.assertTrue(TestLexer.test("1.20043242","1.20043242,<EOF>",112))
    def test_float_2(self):
        """test float 1"""
        self.assertTrue(TestLexer.test("1.0000000","1.0000000,<EOF>",113))
    def test_float_3(self):
        """test float 3"""
        self.assertTrue(TestLexer.test("0.","0.,<EOF>",114))
    def test_float_4(self):
        """test float 4"""
        self.assertTrue(TestLexer.test(".0e32",".0e32,<EOF>",115))
    def test_float_5(self):
        """test float 5"""
        self.assertTrue(TestLexer.test(".e+32",".e+32,<EOF>",116))
    def test_float_6(self):
        """test float 6"""
        self.assertTrue(TestLexer.test(".58439538e+32",".58439538e+32,<EOF>",117))
    def test_float_7(self):
        """test float 7"""
        self.assertTrue(TestLexer.test("12_434_43.58439538e+32","1243443.58439538e+32,<EOF>",118))

    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))