import unittest
import Unit

# assertEqual(expected_value,actual_value) - 
# Asserts that expected_value == actual_value

# assertTrue(result) - Asserts that bool(result) is True

# assertFalse(result) - Asserts that bool(result) is False

# assertRaises(exception, function, *args, **kwargs) - 
# Asserts that function(*args, **kwargs) raises the exception

class UnitTest(unittest.TestCase):
    def test_add(self):
        result = Unit.add(10,5)
        self.assertEqual(result, 15)

    def test_sub(self):
        result = Unit.sub(10,5)
        self.assertEqual(result, 5)
    
    def test_prime(self):
        self.assertTrue(Unit.is_prime(3))
        self.assertFalse(Unit.is_prime(30))

    # OUTPUT
        # ...
        # ----------------------------
        # Ran 3 tests in 0.001s
        # OK    
    

    # EXCEPTION HANDLING -  syntax 
    # def test_exception(self):
    #     self.assertRaises(exception-name,function-name,args)

    def test_typeerror_1(self):
        with self.assertRaises(TypeError):
            Unit.is_prime(6.5)
            Unit.is_prime(4.9)

    def test_typeerror_2(self):
        with self.assertRaises(TypeError):
            Unit.is_prime('five')
            Unit.is_prime("six")
            Unit.is_prime(True)

    def test_valueerror(self):
        with self.assertRaises(ValueError):
            Unit.is_prime(-4)
            Unit.is_prime(0)
    
    #OUTPUT
    # ......
    # ----------------------------
    # Ran 6 tests in 0.001s
    # OK

if __name__=='__main__':
    unittest.main()
