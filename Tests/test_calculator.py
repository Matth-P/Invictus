import unittest
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Calculadora.calculator import Calculator


class Test_Calcualtor(unittest.TestCase):
    
        def test_sum(self):
           self.assertEqual(Calculator.sum(5,5),10)
           self.assertEqual(Calculator.sum(-5,5),0)
           self.assertEqual(Calculator.sum(-5,0),-5)
           
        def test_sub(self):
            self.assertEqual(Calculator.sub(5,5),0)
            self.assertEqual(Calculator.sub(0,-5), 5)
            self.assertEqual(Calculator.sub(-5,-5),0)  
        
        def test_mult(self):
            self.assertEqual(Calculator.mult(5,5),25)
            self.assertEqual(Calculator.mult(5,-5),-25)
            self.assertEqual(Calculator.mult(-5,-5),25)
        
        def test_div(self):
            self.assertEqual(Calculator.div(25,5),5)
            self.assertEqual(Calculator.div(5,5),1)
            self.assertEqual(Calculator.div(5,5),1)
            self.assertEqual(Calculator.div(5,25),0.2)
            with  self.assertRaises(ZeroDivisionError):
                Calculator.div(5,0)

                
if __name__ == "__main__":
    unittest.main()                