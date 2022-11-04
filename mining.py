import hashlib
import sha3

fixedString="KeigoYanai20220420"
nonce = 0
zeroCounter = 0

while True:
  inputString = fixedString + str(nonce)
  hash = hashlib.sha3_256(inputString.encode('utf-8')).hexdigest()
  nonce += 1
  if hash[0:7] == "0000000":
    zeroCounter = 28
    if hash[7] == "0":
      zeroCounter += 4
    elif hash[7] == "1":
      zeroCounter += "3"
    elif hash[7] == "2" or hash[7] == "3":
      zeroCounter += 2
    elif hash[7] == "4" or hash[7] == "5" or hash[7] == "6" or hash[7] == "7":
      zeroCounter += 1
    break
print("Input", inputString)
print("Nonce", nonce)
print("Hash", hash)
print("先頭の0のbit数", zeroCounter)
