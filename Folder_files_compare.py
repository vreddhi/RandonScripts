import os

All_files = { }
Original_jpeg_files = { }
Hashed_jpeg_files = { }

for file in os.listdir():
    if file.endswith(".jpg"):
        filename = file.split('.')[:-1]
        Original_files[filename] = "TRUE"
        All_files[filename] = "TRUE"
    if file.endswith(".md5"):
        filename = file.split('.')[:-2]
        Hashed_jpeg_files[filename] = "TRUE"
        All_files[filename] = "TRUE"  


print 'Following files do not have a complimentary jpeg or md5 hash'
for key in All_files:
    if key in Original_files and if key in Hashed_jpeg_files:
        donothing = "true"
    else:
        print key
