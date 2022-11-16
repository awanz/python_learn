# sebelum code, install dulu librarynya menggunakan comment
# pip install camelcase
#

import camelcase

camelCase = camelcase.CamelCase
text = "welcome awan"

print(camelCase.hump(text))

# untuk uninstall
# pip uninstall camelcase

# untuk melihat library yang sudah pernah diinstall
# pip list