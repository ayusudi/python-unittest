try:
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  inputIndex = input("Silahkan input index 0-25 : ")
  index = int(inputIndex)
  if index < 0 :
    raise Exception('Index tidak menerima minus')
  print(alphabet[index], index)
except Exception as e :
  print("Ada kegagalan")
  print(e)
finally:
  print("Terimakasih telah menggunakan program ini")


# try:
#   alphabet = 'abcdefghijklmnopqrstuvwxyz'
#   inputIndex = input("Silahkan input index 0-25 : ")
#   index = int(inputIndex)
#   print(alphabet[index], index)
# except:
#   print("Ada kegagalan")