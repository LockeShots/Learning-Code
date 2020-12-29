def Dec2Bin(denary):
  output = ""
  while denary > 0:
    remainder = denary % 2
    output = str(remainder) + output
    denary = int((denary - remainder) / 2)
  return output

thenumber = int(input('enter a number to convert: '))
print(f"Binary value = {Dec2Bin(thenumber)}")