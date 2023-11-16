# 1. file tersendiri testing
# 2. import unittest 
# 3. import file dan function, class yang akan kita test 
# 4. Buat class untuk testing 
# 5. Membuat method dengan keyword awalnya "test"
#    5.1 Pertimbangan input 
#    5.2 Process (pemanggilan function yang akan ditest)
#    5.3 Melakukan pengecekan ke perubahan
# 6. Eksekusi unittest.main()

import unittest
from calculator import checkIsEven, Calculator

class TestCheckIsEven(unittest.TestCase):
  def test_even(self):
    input = 50 
    result = checkIsEven(input)
    self.assertEqual(result, True)

  def test_odd(self):
    input = 55 
    result = checkIsEven(input)
    self.assertEqual(result, False)

class TestCalculator(unittest.TestCase):
  def test_add(self):
    object = Calculator()
    object.add(50)
    self.assertEqual(object.number, 50)

  def test_min(self):
    object1 = Calculator()
    object1.min(50)
    self.assertEqual(object1.number, -50)

if __name__ == '__main__':
  unittest.main()