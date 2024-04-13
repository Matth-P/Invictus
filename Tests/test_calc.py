import unittest
from calculator import Calculator

class Test_Calcualtor(unittest.TestCase):
    
        def test_sum(self):
           calc = Calculator()
           result = calc.sum(2,5)
           self.assertEqual(result,7)
           
        def test_sub(self):
            calc = Calculator()
            result  = calc.sub(9,8)
            self.assertEqual(result,1) 
        
        def test_mult(self):
            calc = Calculator()
            result = calc.mult(5,5)
            self.assertEqual(result,25)
        
        def test_div(self):
            calc = Calculator()
            result = calc.div(5,5)
            self.assertEqual(result,1)      