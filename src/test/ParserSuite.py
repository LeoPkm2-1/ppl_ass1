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
                Var a,b,c: Array[
                    Array[Int,2],3]=Array( Array(
                        Array(
                            Array(3,4),Array(
                                Array(3,4),Array(5,6)
                            )
                        ),Array(5,6)
                    ),Array(3,4),Array(5,6)  )   ;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_method_nobody1(self):
        """test_method_nobody1 """
        input="""
            Class c{
                Var a,b,c:Int;
                Val e,c,d:Float;
                Var $r,t:Array[Boolean,3]=Array(True,False,True);
                Var a,b,c: Array[
                    Array[Int,2],3]=Array( Array(
                        Array(
                            Array(3,4),Array(
                                Array(3,4),Array(5,6)
                            )
                        ),Array(5,6)
                    ),Array(3,4),Array(5,6)  )   ;
                
                ahihi(){}
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_method_nobody2(self):
        """test_method_nobody1 """
        input="""
            Class c{
                Var a,b,c:Int;
                Val e,c,d:Float;
                Var $r,t:Array[Boolean,3]=Array(True,False,True);
                Var a,b,c: Array[
                    Array[Int,2],3]=Array( Array(
                        Array(
                            Array(3,4),Array(
                                Array(3,4),Array(5,6)
                            )
                        ),Array(5,6)
                    ),Array(3,4),Array(5,6)  )   ;
                
                ahihi(a,b:Int){}
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_method_nobody3(self):
        """test_method_nobody3 """
        input="""
            Class c{
                Var a,b,c:Int=10,A,Car::$c;
                Val e,c,d:Float;
                Var d,e:String="ahihi","ahaihi"+."hehe";
                Var $r,t:Array[Boolean,3]=Array(True,False,True);
                Var a,b,c: Array[
                    Array[Int,2],3]=Array( Array(
                        Array(
                            Array(3,4),Array(
                                Array(3,4),Array(5,6)
                            )
                        ),Array(5,6)
                    ),Array(3,4),Array(5,6)  )   ;
                
                ahihi(a,b:Int;c,d:Float){}
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_method_nobody4(self):
        """test_method_nobody4 """
        input="""
            Class c{
                Var a,b,c:Int;
                Val e,c,d:Float;
                Var $r,t:Array[Boolean,3]=Array(True,False,True);
                Var a,b,c: Array[
                    Array[Int,2],3]=Array( Array(
                        Array(
                            Array(3,4),Array(
                                Array(3,4),Array(5,6)
                            )
                        ),Array(5,6)
                    ),Array(3,4),Array(5,6)  )   ;
                
                ahihi(a,b:Int;e,f,g:Array[Int,5]){}
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_method_nobody5(self):
        """test_method_nobody5 """
        input="""
            Class c{
                               
                ahihi(a:Array[Array[Array[Int,10],5],3];e:Array[Int,5]){}
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_method_nobody6(self):
        """test_method_nobody6 """
        input="""
            Class c{
                               
                ahihi(a:Array[Array[Array[Int,10],5],3];e:ahihi){}
            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def te(self):
        """test_temp """
        input="""
            Class c{
                               
                ## Car::$funct(1,2,3)##
                Car.$ahihi

            }
        """
        expect="successful"
        self.assertTrue(TestParser.test(input,expect,225))

    # def test_class_with_arr2(self):
    #     """test_class_with_arr"""
    #     input="""
    #         Class c{
    #             Var a,b,c: Array[Array[Int,1],5];
    #             Var a,b,c: Array[Boolean,5]=Array(True,False,True);
    #             Var a,b,c: Array[Float,5]=Array(1.0,0.,1e342,1.432,1.42e+424,afsa3);
    #             Var a,b,c: Array[String,5]=Array("fdsa fsjlk ","fdsaj",afsd,$fsad);
    #         }
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect,218))

    # def test_class_with_arr2(self):
    #     """test_class_with_arr"""
    #     input="""
    #         Class c{
    #             Var a,b,c: Array[Array[int,1],5]=Array(
    #                 Array(12),
    #                 Array(1),
    #                 Array(a),
    #                 Array($sa),
    #                 Array(012)
    #             );
    #             Var a,b,c: Array[Boolean,5]=Array(True,False,True);
    #             Var a,b,c: Array[Float,5]=Array(1.0,0.,1e342,1.432,1.42e+424,afsa3);
    #             Var a,b,c: Array[String,5]=Array("fdsa fsjlk ","fdsaj",afsd,$fsad);
    #         }
    #     """
    #     expect="successful"
    #     self.assertTrue(TestParser.test(input,expect,218))