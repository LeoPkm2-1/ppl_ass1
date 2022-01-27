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
        input = """Class main{}"""
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
    
    def test_class_with_static(self):
        """test_class_with_static"""
        input="""
            Class c{
                Var $fds,$b:Int;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,204))
        
    def test_class_with_static_and_instance(self):
        """test_class_with_static"""
        input="""
            Class c{
                Var $fds,$b,c,f,e,$err:String;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_const_instance(self):
        """test_class_with_static"""
        input="""
            Class c{
                Val c,f,e,$err:String;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_const_static(self):
        """test_const_static"""
        input="""
            Class c{
                Val $c,$f,$e,$err:String;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_const_staticAndinstance(self):
        """test_const_staticAndinstance"""
        input="""
            Class c{
                Val $c,f,$e,err:Float;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_var_decl_with_int_inital(self):
        """test_var_decl_with_int_inital"""
        input="""
            Class c{
                Var a,s42,_543:Int=43,54,a;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_var_decl_with_float_inital(self):
        """test_var_decl_with_float_inital"""
        input="""
            Class c{
                Var a,s42,_543:Float=4.3,.0e-100,a;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_var_decl_with_bool_inital(self):
        """test_var_decl_with_bool_inital"""
        input="""
            Class c{
                Var a,s42,_543:Boolean=True,False,True;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_var_decl_with_string_inital(self):
        """test_var_decl_with_string_inital"""
        input="""
            Class c{
                Var a,s42,_543:String="ahihi xin chao","","132","Flo;t","True",a,$a_S21;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_class_with_comment(self):
        """test_class_with_comment"""
        input="""
            Class c{
                ## ##
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_class_with_comment2(self):
        """test_class_with_comment"""
        input="""
            Class c{
                ## 
                
                
                ##
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_class_with_comment3(self):
        """test_class_with_comment"""
        input="""
            Class c{
                ## 
                noting ok ahihi
                
                ##
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_class_with_comment4(self):
        """test_class_with_comment"""
        input="""
            Class c{
                ## 
                Var a,s42,_543:Int = 4,5,3;
                
                ##
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_class_with_arr1(self):
        """test_class_with_arr"""
        input="""
            Class c{
                Var a,b,c: Array[Int,5];
                Var a,b,c: Array[Boolean,5];
                Var a,b,c: Array[Float,5];
                Var a,b,c: Array[String,5];
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_class_with_arr(self):
        """test_class_with_arr"""
        input="""
            Class c{
                Var a,b,c: Array[Int,5]=Array(12,0X43,a,$fas);
                Var a,b,c: Array[Boolean,5]=Array(True,False,True);
                Var a,b,c: Array[Float,5]=Array(1.0,0.,1e342,1.432,1.42e+424,afsa3);
                Var a,b,c: Array[String,5]=Array("fdsa fsjlk ","fdsaj",afsd,$fsad);
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,217))


    def test_class_with_arr2(self):
        """test_class_with_arr"""
        input="""
            Class c{
                Var a,b,c: Array[Array[int,1],5]=Array(
                    Array(12),
                    Array(1),
                    Array(a),
                    Array($sa),
                    Array(012)
                );
                Var a,b,c: Array[Boolean,5]=Array(True,False,True);
                Var a,b,c: Array[Float,5]=Array(1.0,0.,1e342,1.432,1.42e+424,afsa3);
                Var a,b,c: Array[String,5]=Array("fdsa fsjlk ","fdsaj",afsd,$fsad);
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,218))