try:
    print("jika sukses")
except:
    print("jika ada error")
else:
    print("akan menjalankan ketika tidak ada apa-apa")

try:
  f = open("example.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")