import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))
    
    # def test_program_class_dec_1(self):
    #     """test_program_class_dec"""
    #     input = """Class Program { 
    #        programclassbody
    #     } """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,203))

    def test_program_class_empty_body(self):
        """test_program_class_empty_body"""
        input = """Class drogram{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))


    def test_class_have_vardecl_1(self):
        """test_temp"""
        input="""
        Class abc{
            Var a:Int;
        }

        Class c{
            Var fds,b,s,fsd: Float;
        }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,203))