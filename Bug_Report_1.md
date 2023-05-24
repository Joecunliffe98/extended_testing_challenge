## Allowlist does not work with originals folder

### Description:

When a file is in the originals folder it cannot be put into the finals folder even when the file name is added to the allowlist.

### Input:

File name: Lane
File contents: Dr Katie Lane
               Flat 17i
               Walsh spur
               Leonport
               RM1 2TJ
               
Terminal Command: python3 document_updater.py target_directory

File name added to allowlist

### Notes:

If a file is in the originals folder and on the allowlist it will NOT be added to the finals folder when the program is ran. This is also the case if the file name is not in the allowlist.

Files from originals will not be added to finals unless updated at some point using the updates folder and allowlists file.

### Severity: High

### Priority: High

This is a piece of core functionality that is not working correctly. The orignals folder is not being accessed or used as intended. 
