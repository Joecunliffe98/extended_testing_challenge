# Test Case 3

### Description:

Test if a file in originals folder can be updated using the update folder and moved to the finals folder if name is in the allowlist

### Input:

File name: Brown

File contents: 

               Dr Victoria Brown
               Flat 18G
               Mason tunnel
               Justinton
               E68 6RQ
               
Terminal Command: python3 document_updater.py target_directory

File name added to allowlist

### Expected output:

File named Brown is visible in originals folder with the old data but also visible in the updates folder with the new data. This file is added to the finals folder with the new data. 

### Actual output:

File is added to the finals folder with the update data but the original file still exists with the old data. This is as intended.
 

### Notes:

Updates folder and allowlist work as intended. 
