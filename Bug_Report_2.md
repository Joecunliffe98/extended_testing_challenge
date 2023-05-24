## Allowlist causes an Index error if empty

### Description:

If the allowlist is left empty and the program is run an Index error is thrown 

Index error: list index out of range

### Input:

Allowlist file empty

### Notes:

If the updates and originals folder contain files but no files are found in the allowlist then the program will not run and an error is thrown. 

Maybe a curated error message should be made to tell the user what the issue is (if this is the intended function).

An error message already exists for if the allowlist/droplist cannot be found in the directory so why is there no message for an empty file?

### Severity: Medium

### Priority: Medium

This is a commonly used file that may be left empty whether on purpose or accidentally so an infomative error message should be given to the user.
