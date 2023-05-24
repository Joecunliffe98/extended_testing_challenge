# Test Case 1 

### Description:

Test if a file in orignals folder is moved to finals folder when file name is in the allowlist. No updates are to be done on this file.

### Input:

File name: Lane

File contents: 

               Dr Katie Lane
               Flat 17i
               Walsh spur
               Leonport
               RM1 2TJ
               
Terminal Command: python3 document_updater.py target_directory

File name added to allowlist

### Expected output:

File named Lane is moved to finals folder with the correct file contents

### Actual output:

File is not added to finals folder if the file name is in the allowlist file

### Notes:

File is only added to finals folder when an update is given in the updates folder and the file name is in the allowlist. An orignal file is not required in order for the update to go through into the finals folder.

Originals folder/allowlist not working as intended?

If a file is in the originals folder and on the allowlist it will NOT be added to the finals folder when the program is run
