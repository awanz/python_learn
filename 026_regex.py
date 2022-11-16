import re

txt = "Where i go to your home, because i love you"
findText = re.findall("i", txt) # akan mengambil semua string i
print(findText)

searchText = re.search("y", txt) # mencari lokasi index dari string yang dicari
print(searchText.start())

searchText2 = re.search("your", txt)
print(searchText2)

splitText = re.split("\s", txt) #split string berdasarkan space dan dirubah jadi array
print(splitText)

splitTextOnlyOne = re.split("\s", txt, 1) #split string berdasarkan space dan dirubah jadi array dan 1 
print(splitTextOnlyOne)

newText = re.sub("\s", "-", txt) # replace space jadi -
print(newText)

newText2 = re.sub("\s", "-", txt, 2) # replace space jadi - only 2
print(newText2)

searchText3 = re.search("because", txt)
print(searchText3.span()) # print index angka awal dan akhir
print(searchText3.string) # print all string
print(searchText3.group()) # print string yang di carinya