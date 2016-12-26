# RandomScripts

Folder_files_compare.py:
There are three dictionaries.
1. All_files will contain all filenames.
2. Original_jpeg_files will contain all jpeg image filenames.
3. Hashed_jpeg_files will contain all MD5 filenames.

Dictionary is faster in access as it is O(1) operation. We finally compare or check the existence of filenames(Keys) in both 'Original_jpeg_files' and 'Hashed_jpeg_files', failing to which means there is a file missing (Either jpeg or MD5).



csvTojson.py:
Python Script to parse a csv input file containing source and destination URLComponents
and convert them to akamai PAPI specific json data. This script is limited to redirect
behavior.

