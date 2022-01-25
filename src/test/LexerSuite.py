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
    def test_int_x8_1(self):
        """test_int_x8_1: 2 token"""
        input="000123"
        expect="00,0123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,118))

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
        input="0b1010101011101"
        expect="0b1010101011101,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))

    def test_int_x2_no_undercore2(self):
        """test_int_x2_no_undercore"""
        input="0B1010101011101"
        expect="0B1010101011101,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))
        # withunderscore
    def test_int_x2_with_undercore1(self):
        """test_int_x2_with_undercore"""
        input="0b101_010101_1_101"
        expect="0b1010101011101,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,116))

    def test_int_x2_with_undercore2(self):
        """test_int_x2_with_undercore"""
        input="0B101_010101_1_101"
        expect="0B1010101011101,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,117))
    #   float
        # float = int +decimal
    def test_float_int_and_decimal_compo_no_undercore_1(self):
        """test_float_full_compo_no_undercore_1"""
        input='0.00001'
        expect='0.00001,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,119))
        
    def test_float_int_and_decimal_compo_no_undercore_2(self):
        """test_float_full_compo_no_undercore_2"""
        input='121232.04343001'
        expect='121232.04343001,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,120))

    def test_float_int_and_decimal_compo_with_undercore_1(self):
        """test_float_full_compo_with_undercore_1"""
        input='12_1_232.04343001'
        expect='121232.04343001,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,131))
        # float = int +exp
    def test_float_int_and_exp_compo_no_undercore_1(self):
        """test_float_int_and_exp_compo_no_undercore_1"""
        input='1e424'
        expect='1e424,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,121))

    def test_float_int_and_exp_compo_no_undercore_2(self):
        """test_float_int_and_exp_compo_no_undercore_2"""
        input='1e-424'
        expect='1e-424,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,122))

    def test_float_int_and_exp_compo_no_undercore_3(self):
        """test_float_int_and_exp_compo_no_undercore_3"""
        input='1e+424'
        expect='1e+424,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,123))

    def test_float_int_and_exp_compo_with_undercore_1(self):
        """test_float_int_and_exp_compo_with_undercore_1"""
        input='1_42e424'
        expect='142e424,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,132))

    def test_float_int_and_exp_compo_with_undercore_2(self):
        """test_float_int_and_exp_compo_with_undercore_2"""
        input='1_432e-424'
        expect='1432e-424,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,133))

    def test_float_int_and_exp_compo_with_undercore_3(self):
        """test_float_int_and_exp_compo_with_undercore_3"""
        input='153_432e+424'
        expect='153432e+424,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,134))      

        # float = dec +exp
    def test_float_dec_and_exp_compo_no_undercore_1(self):
        """test_float_dec_and_exp_compo_no_undercore_1"""
        input='.0e543'
        expect='.0e543,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,124))

    def test_float_dec_and_exp_compo_no_undercore_2(self):
        """test_float_dec_and_exp_compo_no_undercore_2"""
        input='.0e-543'
        expect='.0e-543,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,125))

    def test_float_dec_and_exp_compo_no_undercore_3(self):
        """test_float_dec_and_exp_compo_no_undercore_3"""
        input='.21E-543'
        expect='.21E-543,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,126))

        # float = int + dec + exp
    def test_float_int_dec_exp_compo_no_undercore_1(self):
        """test_float_int_dec_exp_compo_no_undercore_1"""
        input="0.2132e534"
        expect="0.2132e534,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,127))

    def test_float_int_dec_exp_compo_no_undercore_2(self):
        """test_float_int_dec_exp_compo_no_undercore_2"""
        input="2132432.2132e534"
        expect="2132432.2132e534,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,128))
    
    def test_float_int_dec_exp_compo_no_undercore_3(self):
        """test_float_int_dec_exp_compo_no_undercore_3"""
        input="2132432.2132e+534"
        expect="2132432.2132e+534,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,129))
    
    def test_float_int_dec_exp_compo_no_undercore_4(self):
        """test_float_int_dec_exp_compo_no_undercore_4"""
        input="2132432.2132E-534"
        expect="2132432.2132E-534,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,130))

    def test_float_int_dec_exp_compo_with_undercore_1(self):
        """test_float_int_dec_exp_compo_with_undercore_1"""
        input="1_0.2132e534"
        expect="10.2132e534,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,135))
    
    def test_float_int_dec_exp_compo_with_undercore_2(self):
        """test_float_int_dec_exp_compo_with_undercore_2"""
        input="21_324_32.2132e+534"
        expect="2132432.2132e+534,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,136))
    
    def test_float_int_dec_exp_compo_with_undercore_4(self):
        """test_float_int_dec_exp_compo_with_undercore_4"""
        input="2_13243_2.2132E-534"
        expect="2132432.2132E-534,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,137))
    
    # string literals

    def test_string_normal(self):
        input='"ahihi xin  cac ban"'
        expect="ahihi xin  cac ban,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,138))

    def test_string_tab(self):
        """test_string_tab"""
        input=r""""This is a string containing tab \t" """
        expect=r"This is a string containing tab \t,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,139))
    
    def test_string_tab2(self):
        """test_string_tab2"""
        input= '"This is a string containing tab \\t"'
        expect="This is a string containing tab \\t,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,140))

    def test_string_tab3(self):
        """test_string_tab3"""        
        input= "\"This is a string containing tab \\t\""
        expect="This is a string containing tab \\t,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,141))
    
    def test_string_wrongescape(self):
        """test_string_wrongescape"""
        input= r"""
        "a?"
        """
        expect="a?,<EOF>"        
        self.assertTrue(TestLexer.test(input,expect,142))

    # def test_string_doublequote(self):
    #     """test_string_doublequote"""
    #     input= "\"He asked me:\'\"Where is John?\'\""
    #     expect="He asked me: '\"Where is John?'\",<EOF>"        
    #     self.assertTrue(TestLexer.test(input,expect,143))

    # def test_string_doublequote(self):
    #     """test_string_doublequote"""
    #     input= "\"ahihi xin chao\""
        
    #     expect="ahihi xin chao,<EOF>"        
    #     self.assertTrue(TestLexer.test(input,expect,143))

    def test_string_doublequote(self):
        """test_string_doublequote"""
        input="\"He asked me: '\"Where is John?'\"\""
        expect="He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,143))
    
    def test_string_newline(self):
        """test_string_newline"""
        input="\"He asked me: '\"Where is John?'\" and end with newline \\n\""
        expect="He asked me: '\"Where is John?'\" and end with newline \\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,144))

