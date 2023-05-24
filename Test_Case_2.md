# Test Case 2

### Description:

Test if a file in originals folder is moved to finals folder when file name is in the droplist. 

### Input:

File name: Wilson
File contents: Mr Josh Wilson
               34 Glenn coves
               Gilbertburgh
               IG4 0JE
Terminal Command: python3 document_updater.py target_directory

File name added to droplist

### Expected output:

File named Wilson is not added to the finals folder as Wilson is in the droplist

### Actual output:

No droplist file found in file system. Had to manual make droplist file and remove allowlist as they can not be run in parallel.

Once the file is made and name is added the file does not appear in finals. This is the correct functionality.  

### Notes:

No droplist file is in the file system for the application.

Unable to use droplist unless droplist file is manually added. If manually added an error message is shown saying an allowlist and droplist cannot be present at the same time. Allowlist must be removed to run the test. This is known about

