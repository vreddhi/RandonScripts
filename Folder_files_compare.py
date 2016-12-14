import os

original_files = { }

for file in os.listdir():
    if file.endswith(".jpg"):
        filename = file.split('.')[:-1]
        original_files[file] = "MISSING"

for file in os.listdir():
    if file.endswith(".md5"):
        filename = file.split('.')[:-2]
        if filename in original_files:
            original_files[filename] = "BOTH_EXIST"


print 'Following jpeg files do not have the corresponding MD5 hash files'
for key, value in original_files.items():
    if original_files[key] == "MISSING":
        print key
