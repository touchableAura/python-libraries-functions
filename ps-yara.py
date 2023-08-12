import yara
import os 

# full path to libryara.dll
# yara_dll_path = r'C:\Users\19023\Documents\Yara\build\bin\libyara.dll'


# problems with yara 
yara_rules = yara.compile(filepath='yara-rules/test-rule.yar')

directory = '/python-libraries-functions'

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    with open(file.path, 'rb') as file:
        data = file.read()
        matches = yara_rules.match(data=data)
        if matches:
            print(f"{filename}: Matched, possibly infected!")
        else:
            print(f"{filename}: Clean")
    



