
def checkIsEven(number):
  '''
  Function checkIsEven
  digunakan untuk mengecek input angka (number) merupakan angka genap atau tidak
  output dari fungsi ini adalah boolean
  '''
  if number % 2 == 0 :
    return True
  else :
    return False
  

class Calculator:
  def __init__(self, number = 0):
    self.number = number

  def __str__(self):
    return f'Calculator ini memiliki value number sejumlah {self.number}'

  def add(self, n):
    '''
    Method add
    Menambahkan n ke attribute number
    '''
    self.number += n

  def min(self, n):
    '''
    Method min
    Mengurangi n ke attribute number
    '''
    self.number -= n


if __name__ == '__main__':
  calculatorku = Calculator()
  calculatorku.add(500)
  print(calculatorku.number)



